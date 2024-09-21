from sqlalchemy import Column, Integer, String
from db.database import Base
from sqlalchemy.orm import relationship

class Supplier(Base):
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

    products = relationship("Inventory", back_populates="supplier")
