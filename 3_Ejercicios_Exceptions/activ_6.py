import pymysql

while True:
    connection = pymysql.connect( host='localhost', user= 'bdi', passwd='pepe1234', db='Exepciones')
    cur = connection.cursor()
    code = input("Cod de la base de datos: ")

    try:
        cur.execute(code)
    except pymysql.err.ProgrammingError as error:
        print(error, "\n__Error en la sintaxis__")

    except pymysql.err.InternalError as error:
        print(error, "\n__Error__")
        
    except pymysql.err.OperationalError as error:
        print(error, "\n__ERROR...__")

        menu = int (input ("para terminar...(0)...para continuar...(1): "))
        if menu == 0:
            print ("esto fue el ejercio 6... muchas gracia por su participacion...")
            break
    connection.close()