#Código para diccionario de palabras con traducción a otro idioma

idioma = input("Ingrese el idioma en el que se traducirán las palabras: ")

diccionario = {}

m = int(input("Ingrese la cantidad de palabras a añadir al diccionario: "))

for i in range(0,m):
    palabra = input("Ingrese una palabra: ")
    traducción = input("Ingrese la palabra traducida al " + idioma + ": ")
    diccionario[palabra] = traducción
    i=+1
    
print(diccionario)
