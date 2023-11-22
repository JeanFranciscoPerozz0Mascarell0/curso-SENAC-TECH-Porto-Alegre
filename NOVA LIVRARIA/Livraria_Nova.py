class Livraria:
    clientes = [
        {'nome' : 'Jean', 'endereco':'Rua Alberto Torres - 135', 'telefone' : '(54) 99688-1202', 'cpf' : '02973374081'}
    ]
    def __init__(self,escolha):
        pass

    def login_de_usuario(self):
        clientes = [{'nome' : 'Jean', 'endereco':'Rua Alberto Torres - 135', 'telefone' : '(54) 99688-1202', 'cpf' : '02973374081'}]
        nome = input("Insira o nome do usuario: ")
        cpf = input("Insira o cpf: ")

        if nome in clientes[0]['nome'] and cpf in clientes[0]['cpf']:
            print("Login funcionou!")
        else:
            print("Login não funcionou!")


