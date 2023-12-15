import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

def _getenv(key: str):
    env = os.getenv(key)
    if env is None:
        return env
    
    if env.strip() == "":
        os.environ.pop(key)
        return None
    
    return env


def _getenv_or_default(key: str, default: str):
    env = _getenv(key)
    if env is None:
        return default
    return env

class Env:
    # アプリケーション関連
    APP_ENV = _getenv_or_default("APP_ENV", "local")
    APP_NAME = _getenv_or_default("APP_NAME", "demo-app")
    LOG_LEVEL = _getenv("LOG_LEVEL")
    APP_URL = _getenv("APP_URL")
    NEXT_APP_URL = _getenv("NEXT_APP_URL")
    ADMIN_APP_URL = os.getenv("ADMIN_APP_URL")
    API_URL = _getenv("API_URL")
    
    # データベース関連
    DATABASE_HOST = _getenv("DATABASE_HOST")
    DATABASE_PORT = _getenv("DATABASE_PORT")
    DATABASE_NAME = _getenv("DATABASE_NAME")
    DATABASE_USER = _getenv("DATABASE_USER")
    DATABASE_PASSWORD = _getenv("DATABASE_PASSWORD")