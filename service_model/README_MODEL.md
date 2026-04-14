# Fashion Category Prediction

XGBoost model dự đoán Category (Clothing / Accessories / Footwear)

## Cấu trúc project

```
fashion_api/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app, routes
│   ├── model.py          # Load model + predict logic
│   ├── preprocessing.py  # Feature engineering
│   └── schemas.py        # Pydantic request/response
├── models/               # Được tạo sau khi chạy train
│   ├── xgb_category.json
│   ├── label_encoder.pkl
│   └── train_cols.pkl
├── train_and_save.py     # Chạy 1 lần để train + lưu model (kiểm tra folders models xem có đủ 3 files chưa. Nếu chưa thì chạy)
├── requirements.txt
└── README.md
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

## API Endpoints

| Method | Endpoint         | Mô tả                         |
| ------ | ---------------- | ----------------------------- |
| GET    | `/`              | Kiểm tra server               |
| GET    | `/health`        | Trạng thái server + model     |
| POST   | `/predict`       | Dự đoán 1 user                |
| POST   | `/predict/batch` | Dự đoán nhiều users (max 100) |

### Swagger UI

Truy cập http://localhost:8000/docs để xem và test API trực tiếp.

---

## Ví dụ Request

### Single predict

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 28,
    "gender": "Male",
    "purchase_amount_usd": 45.5,
    "review_rating": 3.8,
    "season": "Fall",
    "previous_purchases": 12,
    "frequency_of_purchases": "monthly",
    "subscription_status": "Yes"
  }'
```

### Response

```json
{
  "predicted": "Clothing",
  "confidence": 0.7234,
  "top_categories": [
    { "category": "Clothing", "confidence": 0.7234 },
    { "category": "Accessories", "confidence": 0.1892 }
  ]
}
```

### Batch predict

```bash
curl -X POST http://localhost:8000/predict/batch \
  -H "Content-Type: application/json" \
  -d '[
  {
    "age": 28,
    "gender": "Male",
    "purchase_amount_usd": 45.5,
    "review_rating": 3.8,
    "season": "Fall",
    "previous_purchases": 12,
    "frequency_of_purchases": "monthly",
    "subscription_status": "Yes"
  },

  {
    "age": 35,
    "gender": "Female",
    "purchase_amount_usd": 78.5,
    "review_rating": 4.6,
    "season": "Spring",
    "previous_purchases": 23,
    "frequency_of_purchases": "monthly",
    "subscription_status": "Yes"
  }
]'
```
