import os
import time as t

class Matematica:
    
    def __init__(self, expressao):
        self.expressao = expressao

    def limpar_terminal():
            os.system('cls')

    def calcular(expressao):
        try:
            resultado = eval(expressao)
            return resultado
        except Exception as e:
            return f"Erro na expressão: {e}"

    def calculadora():
        while True:
            print("________________________________________CALCULADORA________________________________________\n\nExpressões: \n\nDivisão: '/'\nMultiplicação: '*'\nSoma: '+'\nSubtração: '-'\nPotenciação: '**' \nRadiciação: 'n ** 0.5'\n")
            expressao = input("Digite uma expressão matemática ou 'sair': ")
            if expressao.lower() == 'sair':
                print("Calculadora encerrada. Até mais!")
                break
            resultado = calcular(expressao)
            print(f"\nRESULTADO: {resultado}")
            t.sleep(5)
            limpar_terminal()

    calculadora()
