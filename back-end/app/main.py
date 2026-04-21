# Diem vao FastAPI: tao app, CORS, dang ky router va startup DB.
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, SessionLocal, engine
from app.ml.model import _model
from app.routers.prediction_router import router as predictions_router
from app.schemas.prediction_schema import HealthResponse
from app.utils.seed_data import seed_category_products


# App
app = FastAPI(
    title="Fashion Category Prediction API",
    description="Backend demo nho cho du an: du doan category + luu lich su.",
    version="2.0.0",
)

# CORS —  call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", tags=["Root"])
def root():
    return {"message": "Fashion Category Prediction API is running."}


@app.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check():
    return HealthResponse(
        status="ok" if _model is not None else "model_not_loaded",
        model="XGBoost Category Classifier",
        version="2.0.0",
    )

@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)
    with engine.connect() as conn:
        result = conn.execute(text("PRAGMA table_info(prediction_history)"))
        cols = {row[1] for row in result}
        if "top_categories_json" not in cols:
            conn.execute(
                text("ALTER TABLE prediction_history ADD COLUMN top_categories_json TEXT")
            )
            conn.commit()
    db = SessionLocal()
    try:
        seed_category_products(db)
    finally:
        db.close()


app.include_router(predictions_router)
