from Livraria_Nova import Livraria
def main():
    print("Bem vindo a Livraria!")
    print("Digite o que deseja fazer!")
    print("Digite [1] para fazer um login de usuario")
    print("Digite [2] para fazer realizar um novo cadastro")
    print("Digite [3] para sair")
    escolha = input("Digite sua escolha: ")
    if escolha == '1':
        Livraria.login_de_usuario()
    # elif escolha == '2':
    #     Livraria


if __name__ == "__main__":
    main()