class Animais():
    def __init__(self, nome:str, tamanho:str, comprimento:str, patas:str, cor:str, ambiente:str):
        self.nome = nome
        self.tamanho = tamanho
        self.comprimento = comprimento
        self.patas = patas
        self.cor = cor
        self.ambiente = ambiente
    
    
    def exibe_informacoes(self):
        print(f"NOME: {self.nome}")
        print(f"TAMANHO: {self.tamanho}")
        print(f"COMPRIMENTO: {self.comprimento}")
        print(f"PATAS: {self.patas}")
        print(f"COR: {self.cor}")
        print(f"AMBIENTE: {self.ambiente}")
    

