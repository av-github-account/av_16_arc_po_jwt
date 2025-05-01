from datetime import datetime
from app.infrastructure.db import get_conn

def insert_post(user_id: int, message: str, time: datetime):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO messages (user_id, time, message) VALUES (%s, %s, %s)",
            (user_id, time, message)
        )
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()
