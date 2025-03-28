#Código para diccionario de precios de productos

productos = {}

m = int(input("Ingrese la cantidad de productos a agregar: "))

for i in range(0,m):
    producto = input("Ingrese el producto: ")
    precio = input("Ingrese el precio: ")
    productos[producto] = precio
    i=+1
   
    
precio_buscar = input("Ingrese el producto a buscar su precio: ")
print(productos[precio_buscar])