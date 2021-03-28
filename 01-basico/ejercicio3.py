"""
Ejercicio 3: Escribir los cuadrados de los 60 primero números naturales
 - Resolverlo con for y while
"""

contador = 1
while contador <= 60:
    resultado = contador * contador
    print(f"El cuadrado de {contador} es {resultado} usando while")
    contador += 1

contador = 1
for contador in range(61):
    resultado = contador * contador
    print(f"El cuadrado de {contador} es {resultado} usando for")
