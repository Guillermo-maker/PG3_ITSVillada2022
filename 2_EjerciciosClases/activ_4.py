class Operacion:

    def __init__(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es",suma)

    def restar(self):
        resta=self.valor1-self.valor2
        print("La rersta es",resta)

    def multiplicar(self):
        mult=self.valor1*self.valor2
        print("El producto es",mult)

    def dividir(self):
        div=self.valor1/self.valor2
        print("La division es",div)


operacion1=Operacion()