import os
import dotenv

dotenv.load_dotenv()


class Config:
    DEBUG = os.getenv('DEBUG', False)
    API_SECRET = os.getenv('API_SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///mydatabase.db').replace("postgres://", "postgresql://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
