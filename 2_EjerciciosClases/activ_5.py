class Persona:
    def __init__(self):
        self.nombre = input("ingrese el nombre de la persona: ")
        self.edad = int(input ("ingrese la edad de la persona: "))

    def presentar(self):
        print("Hola, soy", self.nombre, "y tengo", self.edad, "años")
    

class empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingrese el sueldo del empleado: "))
    
    def mostrar_sueldo(self):
        print("El sueldo del empleado es:", self.sueldo)

    def impuestos(self):
        if self.sueldo >= 3000:
            print("pagas impuestos:")
        else:
            print("no pagas impuestos")
    

persona1 = Persona()
persona1.presentar()
empleado1 = empleado()
empleado1.mostrar_sueldo()
empleado1.impuestos()