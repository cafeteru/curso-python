class Restaurant:
    def __init__(
            self):  # El método __init__ es un constructor que se llama automáticamente cuando se crea una instancia de la clase. Se utiliza para inicializar los atributos del objeto.
        self.nombre = None

    def agregar_restaurant(self,
                           nombre: str):  # Self es una referencia a la instancia del objeto y se pasa automáticamente cuando se llama al método
        self.nombre = nombre

    def mostrar_restaurant(self):
        print(self.nombre)


restaurant = Restaurant()
print(restaurant)
restaurant.agregar_restaurant("La Pizzería")
restaurant.mostrar_restaurant()

restaurante2 = Restaurant()
restaurante2.agregar_restaurant("La Hamburguesería")
restaurante2.mostrar_restaurant()

print(f"Nombre del restaurante 1: {restaurant.nombre}")
print(f"Nombre del restaurante 2: {restaurante2.nombre}")
