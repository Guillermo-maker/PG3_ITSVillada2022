letra = input ("Escribe una letra: ")
largo = int(input("Escriba el largo de la lista: "))
ancho = int(input("Escriba el ancho de la lista: "))

for i in range (1,ancho +1 ):
    for j in range (1,largo +1 ):
        print (letra, end = "")
    print (" ")