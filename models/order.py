from sqlalchemy import Column, Integer, ForeignKey, String
from db.database import Base
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('inventory.id'))
    supplier_id = Column(Integer, ForeignKey('supplier.id'))
    quantity = Column(Integer, nullable=False)
    order_date = Column(String)

    product = relationship("Inventory")
    supplier = relationship("Supplier")
