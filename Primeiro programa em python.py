
print("Bem vindo a calculadora!")
n1 = input(float("Digite o primeiro numero a ser calculado: "))
n2 = input(float("Digite o segundo numero: "))

acao = input(str("1) somar\n2)subtrair\n3)multiplicar\n4)dividir\nDigite a ação que deseja executar: "))

def somar(soma, n1, n2):
    soma = n1 + n2
    return f"A soma dos elementos digitados é: {soma}."

def subtrair(subtracao, n1, n2):
    subtracao = n1 + n2
    return f"A soma dos elementos digitados é: {subtracao}."

def multiplicar(multiplicar, n1, n2):
    multiplicar = n1 + n2
    return f"A soma dos elementos digitados é: {multiplicar}."

def dividir(divisao, n1, n2):
    divisao = n1 + n2
    return f"A soma dos elementos digitados é: {divisao}."


if(acao == 1):
    acao = somar()

elif(acao == 2):
    acao == subtrair()

elif(acao == 3):
    acao == multiplicar()

elif(acao == 4):
    acao == dividir()

else:  
    print("Erro na escolha")
