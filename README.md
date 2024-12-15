# RESTful API for E-Commerce Platform

## Project Structure
```
|   .env                         # Environment variables
|   docker-compose.yaml          # Docker Compose file
|   Dockerfile                   # Docker file for api service
|   example.py                   # Example API calls
|   README.md
|   requirements.txt             # Python dependencies
|   
+---app
|   +---api
|   |   |   endpoints.py         # API endpoints
|   |   |   __init__.py          # API server
|   |   |   
|   |           
|   +---db
|   |   |   __init__.py          # Database connection
|   |   |   
|   |   +---models               # SQLAlchemy models
|   |   |   |   order.py         # Order model
|   |   |   |   order_product.py # Order-Product model i.e. with quantity
|   |   |   |   product.py       # Product model
|   |   |   |   __init__.py
|   |   |   |   
|   |   |           
|   |           
|   +---schemas                  # Pydantic schemas
|   |   |   order.py             # Order schemas
|   |   |   product.py           # Product schemas
|   |   |   __init__.py
|   |   |   
|   |           
|   +---services                 # Services
|   |   |   __init__.py          # Core logic for creating products, orders
|   |   |   
|   |           
|   \---utils                    # Utility functions
|       |   auth_utils.py        # Auth utils
|       |   exceptions.py        # Exception classes
|       |   __init__.py
|       |   
|               
+---config                       # Config manager for .env file
|   |   __init__.py
|   |   
|           
\---tests                        # Tests
    |   test_endpoints.py        # Test cases for API endpoints
    |   __init__.py
    |   
```


## Usage / Manual Tests

1. `docker compose down --remove-orphans --volumes && docker compose up --build api`
2. Wait till the app is up and running^
3. `python example.py`

Above `example.py` contains API calls cases ~ for creating products, getting all products, creating orders


## Automated Tests
1. `docker compose down --remove-orphans --volumes && docker compose up --build api_tests`


## Docs

`/docs`
![api_docs_testing](/tests/api_docs_testing.png)
