# Elabore um sistema de uma livraria. De acordo com os requisitos a seguir:
# 1. A livraria deseja manter um cadastro de clientes.

# 2. Sobre cada cliente, é importante manter seu endereço, telefone, CPF e lista dos livros que este cliente já comprou. Para cada compra, é importante guardar a data em que esta foi realizada.

# 3. Um cliente pode comprar muitos livros. Um livro pode ser vendido para mais de um cliente pois geralmente há vários livros em estoque.

# 4. Um cliente pode ser pessoa física ou jurídica. Se for pessoa jurídica, o seu identificador deve ser o CNPJ e pessoa física CPF.

# 5. Cada cliente tem um código único.

# 6. Deve-se manter um cadastro sobre cada livro na livraria. Para cada livro, é importante armazenar o nome do autor, assunto, editora, ISBN e a quantidade dos livros em estoque.

import datetime as date

print("Bem vindo a Livraria!")
print("Digite o que deseja fazer!")
print("Digite [1] para fazer um login de usuario")
print("Digite [2] para fazer realizar um novo cadastro")
print("Digite [3] para sair")
escolha = int(input("Digite sua escolha: "))
clientes = [{'login' : 'Jean','nome' : 'Jean Francisco Perozzo Mascarello', 'cpf' : '02973374081', 'endereco' : 'Rua Alberto Torres - 135', 'telefone' : '32912683'}]
livros_comprados_do_cliente = []
match escolha:
    case 1: 
        print("Seu login é seu nome e sua senha é seu cpf.")
        login = input("Digite seu endereco de Login: ")
        senha = input("Digite sua senha: ")

        for pessoa in clientes:
            if login in clientes[0]['login'] and senha in clientes[0]['cpf']:
                print(f"Bem vindo {clientes[0]['nome']}!")
                print(f"Seu cpf é: {clientes[0]['cpf']}.")
                print(f"Seu endereco é: {clientes[0]['endereco']}.")
                print(f"Seu telefone é: {clientes[0]['telefone']}.")

                print("Deseja comprar um novo livro? ")
                comprar_novo_livro = input("[S] para SIM\n[N] para NÃO\nO que deseja fazer?").upper()
                while comprar_novo_livro == 's':
                    nome_livro = input("Insira o nome do livro: ")
                    quantidade_de_livros_comprados = input("Quantos livros deseja comprar? ")
                    data_da_compra = str(date.date.today())
                    livros_comprados_do_cliente.append({'nome_livro':nome_livro, 'quantidade_compra': quantidade_de_livros_comprados, 'data_compra':data_da_compra})
                    print("Deseja comprar um novo livro? ")
                    comprar_novo_livro = input("[S] para SIM\n[N] para NÃO\nO que deseja fazer?").upper()
                clientes.append()
            else:
                print("Você não está cadastrado!")