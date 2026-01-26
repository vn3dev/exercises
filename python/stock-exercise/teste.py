import json

ARQUIVO = "estoque.json"

def carregar_estoque():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def salvar_estoque(estoque):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)

def adicionar(estoque, produto, qtd):
    estoque[produto] = estoque.get(produto, 0) + qtd
    salvar_estoque(estoque)

def baixar(estoque, produto, qtd):
    if produto not in estoque:
        print("Produto não existe.")
        return
    if estoque[produto] < qtd:
        print("Estoque insuficiente.")
        return
    estoque[produto] -= qtd
    if estoque[produto] == 0:
        del estoque[produto]
    salvar_estoque(estoque)

estoque = carregar_estoque()

adicionar(estoque, "Arroz", 2)
baixar(estoque, "Arroz", 1)

print(estoque)