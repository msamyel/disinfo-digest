import os
import dotenv

dotenv.load_dotenv()


class Config:
    DEBUG = os.getenv('DEBUG', False)
    API_SECRET = os.getenv('API_SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL', 'sqlite:///mydatabase.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False