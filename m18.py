class ProdutoInexistenteError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass

produtos = {
    "camisola": 50,
    "calças": 100,
    "sapatos": 250,
    "meias": 10,
    "bone": 30,
}

carrinho = {}
saldo = 500         

def mostrar_produtos():
    print("\nProdutos disponíveis:")
    for nome, preco in produtos.items():
        print(f"{nome} - € {preco}")

def adicionar_produto():
    try:
        nome = input("Produto: ").lower()
        if nome not in produtos:
            raise ProdutoInexistenteError("Esse produto não existe.")
        qtd = int(input("Quantidade: "))
        if qtd <= 0:
            raise ValueError("A Quantidade deve ser positiva.")
        carrinho[nome] = carrinho.get(nome, 0) + qtd
        print(f"{qtd}x {nome} adicionado(s) ao carrinho.")
    except ProdutoInexistenteError as e:
        print("Erro:", e)
    except ValueError:
        print("Erro: informe uma quantidade válida (número inteiro positivo).")

def ver_carrinho():
    print("\nSeu carrinho:")
    total = 0
    for nome, qtd in carrinho.items():
        preco = produtos[nome] * qtd
        total += preco
        print(f"{qtd}x {nome} = € {preco}")
    print(f"Total: € {total}")
    return total

def pagar():
    try:
        if not carrinho:
            print("Carrinho vazio.")
            return
        total = ver_carrinho()
        global saldo
        if total > saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        saldo -= total
        carrinho.clear()
        print(f"Pagamento aprovado! Novo saldo: € {saldo}")
    except SaldoInsuficienteError as e:
        print("Erro:", e)

def menu():
    while True:
        print("\n1 - Ver produtos\n2 - Adicionar ao carrinho\n3 - Ver carrinho\n4 - Pagar\n5 - Sair")
        op = input("Escolha: ")
        if op == "1":
            mostrar_produtos()
        elif op == "2":
            adicionar_produto()
        elif op == "3":
            ver_carrinho()
        elif op == "4":
            pagar()
        elif op == "5":
            print("Até a próxima!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    print(" Bem-vindo à Loja Ruben Pinto")
    menu()
