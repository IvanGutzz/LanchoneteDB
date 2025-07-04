# main.py

from database.connection import engine, Base
from models.pedido import Pedido

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")
