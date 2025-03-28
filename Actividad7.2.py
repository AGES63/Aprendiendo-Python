#Código para notas de estudiantes

cal = []

notas = {}

m = int(input("Ingrese la cantidad de alumnos a ingresar sus notas: "))

for i in range(0,m):
    alumno = input("Ingrese el nombre del alumno: ")
    n = int(input("Ingrese la CANTIDAD de notas del alumno: "))
    for i in range(0,n):
        nota = input("Ingrese la nota del alumno: ")
        cal.append(nota)
        i+=1
    notas[alumno] = cal
    i=+1
    
print(notas)
    