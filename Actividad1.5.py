#Código para practicar

g = 9.81

caida_libre = lambda t: 0.5 * g * t**2


tiempo = float(input("Ingresa el tiempo de caída en segundos: "))
distancia = caida_libre(tiempo)

print(f"La distancia recorrida en {tiempo} segundos es {distancia:.2f} metros.")

