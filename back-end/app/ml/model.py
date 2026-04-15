# Tai model va cung cap ham du doan (ML inference adapter).

import pickle
from pathlib import Path

import numpy as np
import pandas as pd
import xgboost as xgb

from app.ml.preprocessing import feature_engineering, build_features

# Paths
MODEL_DIR = Path(__file__).resolve().parents[2] / "models"


# Load artifacts
def _load_artifacts():
    model = xgb.XGBClassifier()
    model.load_model(MODEL_DIR / "xgb_category.json")

    with open(MODEL_DIR / "label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)

    with open(MODEL_DIR / "train_cols.pkl", "rb") as f:
        train_cols = pickle.load(f)

    return model, label_encoder, train_cols


# FastAPI startup
try:
    _model, _label_encoder, _train_cols = _load_artifacts()
    print("[Model] Loaded successfully.")
except FileNotFoundError:
    _model = _label_encoder = _train_cols = None
    print("[Model] WARNING: Model files not found. Run train_and_save.py first.")


# Predict 
def predict_category(raw_input: dict, top_n: int = 2) -> dict:
    if _model is None:
        raise RuntimeError("Model not loaded. Run train_and_save.py first.")

    # Tạo DataFrame 1 dòng từ input
    df = pd.DataFrame([raw_input])

    # Feature engineering
    df = feature_engineering(df)

    # Build feature matrix (khớp schema lúc train)
    X = build_features(df, fit_columns=_train_cols)

    # Predict
    probs     = _model.predict_proba(X)[0]
    top_idx   = np.argsort(probs)[::-1][:top_n]

    top_categories = [
        {
            "category":   _label_encoder.inverse_transform([idx])[0],
            "confidence": round(float(probs[idx]), 4),
        }
        for idx in top_idx
    ]

    return {
        "predicted":      top_categories[0]["category"],
        "confidence":     top_categories[0]["confidence"],
        "top_categories": top_categories,
    }
