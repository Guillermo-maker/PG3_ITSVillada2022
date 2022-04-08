lista = []

def funcion(lista):
    lista = [int(item) for item in input("Ingrese una lista de numeros: ").split()]

    lista.sort(reverse = True)

    print(lista)

funcion(lista) 