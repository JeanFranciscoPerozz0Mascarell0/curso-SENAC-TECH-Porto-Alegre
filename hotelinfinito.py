hotel = {}

for hospede in range(5):
    nome = input("Insira o nome do hospede: ")
    andar = input("Digite qual o andar que você deseja ficar: ")
    hotel[nome] = andar
    
if andar in hotel.values():
    hotel.values(andar)
    
