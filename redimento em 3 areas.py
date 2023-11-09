def separar(ligado = False):
    print("-"*50)

investimento_inicia = float(input("Digite o valor que deseja investir: R$ "))

print("Insira a escolha do tempo que deseja investir: ")
print("1) dia(s)")
print("2) meses(s)")
print("3) ano(s)")

tipo_tempo_de_investimento = int(input("Insira sua escolha: "))

match tipo_tempo_de_investimento:
    case 1: 
        modelo = 'dia(s)'
        tempo_total = int(input(f"Insira quantos {modelo} você deseja investir: "))
        tempo = tempo_total/360
    
    case 2: 
        modelo = 'mes(es)'
        tempo_total = int(input(f"Insira quantos {modelo} você deseja investir: "))
        tempo = tempo_total/12
    
    case 3: 
        modelo = 'ano(s)'
        tempo_total = int(input(f"Insira quantos {modelo} você deseja investir: "))
        tempo = tempo_total/1

#selecione o tipo de investimento
separar(ligado = True)
investimento = int(input("\nSelecione o tipo de investimento: \n\n1) Investimento do GUGU\n2)Al-mosso imvestimentos 🤡🤡🤡\n3)Amarelinha investimentos \n4)Desejo ver a descrição dos investimentos\n\nInsira a escolha:"))
while investimento == 4:
    separar(ligado = True)
    print("1. Investimento do GUGU: investimento com lucro de 10 por cento ao ano sobre o valor investido inicial.\n2. Al-mosso imvestimentos 🤡🤡🤡: lucro de 25 por cento sobre o valor investido por ano.\n3. Amarelinha investimentos: lucro de 4 por cento do valor investido ao ano.")
    separar(ligado = True)
    investimento = int(input("Escolha seu tipo de investimento: "))
    separar(ligado = True)
match investimento:
    case 1:
        lucro = investimento_inicia * 0.1
        saldo_total = lucro * tempo
        saldo_final = saldo_total + investimento_inicia
    case 2:
        lucro = investimento_inicia * 0.25 
        saldo_total =  lucro * tempo
        saldo_final = saldo_total + investimento_inicia
    case 3:
        lucro = investimento_inicia * 0.4
        saldo_total = lucro * tempo
        saldo_final = saldo_total + investimento_inicia 
        
print(f"O valor investido foi: {investimento_inicia:.2f}.")
print(f"O tempo investido foi de: {tempo_total} {modelo}.")
print(f"O valor do lucro potencial seria: {saldo_total:.2f}.")
print(f"O valor do lucro total seria: {saldo_final:.2f}.\n")
separar(ligado = True)