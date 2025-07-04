# models/pedido.py

from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database.connection import Base

class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String(100), nullable=False)
    item = Column(String(100), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)
    data_pedido = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Pedido(id={self.id}, cliente='{self.cliente}', item='{self.item}')>"
