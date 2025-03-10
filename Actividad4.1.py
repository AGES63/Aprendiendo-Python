#Código para contar palabras


oración = input("Ingrese una oración: ")
palabras = oración.split()
count = 0

for i in palabras:
    count+=1
print(count)