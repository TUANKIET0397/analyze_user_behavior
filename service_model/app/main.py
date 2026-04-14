from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import UserInput, PredictResponse, HealthResponse
from app.model import predict_category, _model


# App
app = FastAPI(
    title="Fashion Category Prediction API",
    description="Dự đoán Category (Clothing / Accessories / Footwear) từ thông tin user.",
    version="1.0.0",
)

# CORS —  call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routes
@app.get("/", tags=["Root"])
def root():
    return {"message": "Fashion Category Prediction API is running."}


@app.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check():
    """Kiểm tra trạng thái server và model."""
    return HealthResponse(
        status  = "ok" if _model is not None else "model_not_loaded",
        model   = "XGBoost Category Classifier",
        version = "1.0.0",
    )


@app.post("/predict", response_model=PredictResponse, tags=["Prediction"])
def predict(user: UserInput):
    """
    Dự đoán Category từ thông tin user.

    Trả về:
    - **predicted**: Category dự đoán cao nhất
    - **confidence**: Độ chắc chắn (0–1)
    - **top_categories**: Danh sách top N categories với confidence
    """
    if _model is None:
        raise HTTPException(
            status_code=503,
            detail="Model chưa được load. Vui lòng chạy train_and_save.py trước.",
        )

    try:
        result = predict_category(
            raw_input=user.to_raw_dict(),
            top_n=user.top_n or 2,
        )
        return PredictResponse(**result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict/batch", response_model=list[PredictResponse], tags=["Prediction"])
def predict_batch(users: list[UserInput]):
    """
    Dự đoán nhiều users cùng lúc.
    Tối đa 100 records mỗi request.
    """
    if len(users) > 100:
        raise HTTPException(
            status_code=400,
            detail="Batch size tối đa là 100 records.",
        )

    if _model is None:
        raise HTTPException(status_code=503, detail="Model chưa được load.")

    results = []
    for user in users:
        try:
            result = predict_category(
                raw_input=user.to_raw_dict(),
                top_n=user.top_n or 2,
            )
            results.append(PredictResponse(**result))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Lỗi khi xử lý record: {e}")

    return results
