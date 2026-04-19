# Schema Pydantic cho request/response va Swagger docs.
from datetime import datetime
from typing import List, Literal

from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    age: int = Field(..., ge=1, le=100, example=28)
    gender: Literal["Male", "Female"] = Field(..., example="Male")
    purchase_amount_usd: float = Field(..., gt=0, example=45.5)
    review_rating: float = Field(..., ge=0, le=5, example=4)
    season: Literal["Spring", "Summer", "Fall", "Winter"] = Field(..., example="Fall")
    previous_purchases: int = Field(..., ge=0, example=12)
    frequency_of_purchases: Literal[
        "weekly",
        "bi-weekly",
        "fortnightly",
        "monthly",
        "every 3 months",
        "quarterly",
        "annually",
    ] = Field(..., example="monthly")
    subscription_status: Literal["Yes", "No"] = Field(..., example="No")



class CategoryResult(BaseModel):
    category: str
    confidence: float


class PredictionResult(BaseModel):
    predicted_category: str
    confidence: float


class PredictionResultDetailed(PredictionResult):
    top_categories: list[CategoryResult]


class PredictionData(BaseModel):
    id: int
    input: PredictionInput
    prediction: PredictionResultDetailed
    created_at: datetime


class PredictionDataDetailed(BaseModel):
    id: int
    input: PredictionInput
    prediction: PredictionResultDetailed
    created_at: datetime


class PredictionCreateResponse(BaseModel):
    message: str
    data: PredictionDataDetailed


class PredictionListResponse(BaseModel):
    message: str
    data: list[PredictionData]


class PredictionDetailResponse(BaseModel):
    message: str
    data: PredictionData


class PredictionDeleteResponse(BaseModel):
    message: str


class CategoryProductItem(BaseModel):
    id: int
    category: str
    product_name: str
    image_path: str
    price: float


class PredictionProductsData(BaseModel):
    prediction: PredictionData
    products: list[CategoryProductItem]


class PredictionProductsResponse(BaseModel):
    message: str
    data: PredictionProductsData


class HealthResponse(BaseModel):
    status: str
    model: str
    version: str

class FeatureImpact(BaseModel):
    feature: str
    impact: float
    impact_percent: float


class PredictionChartData(BaseModel):
    predicted: str
    confidence: float
    feature_importance: List[FeatureImpact]


class PredictionChartResponse(BaseModel):
    data: PredictionChartData
