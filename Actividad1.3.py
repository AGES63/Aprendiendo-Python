#Código para saber si un número es primo o no

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Prueba del código
num = int(input("Ingresa un número: "))
if es_primo(num):
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")


