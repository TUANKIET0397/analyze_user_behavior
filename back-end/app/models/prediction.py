# ORM model cho bang prediction_history (luu lich su du doan).
from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class PredictionHistory(Base):
    __tablename__ = "prediction_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    gender: Mapped[str] = mapped_column(String(20), nullable=False)
    purchase_amount_usd: Mapped[float] = mapped_column(Float, nullable=False)
    review_rating: Mapped[float] = mapped_column(Float, nullable=False, default=3.0)
    previous_purchases: Mapped[int] = mapped_column(Integer, nullable=False)
    season: Mapped[str] = mapped_column(String(20), nullable=False)
    subscription_status: Mapped[bool] = mapped_column(Boolean, nullable=False)
    frequency_of_purchases: Mapped[str] = mapped_column(String(30), nullable=False)
    discount_applied: Mapped[bool] = mapped_column(Boolean, nullable=False)
    predicted_category: Mapped[str] = mapped_column(String(50), nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    top_categories_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
