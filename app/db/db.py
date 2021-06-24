from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

import os
from app.db.models import Base

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv('DB_URI')

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
)

Base.metadata.create_all(engine)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
