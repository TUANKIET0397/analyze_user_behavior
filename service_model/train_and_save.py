"""
train_and_save.py
-----------------
Chạy file này 1 lần để train model và lưu vào thư mục models/.
Sau đó FastAPI sẽ load model từ đó mà không cần train lại.

Usage:
    python train_and_save.py
"""

import pickle
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight, compute_sample_weight
from sklearn.metrics import accuracy_score, classification_report

# Config
DATA_PATH  = "shopping_trends_updated.csv"
MODEL_DIR  = "models"

CATEGORICAL_COLS = [
    "Subscription Status",
    "Age_Group",
    "Spending_Level",
    "Season_Spending_Level",
    "Gender_Price_Interaction",
    "Gender_Season",
]

NUMERICAL_COLS = [
    "Value_Per_Star",
    "Frequency_Spend_Ratio",
    "Total_Customer_Value",
    "Age",
    "Purchase Amount (USD)",
    "Review Rating",
    "Previous Purchases",
    "Frequency_Score",
    "Loyalty_Score",
]

# Feature Engineering
def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Nhóm tuổi
    def age_group(age):
        if age < 30:   return "Young"
        elif age < 45: return "Middle"
        elif age < 60: return "Adult"
        else:          return "Old"

    df["Age_Group"] = df["Age"].apply(age_group)

    # Spending level
    def spending_level(x):
        if x < 30:   return "Low"
        elif x < 60: return "Medium"
        else:        return "High"

    df["Spending_Level"] = df["Purchase Amount (USD)"].apply(spending_level)

    # Tần suất mua
    df["Frequency of Purchases"] = df["Frequency of Purchases"].str.strip().str.lower()
    freq_map = {
        "weekly": 4, "bi-weekly": 2, "fortnightly": 2,
        "monthly": 1, "every 3 months": 0.33,
        "quarterly": 0.33, "annually": 0.08,
    }
    df["Frequency_Score"] = df["Frequency of Purchases"].map(freq_map)

    # Derived features
    df["Loyalty_Score"]            = (df["Previous Purchases"] + df["Frequency_Score"]).round(2)
    df["Season_Spending_Level"]    = df["Season"] + "_" + df["Spending_Level"]
    df["Gender_Price_Interaction"] = df["Gender"] + "_" + df["Spending_Level"]
    df["Value_Per_Star"]           = df["Purchase Amount (USD)"] / (df["Review Rating"] + 1)
    df["Frequency_Spend_Ratio"]    = df["Frequency_Score"] / (df["Purchase Amount (USD)"] + 1)
    df["Total_Customer_Value"]     = df["Previous Purchases"] * df["Purchase Amount (USD)"]
    df["Gender_Season"]            = df["Gender"] + "_" + df["Season"]

    # Drop không cần nữa
    df = df.drop(
        columns=["Discount Applied", "Promo Code Used",
                 "Frequency of Purchases", "Season", "Gender"],
        errors="ignore",
    )
    return df


def build_features(df: pd.DataFrame, fit_columns=None) -> pd.DataFrame:
    X_cat = pd.get_dummies(df[CATEGORICAL_COLS], columns=CATEGORICAL_COLS)
    X = pd.concat([X_cat, df[NUMERICAL_COLS]], axis=1)
    bool_cols = X.select_dtypes(include="bool").columns
    X[bool_cols] = X[bool_cols].astype(int)
    X = X.fillna(0)
    if fit_columns is not None:
        X = X.reindex(columns=fit_columns, fill_value=0)
    return X


# Load & preprocess data
print("Loading data...")
df = pd.read_csv(DATA_PATH)

df = df.drop(
    columns=["Customer ID", "Size", "Color", "Item Purchased",
             "Location", "Payment Method", "Shipping Type", "Unnamed: 18"],
    errors="ignore",
)

df["Category"] = df["Category"].replace("Outerwear", "Clothing")
df = feature_engineering(df)

# Encode target
le_target = LabelEncoder()
y = le_target.fit_transform(df["Category"])

X = build_features(df)
train_cols = X.columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Class weights
classes = np.unique(y_train)
class_weights = compute_class_weight(
    class_weight="balanced", classes=classes, y=y_train
)
cw = dict(zip(classes, class_weights))
sample_weights = compute_sample_weight(class_weight=cw, y=y_train)

# Train
print("Training XGBoost...")
model = xgb.XGBClassifier(
    n_estimators=5000,
    learning_rate=0.03,
    max_depth=9,
    subsample=0.6,
    colsample_bytree=0.9,
    reg_lambda=0.5,
    objective="multi:softprob",
    eval_metric="mlogloss",
    random_state=42,
    early_stopping_rounds=50,
)

model.fit(
    X_train, y_train,
    sample_weight=sample_weights,
    eval_set=[(X_test, y_test)],
    verbose=50,
)

# Evaluate
y_pred = model.predict(X_test)
print("\n=== Evaluation ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=le_target.classes_))

# Save
import os
os.makedirs(MODEL_DIR, exist_ok=True)

model.save_model(f"{MODEL_DIR}/xgb_category.json")

with open(f"{MODEL_DIR}/label_encoder.pkl", "wb") as f:
    pickle.dump(le_target, f)

with open(f"{MODEL_DIR}/train_cols.pkl", "wb") as f:
    pickle.dump(train_cols, f)

print(f"\nModels saved to ./{MODEL_DIR}/")
print("  xgb_category.json")
print("  label_encoder.pkl")
print("  train_cols.pkl")
