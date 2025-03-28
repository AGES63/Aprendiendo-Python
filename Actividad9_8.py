#Función para conversión de temperatura 

def convertir_celsius_a_fahrenheit(temperatura):
    fahren = temperatura*(9/5) + 32
    return fahren


tempF = int(input("Ingrese la temperatura en grados Celsius: "))
print(convertir_celsius_a_fahrenheit(tempF))


def convertir_fahrenheit_a_celsius(temperatura):
    celsius = (temperatura-32)*(5/9)
    return celsius

tempC = int(input("Ingrese la temperatura en grados Fahrenheit: "))
print(convertir_fahrenheit_a_celsius(tempC))

