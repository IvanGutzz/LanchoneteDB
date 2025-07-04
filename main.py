# main.py

from database.connection import SessionLocal, Base, engine
from database.crud import (
    criar_pedido,
    listar_pedidos,
    buscar_pedido_por_id,
    atualizar_pedido,
    deletar_pedido
)
from models.pedido import Pedido

# Criar as tabelas no banco (se ainda não existem)
Base.metadata.create_all(bind=engine)

# Criar uma sessão com o banco de dados
db = SessionLocal()

# ----------- TESTES -----------

# Criar um novo pedido
novo_pedido = criar_pedido(db, "Carlos", "X-Burguer", 2, 18.90)
print("✅ Pedido criado:", novo_pedido)

# Listar todos os pedidos
pedidos = listar_pedidos(db)
print("📋 Lista de pedidos:")
for p in pedidos:
    print(p)

# Buscar um pedido pelo ID
pedido_id = novo_pedido.id
pedido_encontrado = buscar_pedido_por_id(db, pedido_id)
print(f"🔎 Pedido encontrado (ID {pedido_id}):", pedido_encontrado)

# Atualizar o pedido
pedido_atualizado = atualizar_pedido(db, pedido_id, "Carlos", "X-Salada", 3, 20.50)
print(f"📝 Pedido atualizado:", pedido_atualizado)

# Deletar o pedido
pedido_deletado = deletar_pedido(db, pedido_id)
print(f"❌ Pedido deletado:", pedido_deletado)

# Listar novamente para confirmar deleção
print("📋 Lista final de pedidos:")
for p in listar_pedidos(db):
    print(p)

# Fechar a sessão
db.close()
