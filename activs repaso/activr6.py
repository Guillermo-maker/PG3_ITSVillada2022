
def contavocal(p):
      
   
    contador = 0

    vocales = set("aeiouAEIOU")
      
    for alphabet in p:
      
        if alphabet in vocales:
            contador = contador + 1
      
    print("numero de voclales :", contador)
      

p = input("ingresar palabra: ")
  
contavocal(p)