from pydantic import BaseModel, Field
from typing import Literal, Optional


# Request
class UserInput(BaseModel):
    """Thông tin đầu vào của 1 user."""

    # Thông tin cá nhân
    age: int = Field(..., ge=1, le=100, example=28)
    gender: Literal["Male", "Female"] = Field(..., example="Male")

    # Giao dịch
    purchase_amount: float = Field(..., gt=0, alias="purchase_amount_usd", example=45.5)
    review_rating: float   = Field(..., ge=1.0, le=5.0, example=3.8)
    season: Literal["Spring", "Summer", "Fall", "Winter"] = Field(..., example="Fall")

    # Lịch sử
    previous_purchases: int = Field(..., gt=0, example=12)
    frequency_of_purchases: Literal[
    "weekly",
    "bi-weekly",
    "fortnightly",
    "monthly",
    "every 3 months",
    "quarterly",
    "annually"
    ] = Field(...)
    
    # Subscription
    subscription_status: Literal["Yes", "No"] = Field(..., example="Yes")

    # Tham số tuỳ chọn
    top_n: Optional[int] = Field(default=2, ge=1, le=3, description="Số categories trả về")

    class Config:
        populate_by_name = True

    def to_raw_dict(self) -> dict:
        """Chuyển sang dict với tên cột khớp với DataFrame lúc train."""
        return {
            "Age":                    self.age,
            "Gender":                 self.gender,
            "Purchase Amount (USD)":  self.purchase_amount,
            "Review Rating":          self.review_rating,
            "Season":                 self.season,
            "Previous Purchases":     self.previous_purchases,
            "Frequency of Purchases": self.frequency_of_purchases,
            "Subscription Status":    self.subscription_status,
        }


# Response
class CategoryResult(BaseModel):
    category:   str
    confidence: float


class PredictResponse(BaseModel):
    predicted:      str                   
    confidence:     float                 
    top_categories: list[CategoryResult]  

class HealthResponse(BaseModel):
    status:  str
    model:   str
    version: str
