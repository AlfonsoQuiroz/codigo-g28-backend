"""
Enunciado: Pide 6 notas al usuario, guardalas en una lista y calcula el promedio.
"""

notas = []

for i in range(6):
    nota = float(input(f"Ingrese la nota del usuario {i+1}: "))
    notas.append(nota)

#promedio
promedio= sum(notas) / len(notas)

print(f"El promedio final es: {promedio}")