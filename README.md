# Breninho
class ProdutoInexistenteError(Exception):
    pass
class SaldoInsuficienteError(Exception):
    pass
    
Criação de exceções personalizadas.
ProdutoInexistenteError será usada quando o produto não for encontrado na lista.
SaldoInsuficienteError será usada quando o usuário tentar pagar sem saldo suficiente.

python
Copiar
Editar
produtos = {
    "camisola": 50,
    "calças": 100,
    "Sapatos": 250,
    "meias": 10,
    "bone": 30
}

Dicionário de produtos com seus respectivos preços.
As chaves são os nomes dos produtos e os valores são os preços em reais.

python
Copiar
Editar
carrinho = {}
saldo = 500  # Saldo fictício do usuário

carrinho: dicionário que armazenará os produtos e quantidades escolhidas pelo usuário.
saldo: valor inicial que o usuário tem para simular o pagamento das compras.

Função para mostrar os produtos:
python
Copiar
Editar
def mostrar_produtos():
    print("\nProdutos disponíveis:")
    for nome, preco in produtos.items():
        print(f"{nome} - R$ {preco}")
        
Mostra todos os produtos da loja com seus preços, percorrendo o dicionário produtos com for.

Função para adicionar produtos ao carrinho:
python
Copiar
Editar
def adicionar_produto():
    try:
        nome = input("Produto: ").lower()
        if nome not in produtos:
            raise ProdutoInexistenteError("Esse produto não existe.")
Solicita o nome do produto ao usuário.

Converte para minúsculo (lower) para evitar erros por letras maiúsculas.

Verifica se o produto existe. Se não, lança uma exceção personalizada.

python
Copiar
Editar
        qtd = int(input("Quantidade: "))
        if qtd <= 0:
            raise ValueError("Quantidade deve ser positiva.")
Recebe a quantidade e converte para inteiro.

Verifica se a quantidade é maior que zero, caso contrário, levanta um ValueError.

python
Copiar
Editar
        carrinho[nome] = carrinho.get(nome, 0) + qtd
        print(f"{qtd}x {nome} adicionado(s) ao carrinho.")
Adiciona o produto ao carrinho. Se já existir, soma a nova quantidade com a anterior.

Mostra uma mensagem confirmando a adição.

python
Copiar
Editar
    except ProdutoInexistenteError as e:
        print("Erro:", e)
    except ValueError:
        print("Erro: informe uma quantidade válida (número inteiro positivo).")
Trata os dois erros possíveis: produto inexistente e quantidade inválida.

Função para ver o carrinho:
python
Copiar
Editar
def ver_carrinho():
    print("\nSeu carrinho:")
    total = 0
    for nome, qtd in carrinho.items():
        preco = produtos[nome] * qtd
        total += preco
        print(f"{qtd}x {nome} = R$ {preco}")
    print(f"Total: R$ {total}")
    return total
Mostra os itens no carrinho, quantidade, e valor total da compra.

Calcula o total somando o valor de cada item (preço x quantidade).

Retorna o total da compra.

Função para realizar o pagamento:
python
Copiar
Editar
def pagar():
    try:
        if not carrinho:
            print("Carrinho vazio.")
            return
Verifica se o carrinho está vazio. Se estiver, avisa e cancela a operação.

python
Copiar
Editar
        total = ver_carrinho()
        global saldo
        if total > saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
Chama a função ver_carrinho() para calcular o total.

Verifica se o saldo é suficiente. Se não for, levanta a exceção personalizada.

python
Copiar
Editar
        saldo -= total
        carrinho.clear()
        print(f"Pagamento aprovado! Novo saldo: R$ {saldo}")
    except SaldoInsuficienteError as e:
        print("Erro:", e)
Desconta o valor do saldo.

Limpa o carrinho.

Informa o novo saldo.

Se o saldo for insuficiente, exibe o erro.

Função principal com o menu:
python
Copiar
Editar
def menu():
    while True:
        print("\n1 - Ver produtos\n2 - Adicionar ao carrinho\n3 - Ver carrinho\n4 - Pagar\n5 - Sair")
        op = input("Escolha: ")
Exibe as opções para o usuário escolher o que deseja fazer.

A função menu() roda continuamente até o usuário escolher sair.

python
Copiar
Editar
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
Executa a função correspondente à escolha do usuário.

Se a opção for inválida, avisa o usuário.

Execução principal:
python
Copiar
Editar
if __name__ == "__main__":
    print("🛒 Bem-vindo à Loja Virtual Simples")
    menu()
Esse bloco garante que o menu só será executado se o arquivo for rodado diretamente.

Dá boas-vindas e chama o menu().
