class Restaurant():
    def __init__(self, nombre: str, categoria: str, precio: float):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio

    def mostrar_restaurant(self):
        print(f"El restaurante {self.nombre} es de categoría {self.categoria}.")
        print(f"El precio promedio es de {self.__precio} dólares.")

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            print("El precio no puede ser negativo.")
        else:
            self.__precio = nuevo_precio

class Hotel(Restaurant): # La clase Hotel hereda de Restaurant
    def __init__(self, nombre: str, categoria: str, precio: float, estrellas: int):
        super().__init__(nombre, categoria, precio)
        self.estrellas = estrellas

    def mostrar_hotel(self):
        self.mostrar_restaurant()
        print(f"El hotel tiene {self.estrellas} estrellas.")

hotel = Hotel("Hotel Playa", "Hotel de Playa", 100, 4)
hotel.mostrar_hotel()