from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from ..db import init_db
from .endpoints import router as api_router


def get_fastapi():
    _api = FastAPI()

    _api.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _api


# Setup DB
init_db()

api = get_fastapi()


# HTTP errors
@api.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@api.get("/")
def get():
    return {"message": "Hello World!"}


api.include_router(api_router)
