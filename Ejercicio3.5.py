#Código para obtener promedio



lista = []

while True:
    elemento = input("Ingrese un elemento (o escriba 'salir' para terminar): ")
    if type(elemento) == str:
        break
    lista.append(elemento)
    
def obtener_promedio(lista):
    if not lista:
        return None
    return sum(lista)/len(lista)
    


print(obtener_promedio(lista))  