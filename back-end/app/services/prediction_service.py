# Service layer: xu ly du doan va luu/tra lich su DB.
from sqlalchemy.orm import Session

from app.ml.model import _model, predict_category
from app.models.category_product import CategoryProduct
from app.models.prediction import PredictionHistory
from app.schemas.prediction_schema import (
    CategoryResult,
    CategoryProductItem,
    PredictionData,
    PredictionDataDetailed,
    PredictionInput,
    PredictionProductsData,
    PredictionResult,
    PredictionResultDetailed,
)
from app.utils.mapper import map_input_to_raw


def create_prediction_record(
    db: Session,
    payload: PredictionInput,
    top_n: int = 2,
) -> PredictionDataDetailed:
    if _model is None:
        raise RuntimeError("Model not loaded. Run train_and_save.py first.")

    model_result = predict_category(raw_input=map_input_to_raw(payload), top_n=top_n)
    top_categories = [CategoryResult(**item) for item in model_result["top_categories"]]
    # Luu trang thai subscription theo bool de phu hop schema DB
    subscription_status_bool = payload.subscription_status == "Yes"

    record = PredictionHistory(
        age=payload.age,
        gender=payload.gender,
        purchase_amount_usd=payload.purchase_amount_usd,
        review_rating=payload.review_rating,
        previous_purchases=payload.previous_purchases,
        season=payload.season,
        subscription_status=subscription_status_bool,
        frequency_of_purchases=payload.frequency_of_purchases,
        # Khong con nhan discount_applied tu client, dat mac dinh False
        discount_applied=False,
        predicted_category=model_result["predicted"],
        confidence=model_result["confidence"],
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return PredictionDataDetailed(
        id=record.id,
        input=payload,
        prediction=PredictionResultDetailed(
            predicted_category=model_result["predicted"],
            confidence=model_result["confidence"],
            top_categories=top_categories,
        ),
        created_at=record.created_at,
    )


def build_prediction_data(record: PredictionHistory) -> PredictionData:
    # Dung schema PredictionData va tra ve top_categories cho frontend
    if _model is not None:
        raw_input = {
            "Age": record.age,
            "Gender": record.gender,
            "Purchase Amount (USD)": record.purchase_amount_usd,
            "Review Rating": record.review_rating,
            "Previous Purchases": record.previous_purchases,
            "Season": record.season,
            "Subscription Status": "Yes" if record.subscription_status else "No",
            "Frequency of Purchases": record.frequency_of_purchases,
            "Discount Applied": "No",
        }
        model_result = predict_category(raw_input=raw_input, top_n=2)
        top_categories = [CategoryResult(**item) for item in model_result["top_categories"]]
        prediction = PredictionResultDetailed(
            predicted_category=model_result["predicted"],
            confidence=model_result["confidence"],
            top_categories=top_categories,
        )
    else:
        # Neu model chua load thi tra ve thong tin da luu
        prediction = PredictionResultDetailed(
            predicted_category=record.predicted_category,
            confidence=record.confidence,
            top_categories=[],
        )

    return PredictionData(
        id=record.id,
        input=PredictionInput(
            age=record.age,
            gender=record.gender,
            purchase_amount_usd=record.purchase_amount_usd,
            review_rating=record.review_rating,
            previous_purchases=record.previous_purchases,
            season=record.season,
            subscription_status="Yes" if record.subscription_status else "No",
            frequency_of_purchases=record.frequency_of_purchases,
        ),
        prediction=prediction,
        created_at=record.created_at,
    )


def build_prediction_products_data(
    db: Session,
    record: PredictionHistory,
) -> PredictionProductsData:
    prediction = build_prediction_data(record)
    products = (
        db.query(CategoryProduct)
        .filter(CategoryProduct.category == record.predicted_category)
        .all()
    )
    product_items = [
        CategoryProductItem(
            id=item.id,
            category=item.category,
            product_name=item.product_name,
            image_path=item.image_path,
            price=item.price,
        )
        for item in products
    ]
    return PredictionProductsData(prediction=prediction, products=product_items)