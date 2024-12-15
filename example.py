import httpx


response = httpx.get(
    url="http://localhost:80",
    timeout=30,
)
print(response.status_code)
print(response.text)


response = httpx.post(
    url="http://localhost:80/products",
    json={
        "name": "MacBook Pro",
        "description": "A useless laptop but from Apple",
        "price": 1999.00,
        "stock": 10,
    },
    headers={
        "Authorization": "Bearer 1234567890"
    },
    timeout=30,
)
print(response.status_code)
print(response.text)


response = httpx.post(
    url="http://localhost:80/products",
    json={
        "name": "MacBook Air",
        "description": "A more useless laptop but from Apple",
        "price": 999.00,
        "stock": 50,
    },
    headers={
        "Authorization": "Bearer 1234567890"
    },
    timeout=30,
)
print(response.status_code)
print(response.text)


response = httpx.get(
    url="http://localhost:80/products",
    headers={
        "Authorization": "Bearer 1234567890"
    },
    timeout=30,
)
print(response.status_code)
print(response.text)


response = httpx.post(
    url="http://localhost:80/products",
    json={
        "name": "MacBook Air",
        "description": "A more useless laptop but from Apple",
        "price": 999.00,
        "stock": 50,
    },
    headers={
        "Authorization": "Bearer 1234567890"
    },
    timeout=30,
)
print(response.status_code)
print(response.text)


response = httpx.post(
    url="http://localhost:80/orders",
    json={
        "products": [
            { "product_id": 1, "quantity": 5 },
            { "product_id": 2, "quantity": 5 },
        ]
    },
    headers={
        "Authorization": "Bearer 1234567890"
    },
    timeout=30,
)
print(response.status_code)
print(response.text)


response = httpx.get(
    url="http://localhost:80/products",
    headers={
        "Authorization": "Bearer 1234567890"
    },
    timeout=30,
)
print(response.status_code)
print(response.text)
