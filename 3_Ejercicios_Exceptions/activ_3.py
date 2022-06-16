while True:
    try:    
        meses = ("Enero", "Febrero", "Marzo", "Abril", 'Mayo', 'Junio', 'Julio'
                ,'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

        print (meses)

        pickmes = int (input("elija el mes segun el numero: "))

        print (meses[pickmes - 1])
        menu = int (input ("para terminar...(0)...para continuar...(1): "))
        if menu == 0:
            print ("esto fue el ejercio 3... muchas gracia por su participacion...")
            break

    except (IndexError,ValueError):
        print( "ingres el numero del mes correctamente")

