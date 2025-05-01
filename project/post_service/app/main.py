from fastapi import FastAPI
from app.api.v1 import post

app = FastAPI()
app.include_router(post.router, prefix="/api/v1")
