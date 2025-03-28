#Función para promedio de lista de números


def calc_prom(lista):
    promedio = sum(lista)//len(lista)
    return promedio

Lista = [40, 40, 40, 40]

print(calc_prom(Lista))