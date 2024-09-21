from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    stock_level = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    supplier_id = Column(Integer, ForeignKey('supplier.id'), nullable=False)

    supplier = relationship("Supplier", back_populates="products")
