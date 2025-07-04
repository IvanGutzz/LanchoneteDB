# menu.py

from database.connection import SessionLocal, Base, engine
from database.crud import (
    criar_pedido,
    listar_pedidos,
    buscar_pedido_por_id,
    atualizar_pedido,
    deletar_pedido,
    criar_pedidos_em_lote
)

# Criar tabelas (caso não existam)
Base.metadata.create_all(bind=engine)

def main():
    db = SessionLocal()

    while True:
        print("\n--- MENU LANCHONETE ---")
        print("1 - Criar pedido")
        print("2 - Listar pedidos")
        print("3 - Buscar pedido por ID")
        print("4 - Atualizar pedido")
        print("5 - Deletar pedido")
        print("6 - Criar vários pedidos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cliente = input("Nome do cliente: ")
            item = input("Item: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço unitário: "))
            pedido = criar_pedido(db, cliente, item, quantidade, preco)
            print("✅ Pedido criado:", pedido)

        elif opcao == "2":
            pedidos = listar_pedidos(db)
            for p in pedidos:
                print(p)

        elif opcao == "3":
            pid = int(input("ID do pedido: "))
            pedido = buscar_pedido_por_id(db, pid)
            print(pedido if pedido else "❌ Pedido não encontrado.")

        elif opcao == "4":
            pid = int(input("ID do pedido: "))
            cliente = input("Novo nome do cliente: ")
            item = input("Novo item: ")
            quantidade = int(input("Nova quantidade: "))
            preco = float(input("Novo preço unitário: "))
            pedido = atualizar_pedido(db, pid, cliente, item, quantidade, preco)
            print("✅ Pedido atualizado:", pedido if pedido else "❌ Pedido não encontrado.")

        elif opcao == "5":
            pid = int(input("ID do pedido: "))
            pedido = deletar_pedido(db, pid)
            print("✅ Pedido deletado:", pedido if pedido else "❌ Pedido não encontrado.")

        elif opcao == "6":
            qtd = int(input("Quantos pedidos deseja cadastrar? "))
            pedidos_data = []

            for i in range(qtd):
                print(f"\nPedido {i + 1}:")
                cliente = input("Nome do cliente: ")
                item = input("Item: ")
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço unitário: "))

                pedidos_data.append({
                    "cliente": cliente,
                    "item": item,
                    "quantidade": quantidade,
                    "preco_unitario": preco
                })

            pedidos_criados = criar_pedidos_em_lote(db, pedidos_data)
            print(f"✅ {len(pedidos_criados)} pedidos cadastrados com sucesso!")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("⚠️ Opção inválida. Tente novamente.")

    db.close()

if __name__ == "__main__":
    main()
