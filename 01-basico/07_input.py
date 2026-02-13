nombre = input("¿Cuál es tu nombre?\n")
print(f"Hola, {nombre}!")

# Leer datos numéricos
edad = input("¿Cuántos años tienes?\n")
# Convertir la entrada a un número entero
if edad.isdigit():
    edad = int(edad)
    print(f"Tienes {edad} años.")
else:
    print("Por favor, introduce un número válido para la edad.")


preguntar = True

while preguntar:
    numero = input('Introduce un número:\n')
    if numero.isdigit():
        numero = int(numero)
        print(f'El número que has introducido es: {numero}')
    elif numero == 'salir':
        print('¡Hasta luego!')
        preguntar = False
    else:
        print('Por favor, introduce un número válido.')
