pessoas = []

#def imc(peso = 0, altura = 0):
#    resultado = peso / (altura*altura)
#    return pessoas.append(resultado)

#def imprimir():
#    print(f"O usuario {pessoas[0]['nome']} está com {pessoas[0]['nome']} ")


for pessoa in range(0,5):
    nome = input("Digite seu nome: ")
    altura = float(input("Insira sua altura: "))
    peso = float(input("Insira seu peso: "))
    print('-'*50)

    variavel_imc = peso / (altura * altura)
    
    pessoas.append({'nome': nome, 'altura' : altura, 'peso' : peso})

    #imc(peso, altura)


 

