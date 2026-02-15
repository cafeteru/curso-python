import os

DIR = 'contactos'


def app():
    crear_directorio()
    mostrar_menu()
    preguntar = True
    while preguntar:
        opcion = input("Selecciona una opción:\r\n")
        opcion = int(opcion)
        if opcion == 1:
            print("Agregar contacto")
        elif opcion == 2:
            print("Editar contacto")
        elif opcion == 3:
            print("Ver contactos")
        elif opcion == 4:
            print("Buscar contacto")
        elif opcion == 5:
            print("Eliminar contacto")
        elif opcion == 6:
            print("Salir")
            preguntar = False
        else:
            print("Opción no válida, por favor selecciona una opción del menú.")

def mostrar_menu():
    print("1. Agregar contacto")
    print("2. Editar contacto")
    print("3. Ver contactos")
    print("4. Buscar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")


def crear_directorio():
    if not os.path.exists(DIR):
        os.mkdir(DIR)
        print(f"Directorio '{DIR}' creado.")
    else:
        print(f"El directorio '{DIR}' ya existe.")


app()
