meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print(meses)
print(meses[0])  # Enero
print(meses[11])  # Diciembre
print(meses[-1])  # Diciembre

lenguajes = ["Python", "JavaScript", "Java", "C#", "C++"]
lenguajes.sort()
print(lenguajes)

# Obtener el último elemento de la lista, de manera inversa
aprendiendo = f'Estoy aprendiendo {lenguajes[-1]}'
print(aprendiendo)

# Modificar un elemento de la lista
lenguajes[1] = "TypeScript"
print(lenguajes)

# Agregar un nuevo lenguaje al final de la lista
lenguajes.append("Rust")
print(lenguajes)

# Eliminar un lenguaje de la lista
del lenguajes[1]
print(lenguajes)

# Eliminar el último lenguaje de la lista
lenguajes.pop()
print(lenguajes)

# Eliminar un lenguaje específico de la lista
lenguajes.remove("Java")
print(lenguajes)