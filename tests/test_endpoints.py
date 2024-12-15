import pytest
from fastapi.testclient import TestClient
from app.api import api
from app.db import init_db, SessionLocal
from app.db.models import Product


client = TestClient(api)


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    init_db()


@pytest.fixture
def db_session():
    db = SessionLocal()
    yield db
    db.close()


def test_create_unique_product(db_session):
    headers = {"Authorization": "Bearer 1234567890"}

    product1 = {
        "name": "Laptop",
        "description": "Gaming laptop",
        "price": 1500.0,
        "stock": 10,
    }
    response = client.post("/products", json=product1, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == product1["name"]

    product2 = {
        "name": "Laptop",
        "description": "Gaming laptop",
        "price": 1500.0,
        "stock": 5,
    }
    response = client.post("/products", json=product2, headers=headers)
    assert response.status_code == 400  # Unique constraint violation
    assert (
        "Product with the same name, description and price already exists."
        in response.json()["detail"]
    )


def test_create_and_check_products(db_session):
    headers = {"Authorization": "Bearer 1234567890"}

    product1 = {
        "name": "Laptop New",
        "description": "Gaming laptop",
        "price": 150.0,
        "stock": 10,
    }
    response = client.post("/products", json=product1, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == product1["name"]

    response = client.get("/products", headers=headers)
    assert response.status_code == 200
    all_products = response.json()
    assert any(
        (
            product1["name"] == p["name"]
            and product1["description"] == p["description"]
            and product1["price"] == p["price"]
            for p in all_products
        )
    )


def test_create_order_sufficient_stock(db_session):
    headers = {"Authorization": "Bearer 1234567890"}

    # Create a product with limited stock
    product_data = {
        "name": "Laptop",
        "description": "High-performance laptop",
        "price": 200.0,
        "stock": 10,  # Limited stock
    }
    response = client.post("/products", json=product_data, headers=headers)
    assert response.status_code == 200  # Ensure product is created

    created_product = response.json()
    product_id = created_product["id"]

    # Attempt to place an order without quantity exceeding stock
    order_data = {"products": [{"product_id": product_id, "quantity": 5}]}
    response = client.post("/orders", json=order_data, headers=headers)
    assert response.status_code == 200
    print(response.json())
    assert response.json()["products"][0]["product_id"] == product_id


def test_create_order_insufficient_stock(db_session):
    headers = {"Authorization": "Bearer 1234567890"}

    # Create a product with limited stock
    product_data = {
        "name": "Laptop",
        "description": "High-performance laptop",
        "price": 100.0,
        "stock": 10,  # Limited stock
    }
    response = client.post("/products", json=product_data, headers=headers)
    assert response.status_code == 200  # Ensure product is created

    created_product = response.json()
    product_id = created_product["id"]

    # Attempt to place an order with quantity exceeding stock
    order_data = {
        "products": [{"product_id": product_id, "quantity": 20}]  # Exceeds stock
    }
    response = client.post("/orders", json=order_data, headers=headers)
    assert response.status_code == 400  # Insufficient stock error
    assert "Insufficient stock" in response.json()["detail"]
