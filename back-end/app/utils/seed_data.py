# Seed data cho bang category_products neu chua co du lieu.
from sqlalchemy.orm import Session

from app.models.category_product import CategoryProduct

def seed_category_products(db: Session) -> None:
    existing = db.query(CategoryProduct).first()
    if existing is not None:
        return

    items = [
        {
            "category": "Clothing",
            "product_name": "Blouse",
            "image_path": "static/products/Blouse.jpg",
            "price": 60.88,
        },
        {
            "category": "Clothing",
            "product_name": "Sweater",
            "image_path": "static/products/Sweater.jpg",
            "price": 57.7,
        },
        {
            "category": "Clothing",
            "product_name": "Jeans",
            "image_path": "static/products/Jeans.jpg",
            "price": 60.87,
        },
        {
            "category": "Clothing",
            "product_name": "Shirt",
            "image_path": "static/products/Shirt.jpg",
            "price": 61.14,
        },
        {
            "category": "Clothing",
            "product_name": "Shorts",
            "image_path": "static/products/Shorts.jpg",
            "price": 60.08,
        },
        {
            "category": "Clothing",
            "product_name": "Coat",
            "image_path": "static/products/Coat.jpg",
            "price": 57.61,
        },
        {
            "category": "Clothing",
            "product_name": "Dress",
            "image_path": "static/products/Dress.jpg",
            "price": 62.17,
        },
        {
            "category": "Clothing",
            "product_name": "Skirt",
            "image_path": "static/products/Skirt.jpg",
            "price": 59.51,
        },
        {
            "category": "Clothing",
            "product_name": "Pants",
            "image_path": "static/products/Pants.jpg",
            "price": 59.01,
        },
        {
            "category": "Clothing",
            "product_name": "Jacket",
            "image_path": "static/products/Jacket.jpg",
            "price": 56.74,
        },
        {
            "category": "Clothing",
            "product_name": "Hoodie",
            "image_path": "static/products/Hoodie.jpg",
            "price": 58.06,
        },
        {
            "category": "Clothing",
            "product_name": "T-shirt",
            "image_path": "static/products/T-shirt.jpg",
            "price": 62.91,
        },
        {
            "category": "Clothing",
            "product_name": "Socks",
            "image_path": "static/products/Socks.jpg",
            "price": 58.19,
        },
        {
            "category": "Footwear",
            "product_name": "Sandals",
            "image_path": "static/products/Sandals.jpg",
            "price": 57.5,
        },
        {
            "category": "Footwear",
            "product_name": "Sneakers",
            "image_path": "static/products/Sneakers.jpg",
            "price": 58.55,
        },
        {
            "category": "Footwear",
            "product_name": "Shoes",
            "image_path": "static/products/Shoes.jpg",
            "price": 61.6,
        },
        {
            "category": "Footwear",
            "product_name": "Boots",
            "image_path": "static/products/Boots.jpg",
            "price": 62.62,
        },
        {
            "category": "Accessories",
            "product_name": "Handbag",
            "image_path": "static/products/Handbag.jpg",
            "price": 57.89,
        },
        {
            "category": "Accessories",
            "product_name": "Sunglasses",
            "image_path": "static/products/Sunglasses.jpg",
            "price": 59.93,
        },
        {
            "category": "Accessories",
            "product_name": "Jewelry",
            "image_path": "static/products/Jewelry.jpg",
            "price": 58.54,
        },
        {
            "category": "Accessories",
            "product_name": "Scarf",
            "image_path": "static/products/Scarfs.jpg",
            "price": 60.9,
        },
        {
            "category": "Accessories",
            "product_name": "Hat",
            "image_path": "static/products/Hat.jpg",
            "price": 60.88,
        },
        {
            "category": "Accessories",
            "product_name": "Backpack",
            "image_path": "static/products/Backpack.jpg",
            "price": 60.39,
        },
        {
            "category": "Accessories",
            "product_name": "Belt",
            "image_path": "static/products/Belt.jpg",
            "price": 59.84,
        },
        {
            "category": "Accessories",
            "product_name": "Gloves",
            "image_path": "static/products/Gloves.jpg",
            "price": 60.55,
        },
    ]

    db.add_all([CategoryProduct(**item) for item in items])
    db.commit()

