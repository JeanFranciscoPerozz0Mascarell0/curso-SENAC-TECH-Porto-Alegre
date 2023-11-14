class Calculate_Body_Mass:
    def __init__(self, name, body_mass, height):

        self.name = name
        self.body_mass = body_mass
        self.height = height
        self.thinness = 18.5
        self.normal = 24.9
        self.overweight = 29.9
        self.obesity = 34.9
        self.obesity2 = 39.9
        self.obesity3 = 40
    
    def printing(self):
        print(f"Nome: {self.name} \nPeso: {self.body_mass} \nAltura: {self.height}")
    
    def calculate_body_mass(self):
        self.body_mass_calculating = self.body_mass/(self.height*self.height)

    def set_name(self, inserted_name):
        self.name = inserted_name
    
    def get_name(self):
        return self.name
    
    def set_height(self, inserted_height):
        self.height = inserted_height
    
    def get_height(self):
        return self.height
    
    def set_body_mass(self, inserted_body_weight):
        self.body_mass = inserted_body_weight
    
    def get_body_mass(self):
        return self.body_mass
    
    def compare_datas(self):
        if self.body_mass_calculating < self.thinness:
            print(self.name,"é desnutrido")
        elif self.body_mass_calculating < self.normal:
            print(self.name, "peso ideal")
        elif self.body_mass_calculating < self.overweight:
            print(self.name, "acima do peso ideal")    
        elif self.body_mass_calculating < self.obesity:
            print(self.name, "obesidade grau I")
        elif self.body_mass_calculating < self.obesity2:
            print(self.name, "obesidade grau II") 
        else:
            print(self.name, "obesidade grau III")