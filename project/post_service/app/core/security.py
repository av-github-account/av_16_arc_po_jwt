from jose import JWTError, jwt, ExpiredSignatureError
from app.core.config import SECRET_KEY, ALGORITHM

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        return "expired"
    except JWTError:
        return None
