-- Users table - lưu thông tin tài khoản
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  name TEXT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- User data table - lưu dữ liệu từ trang Home (match CSV format)
CREATE TABLE IF NOT EXISTS user_data (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  age INTEGER,
  gender TEXT,
  purchase_amount_usd REAL,
  previous_purchases INTEGER,
  season TEXT,
  subscription_status INTEGER,
  frequency_of_purchases TEXT,
  discount_applied INTEGER,
  review_rating REAL,
  promo_code_used INTEGER,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(user_id) REFERENCES users(id)
);

-- Predictions table - lưu kết quả dự đoán từ model
CREATE TABLE IF NOT EXISTS predictions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  predicted_category TEXT,
  prediction_result TEXT,
  analysis TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(user_id) REFERENCES users(id)
);

-- Insert demo user account
INSERT OR IGNORE INTO users (id, username, password, name) 
VALUES (1, 'demo', 'demo123', 'Baozeus');

-- Insert demo user data
INSERT OR IGNORE INTO user_data (user_id, age, gender, purchase_amount_usd, previous_purchases, season, subscription_status, frequency_of_purchases, discount_applied, review_rating, promo_code_used)
VALUES (1, 32, 'Male', 53, 14, 'Spring', 1, 'Weekly', 1, 3.1, 1);
