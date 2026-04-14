# Mapping: chuyen input schema sang raw input cho ML.
from app.schemas.prediction_schema import PredictionInput


def map_input_to_raw(payload: PredictionInput) -> dict:
    # Chuyển schema đầu vào sang đúng key mà pipeline ML đang cần
    return {
        "Age": payload.age,
        "Gender": payload.gender,
        "Purchase Amount (USD)": payload.purchase_amount_usd,
        "Review Rating": payload.review_rating,
        "Previous Purchases": payload.previous_purchases,
        "Season": payload.season,
        "Subscription Status": payload.subscription_status,
        "Frequency of Purchases": payload.frequency_of_purchases,
    }
