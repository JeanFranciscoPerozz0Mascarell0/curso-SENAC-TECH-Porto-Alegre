from Animal_classes import Animais
from Mamíferos import Mamiferos
from Anfíbios import Anfibios
from Répteis import Reptil
from Peixes import Peixes
from Aves import Aves
def main():
    while True:
        print("-"*20)
        print("------BEM VENDO AO SISTEMA DE CATÁLOGO DE ANIMAIS!-------")
        print("-"*20)
        print("[1] Mamífero")
        print("[2] Anfíbio")
        print("[3] Peixe")
        print("[4] Ave")
        print("[5] Réptil")
        escolha = int(input("==> Insira o numero correspondente ao tipo do animal: "))
        match escolha:
            case 1:
                nome_mamifero = (input("Insira o nome do animal Mamífero que deseja catalogar: "))
                comprimento_mamifero = (input(f"Insira comprimento de {nome_mamifero}: "))
                tamanho_mamifero = (input(f"Insira tamanho de {nome_mamifero}: "))
                patas_mamifero = (input(f"Insira quantidade de patas de {nome_mamifero}: "))
                cor_mamifero = (input(f"Insira a cor de {nome_mamifero}: "))
                ambiente_mamifero = (input(f"Insira ambiente que {nome_mamifero} vive: "))
                alimento_mamifero = (input(f"Insira o tipo de alimento que {nome_mamifero} come: "))

                mamifero = Mamiferos(nome=nome_mamifero, comprimento=comprimento_mamifero, tamanho=tamanho_mamifero, patas=patas_mamifero, cor=cor_mamifero, ambiente=ambiente_mamifero, alimento=alimento_mamifero)
                mamifero.exibe_as_informacoes_mamiferos()

            case 2:
                nome_anfibio = (input("Insira o nome do animal Anfíbio que deseja catalogar: "))
                comprimento_anfibio = (input(f"Insira comprimento de {nome_anfibio}: "))
                tamanho_anfibio = (input(f"Insira tamanho de {nome_anfibio}: "))
                patas_anfibio = (input(f"Insira quantidade de patas de {nome_anfibio}: "))
                cor_anfibio = (input(f"Insira a cor de {nome_anfibio}: "))
                ambiente_anfibio = (input(f"Insira ambiente que {nome_anfibio} vive: "))
                alimento_anfibio = (input(f"Insira o tipo de alimento que {nome_anfibio} come: "))

                anfibio = Anfibios(nome=nome_anfibio, comprimento=comprimento_anfibio, tamanho=tamanho_anfibio, patas=patas_anfibio, cor=cor_anfibio, ambiente=ambiente_anfibio, alimento=alimento_anfibio)
                anfibio.exibe_informacoes_anfibios()

            case 3:
                nomepeixe = (input("Insira o nome do animal Peixe que deseja catalogar: "))
                comprimentopeixe = (input(f"Insira comprimento de {nomepeixe}: "))
                tamanhopeixe = (input(f"Insira tamanho de {nomepeixe}: "))
                pataspeixe = (input(f"Insira quantidade de patas de {nomepeixe}: "))
                corpeixe = (input(f"Insira a cor de {nomepeixe}: "))
                ambientepeixe = (input(f"Insira ambiente que {nomepeixe} vive: "))
                alimentopeixe = (input(f"Insira o tipo de alimento que {nomepeixe} come: "))

                peixe = Peixes(nome=nomepeixe, comprimento=comprimentopeixe, tamanho=tamanhopeixe, patas=pataspeixe, cor=corpeixe, ambiente=ambientepeixe, alimento=alimentopeixe)
                peixe.exibe_informacoes_peixe()

            case 4:
                nome_ave = (input("Insira o nome do animal Ave que deseja catalogar: "))
                comprimento_ave = (input(f"Insira comprimento de {nome_ave}: "))
                tamanho_ave = (input(f"Insira tamanho de {nome_ave}: "))
                patas_ave = (input(f"Insira quantidade de patas de {nome_ave}: "))
                cor_ave = (input(f"Insira a cor de {nome_ave}: "))
                ambiente_ave = (input(f"Insira ambiente que {nome_ave} vive: "))
                alimento_ave = (input(f"Insira o tipo de alimento que {nome_ave} come: "))

                ave = Aves(nome=nome_ave, comprimento=comprimento_ave, tamanho=tamanho_ave, patas=patas_ave, cor=cor_ave, ambiente=ambiente_ave, alimento=alimento_ave)
                ave.exibe_informacoes_ave()

            case 5:
                nome_reptil = (input("Insira o nome do animal Réptil que deseja catalogar: "))
                comprimento_reptil = (input(f"Insira comprimento de {nome_reptil}: "))
                tamanho_reptil = (input(f"Insira tamanho de {nome_reptil}: "))
                patas_reptil = (input(f"Insira quantidade de patas de {nome_reptil}: "))
                cor_reptil = (input(f"Insira a cor de {nome_reptil}: "))
                ambiente_reptil = (input(f"Insira ambiente que {nome_reptil} vive: "))
                alimento_reptil = (input(f"Insira o tipo de alimento que {nome_reptil} come: "))

                reptil = Reptil(nome=nome_reptil, comprimento=comprimento_reptil, tamanho=tamanho_reptil, patas=patas_reptil, cor=cor_reptil, ambiente=ambiente_reptil, alimento=alimento_reptil)
                reptil.exibe_informacoes_reptil()
            case _:
                while escolha > 5 or escolha < 1:
                    print("-"*60)
                    print("Opção inválida!")
                    print("-"*60)
                    print("------BEM VENDO AO SISTEMA DE CATÁLOGO DE ANIMAIS!-------")
                    print("-"*20)
                    print("[1] Mamífero")
                    print("[2] Anfíbio")
                    print("[3] Peixe")
                    print("[4] Ave")
                    print("[5] Réptil")
                    escolha = int(input("==> Insira o numero correspondente ao tipo do animal: "))

    


if __name__ == '__main__':
    main()