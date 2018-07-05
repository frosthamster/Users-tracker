import os
import secrets
from pathlib import Path


class Config:
    SECRET_KEY = os.environ.get('APP_SECRET_KEY') or secrets.token_hex(32)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{Path().joinpath("database.db").absolute()}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USERS_PER_PAGE = 15
