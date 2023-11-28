from Animal_classes import Animais
from Mamíferos import Mamiferos
from Anfíbios import Anfibios
from Répteis import Reptil
from Peixes import Peixes
from Aves import Aves
import time
def main():
    escolha = ''
    animais = []
    while escolha != 0:
        
        print("-"*60)
        print("------BEM VENDO AO SISTEMA DE CATÁLOGO DE ANIMAIS!-------")
        print("-"*60)
        print("[1] Mamífero")
        print("[2] Anfíbio")
        print("[3] Peixe")
        print("[4] Ave")
        print("[5] Réptil")
        print("[6] Exibir Catálogo de Animais")
        print("[0] Fechar programa")  
        escolha = ''
        escolha = int(input("==> Insira o numero correspondente ao tipo do animal: "))
        while escolha > 1 or escolha < 6:
            if escolha > 1 or escolha < 6:
                if escolha == 0:
                    print("-"*60)
                    time.sleep(1)
                    print("Fechando Catálogo!")
                    time.sleep(1)
                    print("Até mais! ")
                    print("-"*60)
                    time.sleep(1)
                    break
                elif escolha == 1:
                    mamiferos = []
                    nome_mamifero = (input("Insira o nome do animal Mamífero que deseja catalogar: "))
                    comprimento_mamifero = (input(f"Insira comprimento de {nome_mamifero} em cm: "))
                    tamanho_mamifero = (input(f"Insira tamanho de {nome_mamifero} em cm: "))
                    patas_mamifero = (input(f"Insira quantidade de patas de {nome_mamifero}: "))
                    cor_mamifero = (input(f"Insira a cor do {nome_mamifero}: "))
                    ambiente_mamifero = (input(f"Insira ambiente que {nome_mamifero} vive: "))
                    alimento_mamifero = (input(f"Insira o tipo de alimento que {nome_mamifero} come: "))

                    for animal in range(0, len(mamiferos) + 1):
                        mamiferos.append({'nome': nome_mamifero, 'comprimento': comprimento_mamifero, 'tamanho': tamanho_mamifero, 'nº de patas': patas_mamifero, 'cor': cor_mamifero, 'ambiente': ambiente_mamifero, 'alimento': alimento_mamifero})
                        
                    animais.append(mamiferos)
                    mamifero = Mamiferos(nome=nome_mamifero, comprimento=comprimento_mamifero, tamanho=tamanho_mamifero, patas=patas_mamifero, cor=cor_mamifero, ambiente=ambiente_mamifero, alimento=alimento_mamifero)
                    mamifero.exibe_as_informacoes_mamiferos()
                    mamiferos_cadastrado = mamifero.adiciona_mamifero()
                    animais.append(mamiferos_cadastrado)
                    

                    print('-'*60)
                    print("Animal Adicionado!")
                    break

                elif escolha == 2:
                    anfibio = []
                    nome_anfibio = (input("Insira o nome do animal Anfíbio que deseja catalogar: "))
                    comprimento_anfibio = (input(f"Insira comprimento de {nome_anfibio} em cm: "))
                    tamanho_anfibio = (input(f"Insira tamanho de {nome_anfibio} em cm: "))
                    patas_anfibio = (input(f"Insira quantidade de patas de {nome_anfibio}: "))
                    cor_anfibio = (input(f"Insira a cor de {nome_anfibio}: "))
                    ambiente_anfibio = (input(f"Insira ambiente que {nome_anfibio} vive: "))
                    alimento_anfibio = (input(f"Insira o tipo de alimento que {nome_anfibio} come: "))

                    for animal in range(0, len(anfibio) + 1):
                        anfibio.append({'nome': nome_anfibio, 'comprimento': comprimento_anfibio, 'tamanho': tamanho_anfibio, 'nº de patas': patas_anfibio, 'cor': cor_anfibio, 'ambiente': ambiente_anfibio, 'alimento': alimento_anfibio})
                        

                    animais.append(anfibio)
                    anfibio = Anfibios(nome=nome_anfibio, comprimento=comprimento_anfibio, tamanho=tamanho_anfibio, patas=patas_anfibio, cor=cor_anfibio, ambiente=ambiente_anfibio, alimento=alimento_anfibio)
                    anfibio.exibe_informacoes_anfibios()
                    anfibio_cadastrado = anfibio.adiciona_anfibio()
                    animais.append(anfibio_cadastrado)

                elif escolha == 3:
                    peixe = []
                    nomepeixe = (input("Insira o nome do animal Peixe que deseja catalogar: "))
                    comprimentopeixe = (input(f"Insira comprimento de {nomepeixe} em cm: "))
                    tamanhopeixe = (input(f"Insira tamanho de {nomepeixe} em cm: "))
                    pataspeixe = (input(f"Insira quantidade de patas de {nomepeixe}: "))
                    corpeixe = (input(f"Insira a cor de {nomepeixe}: "))
                    ambientepeixe = (input(f"Insira ambiente que {nomepeixe} vive: "))
                    alimentopeixe = (input(f"Insira o tipo de alimento que {nomepeixe} come: "))

                    for animal in range(0, len(peixe) + 1):
                        peixe.append({'nome': nomepeixe, 'comprimento': comprimentopeixe, 'tamanho': tamanhopeixe, 'nº de patas': pataspeixe, 'cor': corpeixe, 'ambiente': ambientepeixe, 'alimento': alimentopeixe})
                        
                    
                    animais.append(peixe)
                    peixe = Peixes(nome=nomepeixe, comprimento=comprimentopeixe, tamanho=tamanhopeixe, patas=pataspeixe, cor=corpeixe, ambiente=ambientepeixe, alimento=alimentopeixe)
                    peixe.exibe_informacoes_peixe()
                    peixe_cadastrado = peixe.adiciona_peixe()
                    animais.append(peixe_cadastrado)

                elif escolha == 4:
                    ave = []
                    nome_ave = (input("Insira o nome do animal Ave que deseja catalogar: "))
                    comprimento_ave = (input(f"Insira comprimento de {nome_ave} em cm: "))
                    tamanho_ave = (input(f"Insira tamanho de {nome_ave} em cm: "))
                    patas_ave = (input(f"Insira quantidade de patas de {nome_ave}: "))
                    cor_ave = (input(f"Insira a cor de {nome_ave}: "))
                    ambiente_ave = (input(f"Insira ambiente que {nome_ave} vive: "))
                    alimento_ave = (input(f"Insira o tipo de alimento que {nome_ave} come: "))

                    for animal in range(0, len(ave) + 1):
                        ave.append({'nome': nome_ave, 'comprimento': comprimento_ave, 'tamanho': tamanho_ave, 'nº de patas': patas_ave, 'cor': cor_ave, 'ambiente': ambiente_ave, 'alimento': alimento_ave})
                        

                    animais.append(ave)
                    ave = Aves(nome=nome_ave, comprimento=comprimento_ave, tamanho=tamanho_ave, patas=patas_ave, cor=cor_ave, ambiente=ambiente_ave, alimento=alimento_ave)
                    ave.exibe_informacoes_ave()
                    ave_cadastrado = ave.adiciona_ave()
                    animais.append(ave_cadastrado)

                elif escolha == 5:
                    reptil = []
                    nome_reptil = (input("Insira o nome do animal Réptil que deseja catalogar: "))
                    comprimento_reptil = (input(f"Insira comprimento de {nome_reptil} em cm: "))
                    tamanho_reptil = (input(f"Insira tamanho de {nome_reptil} em cm: "))
                    patas_reptil = (input(f"Insira quantidade de patas de {nome_reptil}: "))
                    cor_reptil = (input(f"Insira a cor de {nome_reptil}: "))
                    ambiente_reptil = (input(f"Insira ambiente que {nome_reptil} vive: "))
                    alimento_reptil = (input(f"Insira o tipo de alimento que {nome_reptil} come: "))

                    for animal in range(0, len(reptil) + 1):
                        reptil.append({'nome': nome_reptil, 'comprimento': comprimento_reptil, 'tamanho': tamanho_reptil, 'nº de patas': patas_reptil, 'cor': cor_reptil, 'ambiente': ambiente_reptil, 'alimento': alimento_reptil})
                        

                    animais.append(reptil)
                    reptil = Reptil(nome=nome_reptil, comprimento=comprimento_reptil, tamanho=tamanho_reptil, patas=patas_reptil, cor=cor_reptil, ambiente=ambiente_reptil, alimento=alimento_reptil)
                    reptil.exibe_informacoes_reptil()
                    reptil_cadastrado = reptil.adiciona_reptil()
                    animais.append(reptil_cadastrado)
                    
                elif escolha == 6:
                    print("-" * 60)
                    for animal in range(len(animais)):
                        for ani in animais[animal]:
                            print("-="*30)
                            for key in ani:
                                print(key , ':', ani[key])
                    print("-" * 60)

            

            elif escolha < 0 or escolha > 6:
                print("-"*60)
                print("Opção invalida! ")
                print("-"*60)
                escolha = int(input("==> Insira o numero correspondente ao tipo do animal: "))   
            break
        if escolha == 0:
            breakpoint

if __name__ == '__main__':
    main()