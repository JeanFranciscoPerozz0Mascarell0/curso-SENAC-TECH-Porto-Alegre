from Body_Mass import Calculate_Body_Mass
def main():

    pessoa_1 = Calculate_Body_Mass("",0,0.0)
    
    pessoa_1.set_name(input("NOME: "))
    
    pessoa_1.set_body_mass(float(input("PESO: ")))
       
    pessoa_1.set_height(float(input("ALTURA: ")))
    pessoa_1.calculate_body_mass()
    pessoa_1.printing()
    pessoa_1.compare_datas()

if __name__ == '__main__':
    main()


