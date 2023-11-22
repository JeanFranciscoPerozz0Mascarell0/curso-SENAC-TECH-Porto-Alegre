class Bebe:
    def __init__(self, nome:str, data_nascimento:str, peso_nascimento:int, altura:float, nome_mae:str, medico_parto:str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.peso_nascimento = peso_nascimento
        self.altura = altura
        self.nome_mae = nome_mae
        self.medico_parto = medico_parto

    def exibindo_nome_do_bebe(self):
        print(f'O nome do bebe nascido no dia {self.data_nascimento[0:2]}/{self.data_nascimento[3:5]}/{self.data_nascimento[6:]} é {self.nome} com sua mãe sendo {self.nome_mae}.')

class Mae:
    def __init__(self, nome_mae:str, endereco_mae:str, telefone_mae:str, data_nascimento_mae:str):
        self.nome_mae = nome_mae
        self.endereco_mae = endereco_mae
        self.telefone_mae = telefone_mae
        self.data_nascimento_mae = data_nascimento_mae

    def exibe_informacoes_mae(self):
        print(f"O nome da mãe é {self.nome_mae} e ela nasceu {self.data_nascimento_mae[0:2]}/{self.data_nascimento_mae[3:5]}/{self.data_nascimento_mae[6:]}.")

class Medico:
    def __init__(self, crm:str, nome_medico:str, telefone_medico:str, celular_medico:str, especialidade_medico:str):
        self.crm = crm
        self.nome_medico = nome_medico
        self.telefone_medico = telefone_medico
        self.celular_medico = celular_medico
        self.especialidade_medico = especialidade_medico

    def exibe_informacoes_medico(self):
        print(f"O medico que realizou o parto foi {self.nome_medico}, seu CRM é {self.crm} e sua especialidade é {self.especialidade_medico}.")