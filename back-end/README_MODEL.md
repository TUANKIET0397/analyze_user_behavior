# Fashion Category Prediction

XGBoost model dự đoán Category (Clothing / Accessories / Footwear)

## Cấu trúc project

```
back-end/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
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
│       └── mapper.py
├── models/
│   ├── xgb_category.json
│   ├── label_encoder.pkl
│   └── train_cols.pkl
├── app.db
├── train_and_save.py
├── requirements.txt
└── README_MODEL.md
```

---

## Setup

### 1. Cài dependencies

```bash
pip install -r requirements.txt
```

### 2. Đặt file data

Đặt file `shopping_trends_updated.csv` vào thư mục gốc (cùng cấp với `train_and_save.py`).

### 3. Train và lưu model

```bash
python train_and_save.py
```

Sau bước này thư mục `models/` sẽ được tạo với 3 files.

### 4. Chạy API server

```bash
python -m uvicorn app.main:app --reload
```

API chạy tại: http://localhost:8000

---

hình ảnh - tên - giá tiền bảng category: Footwear - Accessories - clothing

## API Endpoints

| Method | Endpoint                           | Mô tả                     |
| ------ | ---------------------------------- | ------------------------- |
| GET    | `/`                                | Kiểm tra server           |
| GET    | `/health`                          | Trạng thái server + model |
| POST   | `/api/predictions`                 | Dự đoán 1 user + lưu DB   |
| GET    | `/api/predictions`                 | Danh sách lịch sử dự đoán |
| GET    | `/api/predictions/{prediction_id}` | Chi tiết 1 dự đoán        |
| GET    | `/api/predictions/{prediction_id}/products` | Chi tiết 1 dự đoán + gợi ý sản phẩm |
| DELETE | `/api/predictions/{prediction_id}` | Xoa 1 dự đoán             |

### Swagger UI

Truy cập http://localhost:8000/docs để xem và test API trực tiếp.

---

## Ví dụ Request

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
