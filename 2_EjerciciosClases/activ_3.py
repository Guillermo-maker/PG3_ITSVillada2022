class Triangulo:


    def inicializar(self, ancho, largo, letra ):
        self.ancho = ancho
        self.largo = largo
        self.letra = letra

    def triangulo(self):
       for self.largo in range(self.ancho):
            for j in range(self.ancho- self.largo - 1):
                    print(" ", end="")
            for j in range(self.largo+1):
                print(self.letra, end=" ")
            print( ) 
        

    def equilatero(self):
        if self.ancho == self.largo:
            print("Es un triangulo equilatero")
        else:
            print("No es un triangulo equilatero")

            

t1=Triangulo()
t1.inicializar(ancho = int(input ("escriba el ancho: ")),largo = int(input ("escriba el largo: ")), letra = input("escriba la letra: "))
t1.equilatero()
t1.triangulo()


    