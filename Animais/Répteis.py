from Animal_classes import Animais
class Reptil(Animais):
    def __init__(self, nome: str, tamanho: str, comprimento: str, patas: str, cor: str, ambiente: str, alimento:str):
        super().__init__(nome, tamanho, comprimento, patas, cor, ambiente)
        self.alimento = alimento
    
    def exibe_informacoes_reptil(self):
        tipo_animal = 'RÉPTIL'
        print("-"*50)
        print(f"Esse animal é um {tipo_animal}!")
        super().exibe_informacoes()
        print(f"ALIMENTO: {self.alimento}")

    def adiciona_reptil(self):
        reptil = []
        for animal in range(0, len(reptil)):
            reptil.append({'nome': self.nome, 'comprimento': self.comprimento, 'tamanho': self.tamanho, 'nº de patas': self.patas, 'cor': self.cor, 'ambiente': self.ambiente, 'alimento': self.alimento})    
        return reptil