from fastapi import APIRouter, Header, HTTPException, Request
from pydantic import BaseModel
from app.services.post_service import save_post

router = APIRouter()

class PostMessage(BaseModel):
    message: str

@router.post("/post", status_code=201)
def post_message(data: PostMessage, authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400)
    token = authorization.split()[1]
    result = save_post(data.message, token)
    if result == "expired":
        raise HTTPException(status_code=401)
    elif not result:
        raise HTTPException(status_code=400)
    return
