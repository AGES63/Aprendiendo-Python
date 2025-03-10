#Código para invertir palabras

texto = input("Ingrese un texto: ")

palabras = texto.split()


for palabra in palabras:
    print(palabra[::-1], end = ' ')


