from datetime import timedelta
from app.infrastructure.repository import create_user, get_user_by_email
from app.core.security import hash_password, verify_password, create_token
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES

def register_user(email: str, password: str) -> bool:
    if len(password) < 6:
        return False
    return create_user(email, hash_password(password))

def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    token = create_token({"user_id": user.id}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return token
