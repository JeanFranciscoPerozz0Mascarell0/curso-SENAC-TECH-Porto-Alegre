from datetime import datetime
class Pessoa:
    #construtor da classe pessoa
    def __init__(self, nome, data_nascimento, altura):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.altura = altura
        
    #função imprimir todos os dados da classe
    def imprime_dados(self):
        print(f"Nome: {self.nome}, \nData: {self.data_nascimento}, \nAltura: {self.altura}.")

    #função que calcula a idade da pessoa
    def calcula_idade(self):
        #pegar o ano da data de hoje no computador
        ano_atual = datetime.today().year
        print("teste ano: ", ano_atual)
        #calculo da idade da pessoa
        partes_data = self.data_nascimento.split("/")
        ano_nascimento = partes_data[2]
        anos = ano_atual - int(ano_nascimento)
        print("A idade da pessoa é ", anos," anos")
        
