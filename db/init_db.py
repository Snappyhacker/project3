from db.database import Base, engine
from models.inventory import Inventory
from models.supplier import Supplier
from models.order import Order

def init_db():
    """Create all tables in the database"""
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()
