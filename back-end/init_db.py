import sqlite3
import os
from pathlib import Path

def init_database():
    """Khởi tạo database và các bảng"""
    
    # Đường dẫn đến database file
    db_path = Path(__file__).parent / 'shopping_trends.db'
    
    # Kết nối database
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Đọc schema từ file
    schema_file = Path(__file__).parent / 'schema.sql'
    with open(schema_file, 'r', encoding='utf-8') as f:
        schema = f.read()
    
    # Thực thi schema
    cursor.executescript(schema)
    conn.commit()
    
    print(f"Database khởi tạo thành công: {db_path}")
    print("Tài khoản demo: username=demo, password=demo123")
    print("Các bảng được tạo: users, user_data, predictions")
    
    conn.close()

if __name__ == "__main__":
    init_database()
