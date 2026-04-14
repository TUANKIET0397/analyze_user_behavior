# Router API: nhan request, goi service, tra ve schema response.
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.prediction import PredictionHistory
from app.schemas.prediction_schema import (
    PredictionCreateResponse,
    PredictionDeleteResponse,
    PredictionDetailResponse,
    PredictionInput,
    PredictionListResponse,
)
from app.services.prediction_service import build_prediction_data, create_prediction_record


router = APIRouter(prefix="/api/predictions", tags=["Predictions"])


@router.post("", response_model=PredictionCreateResponse, status_code=status.HTTP_201_CREATED)
def create_prediction(payload: PredictionInput, db: Session = Depends(get_db)):
    try:
        data = create_prediction_record(db, payload, top_n=2)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    return PredictionCreateResponse(
        message="Prediction created successfully",
        data=data,
    )


@router.get("", response_model=PredictionListResponse)
def list_predictions(db: Session = Depends(get_db)):
    records = (
        db.query(PredictionHistory)
        .order_by(PredictionHistory.created_at.desc())
        .all()
    )
    data = [build_prediction_data(record) for record in records]
    return PredictionListResponse(
        message="Prediction list retrieved successfully",
        data=data,
    )


@router.get("/{prediction_id}", response_model=PredictionDetailResponse)
def get_prediction(prediction_id: int, db: Session = Depends(get_db)):
    record = db.query(PredictionHistory).filter(PredictionHistory.id == prediction_id).first()
    if record is None:
        raise HTTPException(status_code=404, detail="Prediction not found")

    return PredictionDetailResponse(
        message="Prediction retrieved successfully",
        data=build_prediction_data(record),
    )


@router.delete("/{prediction_id}", response_model=PredictionDeleteResponse)
def delete_prediction(prediction_id: int, db: Session = Depends(get_db)):
    record = db.query(PredictionHistory).filter(PredictionHistory.id == prediction_id).first()
    if record is None:
        raise HTTPException(status_code=404, detail="Prediction not found")

    db.delete(record)
    db.commit()

    return PredictionDeleteResponse(message="Prediction deleted successfully")
