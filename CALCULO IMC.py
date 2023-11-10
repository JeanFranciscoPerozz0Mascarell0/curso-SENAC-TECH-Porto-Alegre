pessoas = []

def calcular_imc(peso = 0, altura = 0):
    resultado = peso / (altura**2)

    if resultado >= 17 and resultado <= 18.4:
        return f'está com o IMC de {resultado:.2f}, e está com magreza leve.'
    elif resultado <= 16.9 and resultado >= 16:
        return f'está com o IMC de {resultado:.2f}, e está com magreza moderada.'
    elif resultado < 16:
        return f'está com o IMC de {resultado:.2f}, e está com magreza grave.'
    elif resultado <= 29.9 and resultado >= 25:
        return f'está com o IMC de {resultado:.2f}, e está com sobrepeso.'
    elif resultado <= 34.9 and resultado >= 30:
        return f'está com o IMC de {resultado:.2f}, e está com obesidade grau 1.'
    elif resultado <= 39.9 and resultado >= 35:
        return f'está com o IMC de {resultado:.2f}, e está com obesidade severa.'
    elif resultado >= 40:
        return f'está com o IMC de {resultado:.2f}, e está com obesidade mórbida.'
    else:
        return f'está com o IMC de {resultado:.2f}, e está no peso ideal.'

def imprimir(imprima = False):
    for c in range(len(pessoas)):
        print(f"{pessoas[c]['nome']} {calcular_imc(pessoas[c]['peso'], pessoas[c]['altura'])}")

for pessoa in range(0,5):
    nome = input("Digite seu nome: ")
    altura = float(input("Insira sua altura: "))
    peso = float(input("Insira seu peso: "))
    print('-'*50)
    pessoas.append({'nome': nome, 'altura' : altura, 'peso' : peso})

imprimir(True)
