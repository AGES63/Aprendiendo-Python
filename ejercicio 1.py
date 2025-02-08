#promedio de duración
cursos_min = 2.5
cursos_max = 7
promedio_cursos = 4
curso_de_dalto= 1.5

diferencia_min = 100 - curso_de_dalto / cursos_min * 100
diferencia_max = 100 - curso_de_dalto / cursos_max * 100
diferencia_promedio = 100 - curso_de_dalto / promedio_cursos * 100
diferencia_max = round(diferencia_max, 2)

print(f"El curso de dalto dura un {diferencia_min}% menos que otros cursos")
print(f"El curso de dalto dura un {diferencia_max}% menos que otros cursos")
print(f"El curso de dalto dura un {diferencia_promedio}% menos que otros cursos")
