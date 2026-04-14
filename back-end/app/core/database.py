# Khoi tao DB engine, session va dependency get_db cho FastAPI.
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import BASE_DIR, DB_FILENAME


DB_PATH = BASE_DIR / DB_FILENAME
DATABASE_URL = f"sqlite:///{DB_PATH.as_posix()}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# import sqlite3
# import os
# from pathlib import Path

# def init_database():
#     """Khởi tạo database và các bảng"""
    
#     # Đường dẫn đến database file
#     db_path = Path(__file__).parent / 'shopping_trends.db'
    
#     # Kết nối database
#     conn = sqlite3.connect(str(db_path))
#     cursor = conn.cursor()
    
#     # Đọc schema từ file
#     schema_file = Path(__file__).parent / 'schema.sql'
#     with open(schema_file, 'r', encoding='utf-8') as f:
#         schema = f.read()
    
#     # Thực thi schema
#     cursor.executescript(schema)
#     conn.commit()
    
#     print(f"Database khởi tạo thành công: {db_path}")
#     print("Tài khoản demo: username=demo, password=demo123")
#     print("Các bảng được tạo: users, user_data, predictions")
    
#     conn.close()

# if __name__ == "__main__":
#     init_database()

# -- Users table - lưu thông tin tài khoản
# CREATE TABLE IF NOT EXISTS users (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   username TEXT UNIQUE NOT NULL,
#   password TEXT NOT NULL,
#   name TEXT NOT NULL,
#   created_at DATETIME DEFAULT CURRENT_TIMESTAMP
# );

# -- User data table - lưu dữ liệu từ trang Home (match CSV format)
# CREATE TABLE IF NOT EXISTS user_data (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   user_id INTEGER NOT NULL,
#   age INTEGER,
#   gender TEXT,
#   purchase_amount_usd REAL,
#   previous_purchases INTEGER,
#   season TEXT,
#   subscription_status INTEGER,
#   frequency_of_purchases TEXT,
#   discount_applied INTEGER,
#   review_rating REAL,
#   promo_code_used INTEGER,
#   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#   FOREIGN KEY(user_id) REFERENCES users(id)
# );

# -- Predictions table - lưu kết quả dự đoán từ model
# CREATE TABLE IF NOT EXISTS predictions (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   user_id INTEGER NOT NULL,
#   predicted_category TEXT,
#   prediction_result TEXT,
#   analysis TEXT,
#   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#   FOREIGN KEY(user_id) REFERENCES users(id)
# );