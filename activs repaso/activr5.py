palabra1 = input ("Escribe una palabra: ")
palabra2 = palabra1 [::-1]

if palabra1 == palabra2:
    print ("Es un palindromo")
else:
    print ("no es palindromo")