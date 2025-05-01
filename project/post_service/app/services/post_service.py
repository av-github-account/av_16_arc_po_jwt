from datetime import datetime
from app.core.security import decode_token
from app.infrastructure.repository import insert_post

def save_post(message: str, token: str):
    payload = decode_token(token)
    if payload == "expired":
        return "expired"
    if payload is None:
        return None
    user_id = payload.get("user_id")
    if not user_id:
        return None
    return insert_post(user_id, message, datetime.utcnow())
