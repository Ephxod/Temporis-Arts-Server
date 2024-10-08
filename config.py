import os
import secrets

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://default_url")
API_KEY = os.getenv("API_KEY", "default_api_key")
APP_ID = os.getenv("APP_ID", "default_app_id")
SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(32))