# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings  # absolute import is safer on Render

SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_url  # already normalized to e.g. postgresql+psycopg://...

# Extra engine settings help avoid stale connections on Render
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,               # ping before using a pooled connection
    pool_recycle=300,                 # recycle connections every 5 minutes
    connect_args=(
        {"check_same_thread": False}
        if SQLALCHEMY_DATABASE_URL.startswith("sqlite")
        else {}
    ),
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
