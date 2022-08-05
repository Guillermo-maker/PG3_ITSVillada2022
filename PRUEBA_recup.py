class banco:

    def depositar (self):
        deposito1 = 2000
        deposito2 = 15
        deposito3 = 400 
    
    def  cliente (self):
        cliente1 = "Pedro"
        cliente2 = "Juan"
        cliente3 = "Ricardo"


    def extraer (self):
        t = 1
    while t == 1:
        try:
            menu = input ("cual es su usuario...1 cliente1, 2 cliente2,  3 cliente3,")
            if menu2 == 1:
                print ("usted es"+ cliente1)
            elif menu2 == 2:
                print ("usted es"+ cliente2)
            elif menu2 == 3:
                print ("usted es"+ cliente3)
            
            print ("ahora elija su deṕosito")

            menu2 = input ("ingrese el dinero que quiere extraer...1 deposito1, 2 deposito2,  3 deposito3, 4 para salir")
            if menu2 == 1:
                print ("usted tiene"+ deposito1 + " pesos")
            elif menu2 == 2:
                print ("usted tiene"+ deposito2 + " pesos")
            elif menu2 == 3:
                print ("usted tiene"+ deposito3 + " pesos")
            elif menu2 == 4:
                print("Adios")
                t = 0
        except (ValueError):
            print ("ingrese los datos correctos")
