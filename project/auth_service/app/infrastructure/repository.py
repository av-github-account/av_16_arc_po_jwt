from app.infrastructure.db import get_conn
from app.domain.models import User

def get_user_by_email(email: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, email, password FROM users WHERE email = %s", (email,))
    row = cur.fetchone()
    conn.close()
    return User(*row) if row else None

def create_user(email: str, hashed_password: str):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_password))
        conn.commit()
        return True
    except:
        conn.rollback()
        return False
    finally:
        conn.close()
