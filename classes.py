# class Automovel: 
#     pass
#     #criação(instanciação) de objeto(s).
#     #todo objeto é uma variavel.
# Honda = Automovel()
# VW = Automovel()

# Honda.ano = 2021
# Honda.modelo = 'Civic'
# Honda.cor = 'azul'

# VW.ano = 2021
# VW.modelo = 'Pointer'
# VW.cor = 'cinza'

# print("Honda é igual a VW: ", Honda == VW)

# VW.ano += 5
# print("novo ano Honda", VW.ano)


# class Automovel:
#     def __init__(self, ano, modelo, cor):
#         self.ano = ano
#         self.modelo = modelo
#         self.cor = cor

# Fiat = Automovel(2023, 'Uno', 'vermelho')
# print("Modelo: ", Fiat.modelo,"\nAno: ", Fiat.ano,"Cor: ", Fiat.cor)
        
class Addition:
    first = 0
    second = 0
    answer = 0

    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = "+ str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second

obj = Addition(1000, 2000)
obj.calculate()
obj.display()
