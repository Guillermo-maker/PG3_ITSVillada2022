class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        print("Hola, soy", self.nombre, "y tengo", self.edad, "años")
    

persona1 = Persona(nombre =input ("ingrese el nombre de la persona: "), edad = int (input ("ingrese la edad de la persona: ")));
persona1.presentar()