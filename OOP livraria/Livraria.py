from datetime import date 
class Livraria:
    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

        
        
    def cadastro(self):
        self.nome = input("Insira o nome do usuario: ")
        self.telefone = input("Insira o telefone: ")
        self.endereco = input("Insira o endereço: ")
        self.cpf = input("Insira o cpf: ")

        self.cliente = [self.nome, self.telefone, self.endereco, self.cpf]

        
    
    def inserindo_livros(self):
        self.livros = {}
        escolha = 'S'
        while escolha == 'S':        
            livro_escolhido = input("Insira o nome do livro escolhido: ")
            dia_de_hoje = str(date.today())
            self.livros[livro_escolhido] = dia_de_hoje
            escolha = input("Deseja comprar algum livro? ").upper() 
        
        self.cliente.append(self.livros)
        

