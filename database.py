from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
# test
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/lecture_notes")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
