from Berçario import Bebe
from Berçario import Mae
from Berçario import Medico
def main():

    print("-------SOBRE O BEBE, INSIRA AS INFORMAÇÕES------------")
    nome = input("Digite o nome do Bebe: ")
    nascimento = str(input("Insira a data de nascimento do bebê: "))
    peso = float(input("Insira o peso (em gramas) do bebê: "))
    altura = float(input("Insira a altura (em cm) do bebê: "))
    nome_mae = input("Insira o nome da mãe do bebê: ")
    medico = input("Digite o nome do medico que realizou o parto: ")
    
    print("-------SOBRE O MÃE, INSIRA AS INFORMAÇÕES------------")

    endereco_da_mae = input("Insira o endereco da mãe: ")
    telefone_da_mae = str(input("Insira o telefone da mãe: "))
    data_nascimento_mae = str(input("Insira a data de nascimento da mãe: "))

    print("-------SOBRE O MEDICO, INSIRA AS INFORMAÇÕES------------")
    #CRM, nome, telefone celular e especialidade.
    crm_medico = input("Insira o CRM do médico: ")
    telefone_do_medico = str(input("Insira o telefone do médico: "))
    celular_do_medico = str(input("Insira o celular do médico: "))
    especialidade_medico = input("Insira a especialidade do médico: ")
   
   
    bebezinho = Bebe(nome=nome, data_nascimento=nascimento, peso_nascimento=peso, altura=altura, nome_mae=nome_mae, medico_parto=medico)
    bebezinho.exibindo_nome_do_bebe()

    mae_do_bebe = Mae(nome_mae=nome_mae, endereco_mae=endereco_da_mae,telefone_mae=telefone_da_mae, data_nascimento_mae=data_nascimento_mae)
    mae_do_bebe.exibe_informacoes_mae()

    medico_do_bebe = Medico(nome_medico=medico, crm=crm_medico, telefone_medico=telefone_do_medico, celular_medico=celular_do_medico, especialidade_medico=especialidade_medico)
    medico_do_bebe.exibe_informacoes_medico()

if __name__ == '__main__':
    main()