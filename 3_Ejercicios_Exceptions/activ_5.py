while True:
    
    try:
        texto = input("Escriba cualquier texto:  ")
        archivo = open('texto_ejemplo.txt', 'w')

        if texto.isnumeric():
            archivo.write(int(texto))
        else:
            menu = int (input ("para terminar...(0)...para continuar...(1): "))

        if menu == 0:
            print ("esto fue el ejercio 5... muchas gracia por su participacion...")
            break

    except TypeError:
        print("Ingrese un texto...")