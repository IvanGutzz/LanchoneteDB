# database/crud.py

from sqlalchemy.orm import Session
from models.pedido import Pedido

def criar_pedido(db: Session, cliente: str, item: str, quantidade: int, preco_unitario: float):
    pedido = Pedido(
        cliente=cliente,
        item=item,
        quantidade=quantidade,
        preco_unitario=preco_unitario
    )
    db.add(pedido)
    db.commit()
    db.refresh(pedido)
    return pedido

def listar_pedidos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Pedido).offset(skip).limit(limit).all()

def buscar_pedido_por_id(db: Session, pedido_id: int):
    return db.query(Pedido).filter(Pedido.id == pedido_id).first()

def atualizar_pedido(db: Session, pedido_id: int, cliente: str, item: str, quantidade: int, preco_unitario: float):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if pedido:
        pedido.cliente = cliente
        pedido.item = item
        pedido.quantidade = quantidade
        pedido.preco_unitario = preco_unitario
        db.commit()
        db.refresh(pedido)
    return pedido

def deletar_pedido(db: Session, pedido_id: int):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if pedido:
        db.delete(pedido)
        db.commit()
    return pedido

def criar_pedidos_em_lote(db: Session, pedidos_data: list[dict]):
    pedidos = []
    for data in pedidos_data:
        pedido = Pedido(
            cliente=data["cliente"],
            item=data["item"],
            quantidade=data["quantidade"],
            preco_unitario=data["preco_unitario"]
        )
        db.add(pedido)
        pedidos.append(pedido)

    db.commit()
    for pedido in pedidos:
        db.refresh(pedido)
    return pedidos
