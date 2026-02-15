import os

nombre_fichero = "archivo.txt"

def crear_fichero():
    archivo = open(nombre_fichero, "w")  # w = write, r = read, a = append
    archivo.write("Hola, este es un archivo de texto.\n")

    for i in range(20):
        archivo.write(f"Línea {i + 1}\n")

    archivo.close()  # Siempre es importante cerrar el archivo después de usarlo


def leer_fichero():
    archivo = open(nombre_fichero, "r")
    contenido = archivo.read()  # Lee todo el contenido del archivo
    print(contenido)
    archivo.close()


def borrar_fichero():
    if os.path.exists(nombre_fichero):
        os.remove(nombre_fichero)
        print("Archivo borrado.")
    else:
        print("El archivo no existe.")


crear_fichero()
leer_fichero()
borrar_fichero()
