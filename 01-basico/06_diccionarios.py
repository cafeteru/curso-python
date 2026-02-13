# Un diccionario en Python es como un objeto que almacena pares de clave-valor. Es una estructura de datos muy útil para organizar información de manera eficiente. A diferencia de las listas, los diccionarios no mantienen un orden específico, pero permiten acceder a los valores mediante sus claves.
cancion = {
    "titulo": "Bohemian Rhapsody",
    "artista": "Queen",
    "album": "A Night at the Opera",
    "año": 1975,
    "genero": "Rock",
}

# Accediendo a los valores del diccionario utilizando las claves
print(cancion["titulo"])  # Imprime: Bohemian Rhapsody
print(cancion["artista"])  # Imprime: Queen
print(cancion["album"])  # Imprime: A Night at the Opera

anio = cancion['año']
print(f"El año de lanzamiento de la canción es: {anio}")

# Agregando un nuevo par clave-valor al diccionario
cancion['genero'] = "Masculino"
print(cancion)  # Imprime: Masculino

# Modificando un valor existente en el diccionario
cancion['genero'] = "Rock"
print(cancion)  # Imprime: Rock

# Eliminando un par clave-valor del diccionario
del cancion['album']
print(cancion)  # Imprime el diccionario sin la clave 'album'