import os
import dotenv

dotenv.load_dotenv()


class Config:
    DEBUG = os.getenv('DEBUG', "false").lower() == "true"
    APP_HOST = os.getenv('APP_HOST', 'http://localhost:5000')
    API_SECRET = os.getenv('API_SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///mydatabase.db').replace("postgres://",
                                                                                           "postgresql://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BLUESKY_ENABLED = os.getenv('BLUESKY_ENABLED', "false").lower() == "true"
    BLUESKY_HANDLE = os.getenv('BLUESKY_HANDLE')
    BLUESKY_APP_PASSWORD = os.getenv('BLUESKY_APP_PASSWORD')
    SEARCH_POSTS_PER_PAGE = int(os.getenv('SEARCH_POSTS_PER_PAGE', 10))
