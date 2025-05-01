import os

DB_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/app")
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 2
