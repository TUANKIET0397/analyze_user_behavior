# Seed data cho bang category_products neu chua co du lieu.
from sqlalchemy.orm import Session

from app.models.category_product import CategoryProduct


def seed_category_products(db: Session) -> None:
    existing = db.query(CategoryProduct).first()
    if existing is not None:
        return

    items = [
        {
            "category": "Footwear",
            "product_name": "Air Runner",
            "image_path": "static/products/footwear_01.jpg",
            "price": 79.0,
        },
        {
            "category": "Footwear",
            "product_name": "Urban Sneakers",
            "image_path": "static/products/footwear_02.jpg",
            "price": 92.5,
        },
        {
            "category": "Footwear",
            "product_name": "Trail Boots",
            "image_path": "static/products/footwear_03.jpg",
            "price": 120.0,
        },
        {
            "category": "Accessories",
            "product_name": "Classic Watch",
            "image_path": "static/products/accessories_01.jpg",
            "price": 140.0,
        },
        {
            "category": "Accessories",
            "product_name": "Leather Belt",
            "image_path": "static/products/accessories_02.jpg",
            "price": 35.0,
        },
        {
            "category": "Accessories",
            "product_name": "Canvas Tote",
            "image_path": "static/products/accessories_03.jpg",
            "price": 28.0,
        },
        {
            "category": "Clothing",
            "product_name": "Minimal Tee",
            "image_path": "static/products/clothing_01.jpg",
            "price": 25.0,
        },
        {
            "category": "Clothing",
            "product_name": "Soft Hoodie",
            "image_path": "static/products/clothing_02.jpg",
            "price": 55.0,
        },
        {
            "category": "Clothing",
            "product_name": "Denim Jacket",
            "image_path": "static/products/clothing_03.jpg",
            "price": 95.0,
        },
    ]

    db.add_all([CategoryProduct(**item) for item in items])
    db.commit()
