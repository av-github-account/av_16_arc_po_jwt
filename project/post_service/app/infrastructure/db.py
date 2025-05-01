import psycopg2
from app.core.config import DB_URL

def get_conn():
    return psycopg2.connect(DB_URL)
