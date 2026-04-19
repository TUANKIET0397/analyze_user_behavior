# Service layer: xu ly du doan va luu/tra lich su DB.
import json

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
    PredictionResultDetailed,
)
from app.utils.mapper import map_input_to_raw


PRODUCT_RULES = {
    "Blouse": {
        "genders": {"Female", "Unisex"},
        "seasons": {"Spring", "Summer"},
        "tags": {"basic"},
        "tier": "medium",
    },
    "Sweater": {
        "genders": {"Female", "Unisex"},
        "seasons": {"Fall", "Winter"},
        "tags": {"basic", "repeat_purchase"},
        "tier": "medium",
    },
    "Jeans": {
        "genders": {"Male", "Unisex"},
        "seasons": {"Spring", "Fall"},
        "tags": {"basic", "repeat_purchase"},
        "tier": "medium",
    },
    "Shirt": {
        "genders": {"Male", "Unisex"},
        "seasons": {"Spring", "Summer"},
        "tags": {"basic", "repeat_purchase"},
        "tier": "basic",
    },
    "Shorts": {
        "genders": {"Male", "Unisex"},
        "seasons": {"Summer"},
        "tags": {"casual"},
        "tier": "basic",
    },
    "Coat": {
        "genders": {"Male", "Female", "Unisex"},
        "seasons": {"Fall", "Winter"},
        "tags": {"seasonal"},
        "tier": "medium",
    },
    "Dress": {
        "genders": {"Female"},
        "seasons": {"Spring", "Summer"},
        "tags": {"occasion"},
        "tier": "premium",
    },
    "Skirt": {
        "genders": {"Female"},
        "seasons": {"Spring", "Summer"},
        "tags": {"occasion"},
        "tier": "medium",
    },
    "Pants": {
        "genders": {"Male", "Unisex"},
        "seasons": {"Fall", "Winter"},
        "tags": {"basic", "repeat_purchase"},
        "tier": "basic",
    },
    "Jacket": {
        "genders": {"Male", "Unisex"},
        "seasons": {"Spring", "Fall"},
        "tags": {"casual"},
        "tier": "medium",
    },
    "Hoodie": {
        "genders": {"Male", "Unisex"},
        "seasons": {"Fall", "Winter"},
        "tags": {"basic", "repeat_purchase"},
        "tier": "basic",
    },
    "T-shirt": {
        "genders": {"Male", "Unisex"},
        "seasons": {"Spring", "Summer"},
        "tags": {"basic", "repeat_purchase"},
        "tier": "basic",
    },
    "Socks": {
        "genders": {"Male", "Female", "Unisex"},
        "seasons": {"Spring", "Summer", "Fall", "Winter"},
        "tags": {"basic", "repeat_purchase", "practical"},
        "tier": "basic",
    },
    "Sandals": {
        "genders": {"Male", "Unisex"},
        "seasons": {"Spring", "Summer"},
        "tags": {"casual"},
        "tier": "basic",
    },
    "Sneakers": {
        "genders": {"Male", "Unisex"},
        "seasons": {"Spring", "Summer", "Fall"},
        "tags": {"basic", "repeat_purchase", "practical"},
        "tier": "medium",
    },
    "Shoes": {
        "genders": {"Male", "Unisex"},
        "seasons": {"Fall", "Winter"},
        "tags": {"occasion"},
        "tier": "premium",
    },
    "Boots": {
        "genders": {"Male", "Unisex"},
        "seasons": {"Fall", "Winter"},
        "tags": {"seasonal"},
        "tier": "medium",
    },
    "Handbag": {
        "genders": {"Female"},
        "seasons": {"Spring", "Summer", "Fall", "Winter"},
        "tags": {"occasion"},
        "tier": "premium",
    },
    "Sunglasses": {
        "genders": {"Male", "Female", "Unisex"},
        "seasons": {"Spring", "Summer"},
        "tags": {"practical"},
        "tier": "medium",
    },
    "Jewelry": {
        "genders": {"Female"},
        "seasons": {"Spring", "Summer", "Fall", "Winter"},
        "tags": {"occasion"},
        "tier": "premium",
    },
    "Scarf": {
        "genders": {"Male", "Female", "Unisex"},
        "seasons": {"Fall", "Winter"},
        "tags": {"practical"},
        "tier": "basic",
    },
    "Hat": {
        "genders": {"Male", "Female", "Unisex"},
        "seasons": {"Spring", "Summer", "Fall", "Winter"},
        "tags": {"practical"},
        "tier": "basic",
    },
    "Backpack": {
        "genders": {"Male", "Female", "Unisex"},
        "seasons": {"Spring", "Summer", "Fall", "Winter"},
        "tags": {"repeat_purchase", "practical"},
        "tier": "basic",
    },
    "Belt": {
        "genders": {"Male", "Female", "Unisex"},
        "seasons": {"Spring", "Summer", "Fall", "Winter"},
        "tags": {"basic", "repeat_purchase", "practical"},
        "tier": "basic",
    },
    "Gloves": {
        "genders": {"Male", "Female", "Unisex"},
        "seasons": {"Fall", "Winter"},
        "tags": {"practical"},
        "tier": "basic",
    },
}


