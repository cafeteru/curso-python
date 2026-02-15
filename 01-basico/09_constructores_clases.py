class Restaurant:
    def __init__(self, nombre: str, categoria: str, precio: float):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio

    def mostrar_restaurant(self):
        print(f"El restaurante {self.nombre} es de categoría {self.categoria}.")
        print(f"El precio promedio es de {self.__precio} dólares.")


restaurant = Restaurant("La Pizzería", "Comida Italiana", 20)
restaurant2 = Restaurant("La Hamburguesería", "Comida Rápida", 15)
restaurant.mostrar_restaurant()
restaurant2.mostrar_restaurant()
