while True:

    try:
        num1 = int(input ("ingrese el primer numero:"))
        num2 = int(input ("ingrese el segundo numero:"))

        r = num1 / num2

        print ("el resultado es:", r)
        menu = int (input ("para terminar...(0)...para continuar...(1): "))

        if menu == 0:
            print ("esto fue el ejercio 1... muchas gracia por su participacion...")
            break
            
            

    except ( ZeroDivisionError):
        print ("ingrese numeros correctamente...no se puede dividir por cero")
    