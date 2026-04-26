# Fashion Category Prediction

XGBoost model for predicting category (Clothing / Accessories / Footwear).

## Project Structure

```
back-end/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
│   │   ├── category_product.py
│   │   └── prediction.py
│   ├── routers/
│   │   └── prediction_router.py
│   ├── schemas/
│   │   └── prediction_schema.py
│   ├── services/
│   │   └── prediction_service.py
│   ├── ml/
│   │   ├── model.py
│   │   └── preprocessing.py
│   └── utils/
│       ├── mapper.py
│       └── seed_data.py
├── models/
│   ├── xgb_category.json
│   ├── label_encoder.pkl
│   └── train_cols.pkl
├── database.db
├── shopping_trends_updated.csv
├── static/
├── train_and_save.py
├── requirements.txt
└── README_MODEL.md
```

---

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Place the dataset file

Place `shopping_trends_updated.csv` in the project root (same level as `train_and_save.py`).

### 3. Train and save the model

```bash
python train_and_save.py
```

After this step, the `models/` folder will be created with 3 files.

### 4. Run the API server

```bash
python -m uvicorn app.main:app --reload
```

API runs at: http://localhost:8000

---

## API Endpoints

| Method | Endpoint                                    | Description                         |
| ------ | ------------------------------------------- | ----------------------------------- |
| GET    | `/`                                         | Server check                        |
| GET    | `/health`                                   | Server + model status               |
| POST   | `/api/predictions`                          | Predict one user + save to DB       |
| GET    | `/api/predictions`                          | Prediction history                  |
| GET    | `/api/predictions/{prediction_id}`          | Prediction details                  |
| GET    | `/api/predictions/{prediction_id}/products` | Prediction details + product list   |
| DELETE | `/api/predictions/{prediction_id}`          | Delete a prediction                 |

### Swagger UI

Visit http://localhost:8000/docs to view and test the API.

---

## Example Requests

### Create prediction

```bash
curl -X POST http://localhost:8000/api/predictions \
    -H "Content-Type: application/json" \
    -d '{
        "age": 28,
        "gender": "Male",
        "purchase_amount_usd": 45.5,
        "review_rating": 4,
        "season": "Fall",
        "previous_purchases": 12,
        "frequency_of_purchases": "monthly",
        "subscription_status": "No"
    }'
```

### Response

```json
{
    "message": "Prediction created successfully",
    "data": {
        "id": 1,
        "input": {
            "age": 28,
            "gender": "Male",
            "purchase_amount_usd": 45.5,
            "review_rating": 4,
            "season": "Fall",
            "previous_purchases": 12,
            "frequency_of_purchases": "monthly",
            "subscription_status": "No"
        },
        "prediction": {
            "predicted_category": "Clothing",
            "confidence": 0.7234,
            "top_categories": [
                { "category": "Clothing", "confidence": 0.7234 },
                { "category": "Accessories", "confidence": 0.1892 }
            ]
        },
        "created_at": "2026-04-14T10:00:00"
    }
}
```

### List predictions

```bash
curl http://localhost:8000/api/predictions
```

### Prediction products

```bash
curl http://localhost:8000/api/predictions/1/products
```

### Response (products)

```json
{
    "message": "Prediction products retrieved successfully",
    "data": {
        "prediction": {
            "id": 1,
            "input": {
                "age": 28,
                "gender": "Male",
                "purchase_amount_usd": 45.5,
                "review_rating": 4,
                "season": "Fall",
                "previous_purchases": 12,
                "frequency_of_purchases": "monthly",
                "subscription_status": "No"
            },
            "prediction": {
                "predicted_category": "Footwear",
                "confidence": 0.7234,
                "top_categories": [
                    { "category": "Footwear", "confidence": 0.7234 },
                    { "category": "Accessories", "confidence": 0.1892 }
                ]
            },
            "created_at": "2026-04-14T10:00:00"
        },
        "products": [
            {
                "id": 1,
                "category": "Footwear",
                "product_name": "Air Runner",
                "image_path": "static/products/footwear_01.jpg",
                "price": 79.0
            },
            {
                "id": 2,
                "category": "Footwear",
                "product_name": "Urban Sneakers",
                "image_path": "static/products/footwear_02.jpg",
                "price": 92.5
            }
        ]
    }
}
```
