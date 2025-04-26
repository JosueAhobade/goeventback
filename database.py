from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Exemple d'URL PostgreSQL — à adapter selon ta config
DATABASE_URL = "postgresql://postgres:root@localhost:5432/eventdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
