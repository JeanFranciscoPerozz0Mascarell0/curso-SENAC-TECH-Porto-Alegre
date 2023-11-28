from Animal_classes import Animais
class Mamiferos(Animais):
    def __init__(self, nome: str, tamanho: str, comprimento: str, patas: str, cor: str, ambiente: str,alimento:str):
        super().__init__(nome, tamanho, comprimento, patas, cor, ambiente)
        self.alimento = alimento

    def exibe_as_informacoes_mamiferos(self):
        tipo_animal = 'MAMÍFERO'
        print("-"*50)
        print(f"Esse animal é um {tipo_animal}!")
        super().exibe_informacoes()
        print(f"ALIMENTO: {self.alimento}")

    def adiciona_mamifero(self):
        mamiferos = []
        for animal in range(0, len(mamiferos)):
            mamiferos.append({'nome': self.nome, 'comprimento': self.comprimento, 'tamanho': self.tamanho, 'nº de patas': self.patas, 'cor': self.cor, 'ambiente': self.ambiente, 'alimento': self.alimento})    
        return mamiferos