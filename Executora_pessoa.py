#importar a classe Pessoa
from Pessoa import Pessoa
def main():
    # criar um objeto da classe Pessoa, para usar 
    # os pseudo-codigos criados

    pessoa_1 = Pessoa("Roberta", "14/05/2005", 1.75)
    # mostrar os dados da pessoa
    pessoa_1.imprime_dados()
    #mostra a idade da pessoa
    pessoa_1.calcula_idade()

if __name__ == '__main__':
    main()