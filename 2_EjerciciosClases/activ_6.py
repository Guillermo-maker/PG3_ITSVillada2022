class Familia:
    def __init__(self):
        self.np =input("Ingrese el nombre de padre: ")
        self.nm =input("Ingrese el nombre de la madre: ")
        self.Af =input("Ingrese el apellido de la familia: ")  
        self.hijos =input("Ingrese el nombre de los hijos de la familia  un  space a la vez: ").split()

    def __str__(self):
        string = self.nm + "," + self.nm
        for i in self.hijos:
            string = string + "," + i
        return string


familia1 = Familia()

print(familia1)
