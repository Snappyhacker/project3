from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL - will create a SQLite database in the project root
DATABASE_URL = "sqlite:///inventory.db"

# Set up the engine and session
engine = create_engine(DATABASE_URL, echo=True)  # Added `echo=True` for debugging
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Get database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
