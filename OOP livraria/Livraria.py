import datetime as dt
class Livraria:
    livros = [
    ["O Sol é para Todos","Harper Lee", "Romance, Justiça Social", "Editora José Olympio", "9788503009490", 10], 
    ["Sapiens: Uma Breve História da Humanidade", "Yuval Noah Harari", "História, Antropologia", "L&PM Editores", "9788525432187", 10], 
    [ "A Menina que Roubava Livros", "Markus Zusak", "Ficção Histórica", "Intrínseca", "9788580573494", 10], 
    ["O Poder do Hábito", "Charles Duhigg", "Psicologia, Desenvolvimento Pessoal", "Objetiva", "9788539004111", 10], 
    ["Norwegian Wood", "Haruki Murakami", "Ficção Contemporânea", "Editora Objetiva", "9788539004111", 10]]

    clientes = [
        {'nome' : 'Jean', 'endereco':'Rua Alberto Torres - 135', 'telefone' : '(54) 99688-1202', 'cpf' : '02973374081'}
    ]
    
    def __init__(self):
        print("\nBem vindo a Livraria!\nPara realizar o login digite:")
        self.nome = input("Insira seu nome: ")
        self.cpf = input("Insira seu cpf: ")

    def login(self, clientes):
        livros_comprado = []
        data_do_livro = []
        for pessoa in range(0, len(clientes)):
            if self.nome in clientes[pessoa]['nome'] and self.cpf in clientes[pessoa]['cpf']:
                print(f"Bem Vindo {clientes[pessoa]['nome']}!")
                print(f"Seu telefone é: {clientes[pessoa]['telefone']}.")
                print(f"Seu endereço é: {clientes[pessoa]['endereco']}.")
                print(f"Seu cpf é: {clientes[pessoa]['cpf']}.")

                print(f"Deseja comprar algum livro? ")
                escolha = input(f"[S] [N]: ")

                while escolha == 's':
                    livros_comprado.append(input("Digite o nome do livro que quer comprar: "))
                    data_do_livro.append(str(dt.date.today()))
                    
                compras = {'livros':livros_comprado,
                            'data do livro': data_do_livro}
                     
                
            else:
                print(f"Ocorreu um erro! Usuario não encontrado!")
    
        return compras
    
    #def cadastro(self):
        
    