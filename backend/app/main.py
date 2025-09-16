# from fastapi import FastAPI

# app = FastAPI(title="nextGen Backend")

# @app.get("/")
# def root():
#     return {"message": "nextGen Learning Backend is running 🚀"}

from fastapi import FastAPI
from app.routes import user

app = FastAPI()
app.include_router(user.router)