def _get_product_rule(product_name: str) -> dict:
    return PRODUCT_RULES.get(
        product_name,
        {
            "genders": {"Unisex"},
            "seasons": {"Spring", "Summer", "Fall", "Winter"},
            "tags": set(),
            "tier": "medium",
        },
    )


def _score_product(
    *,
    product: CategoryProduct,
    input_data: PredictionInput,
    top1_category: str,
    top2_category: str | None,
) -> tuple[float, int, float, str, int]:
    rules = _get_product_rule(product.product_name)

    score = 0.0
    category_rank = 2
    if product.category == top1_category:
        score += 50
        category_rank = 0
    elif top2_category and product.category == top2_category:
        score += 25
        category_rank = 1

    # Season match
    if input_data.season in rules["seasons"]:
        score += 20
    else:
        score -= 15

    # Gender match
    if input_data.gender in rules["genders"]:
        score += 15
    elif "Unisex" in rules["genders"]:
        score += 10
    else:
        score -= 20

    # Price proximity
    price_distance = abs(product.price - input_data.purchase_amount_usd)
    score += max(0.0, 20.0 - price_distance)

    # Repeat purchase / basic preference when user is likely to buy repeatedly
    if (
        input_data.previous_purchases >= 5
        and input_data.frequency_of_purchases in {"weekly", "bi-weekly", "fortnightly"}
        and input_data.subscription_status == "Yes"
    ):
        if rules["tags"].intersection({"repeat_purchase", "basic", "practical"}):
            score += 12
        if rules["tags"].intersection({"occasion", "premium", "high_risk"}):
            score -= 8

    # Rating is low -> avoid premium/high-risk
    if input_data.review_rating < 3.5:
        if rules["tier"] in {"basic", "medium"}:
            score += 5
        elif rules["tier"] in {"premium", "high_risk"}:
            score -= 5

    return (
        score,
        category_rank,
        price_distance,
        product.product_name,
        product.id,
    )


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
        top_categories_json=json.dumps(model_result["top_categories"]),
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
    # Dung schema PredictionData va tra ve thong tin da luu, khong tai du doan
    top_categories = []
    if record.top_categories_json:
        try:
            top_categories = [
                CategoryResult(**item)
                for item in json.loads(record.top_categories_json)
            ]
        except (TypeError, ValueError):
            top_categories = []

    prediction = PredictionResultDetailed(
        predicted_category=record.predicted_category,
        confidence=record.confidence,
        top_categories=top_categories,
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
    top_categories = [item.category for item in prediction.prediction.top_categories]
    top1 = top_categories[0] if len(top_categories) > 0 else record.predicted_category
    top2 = top_categories[1] if len(top_categories) > 1 else None

    categories = [c for c in [top1, top2] if c]
    candidates = (
        db.query(CategoryProduct)
        .filter(CategoryProduct.category.in_(categories))
        .all()
    )

    scored = [
        (item, _score_product(product=item, input_data=prediction.input, top1_category=top1, top2_category=top2))
        for item in candidates
    ]

    def sort_key(pair):
        return (
            -pair[1][0],
            pair[1][1],
            pair[1][2],
            pair[1][3].lower(),
            pair[1][4],
        )

    scored.sort(key=sort_key)

    top1_scored = [pair for pair in scored if pair[0].category == top1]
    top2_scored = [pair for pair in scored if top2 and pair[0].category == top2]

    products = [item for item, _ in top1_scored[:2]]
    if top2_scored:
        products.append(top2_scored[0][0])
    elif len(products) < 3:
        products.extend([item for item, _ in top1_scored[2:3]])
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