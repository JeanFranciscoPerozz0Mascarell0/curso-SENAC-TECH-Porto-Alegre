lista_tarefas = []

def separando(value = False):
    print("-"*40)

def add_tarefa(tarefa: str):
    tarefa = input("Insira a tarefa que deseja realizar: ")
    lista_tarefas.append(tarefa)

separando(True)
acao = str(input("Bem vindo a sua lista de tarefas!\n1) adicionar tarefa a lista\n2) excluir tarefa da lista\n3) mostrar lista\nDigite a tarefa que deseja realizar: "))


add_tarefa()
        
    case 2:
        
        print(lista_tarefas)
        tarefa_excluir = input("Digite a tarefa que você deseja excluir: ")
        lista_tarefas.remove(tarefa_excluir)
        
separando(True)
print(lista_tarefas)

