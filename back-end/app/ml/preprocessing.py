# Tien xu ly va feature engineering cho pipeline ML.
# MODIFIED: handle missing review rating and boolean fields
# REASON: van ho tro gia tri mac dinh neu client thieu review_rating
import pandas as pd
import numpy as np
from typing import Optional


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

FREQ_MAP = {
    "weekly": 4,
    "bi-weekly": 2,
    "fortnightly": 2,
    "monthly": 1,
    "every 3 months": 0.33,
    "quarterly": 0.33,
    "annually": 0.08,
}


def _age_group(age: float) -> str:
    if age < 30:   return "Young"
    elif age < 45: return "Middle"
    elif age < 60: return "Adult"
    else:          return "Old"


def _spending_level(x: float) -> str:
    if x < 30:   return "Low"
    elif x < 60: return "Medium"
    else:        return "High"


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nhận raw DataFrame,
    trả về DataFrame đã có đầy đủ engineered features.
    """
    df = df.copy()

    if "Review Rating" not in df.columns:
        df["Review Rating"] = 3.0
    df["Review Rating"] = df["Review Rating"].fillna(3.0)

    if df["Subscription Status"].dtype == "bool":
        df["Subscription Status"] = df["Subscription Status"].map(
            lambda value: "Yes" if value else "No"
        )

    if "Discount Applied" in df.columns and df["Discount Applied"].dtype == "bool":
        df["Discount Applied"] = df["Discount Applied"].map(
            lambda value: "Yes" if value else "No"
        )

    df["Age_Group"] = df["Age"].apply(_age_group)
    df["Spending_Level"] = df["Purchase Amount (USD)"].apply(_spending_level)

    # Frequency score
    freq_raw = df["Frequency of Purchases"].str.strip().str.lower()
    df["Frequency_Score"] = freq_raw.map(FREQ_MAP)

    # Derived features
    df["Loyalty_Score"]            = (df["Previous Purchases"] + df["Frequency_Score"]).round(2)
    df["Season_Spending_Level"]    = df["Season"] + "_" + df["Spending_Level"]
    df["Gender_Price_Interaction"] = df["Gender"] + "_" + df["Spending_Level"]
    df["Value_Per_Star"]           = df["Purchase Amount (USD)"] / (df["Review Rating"] + 1)
    df["Frequency_Spend_Ratio"]    = df["Frequency_Score"] / (df["Purchase Amount (USD)"] + 1)
    df["Total_Customer_Value"]     = df["Previous Purchases"] * df["Purchase Amount (USD)"]
    df["Gender_Season"]            = df["Gender"] + "_" + df["Season"]

    # Drop cols đã dùng xong
    df = df.drop(
        columns=["Discount Applied", "Promo Code Used",
                 "Frequency of Purchases", "Season", "Gender"],
        errors="ignore",
    )
    return df


def build_features(
    df: pd.DataFrame,
    fit_columns: Optional[list] = None,
) -> pd.DataFrame:
    """
    One-hot encode categorical cols + concat numerical cols.
    fit_columns: nếu truyền vào sẽ reindex để khớp schema lúc train.
    """
    X_cat = pd.get_dummies(df[CATEGORICAL_COLS], columns=CATEGORICAL_COLS)
    X = pd.concat([X_cat, df[NUMERICAL_COLS]], axis=1)

    bool_cols = X.select_dtypes(include="bool").columns
    X[bool_cols] = X[bool_cols].astype(int)
    X = X.fillna(0)

    if fit_columns is not None:
        X = X.reindex(columns=fit_columns, fill_value=0)

    return X
