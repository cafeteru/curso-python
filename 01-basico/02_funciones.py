def metodo_sin_argumentos():
   print("Soy Iván")

def metodo_con_argumentos(nombre: str, edad: int = 18):
    print(f"Hola soy {nombre}")
    print(f"y tengo {edad}")

def metodo_con_return(nombre: str) -> str:
    return nombre.upper()

metodo_sin_argumentos()
metodo_con_argumentos("Iván", 22)
metodo_con_argumentos("Defecto")
retorno = metodo_con_return("Retorno")
print(retorno)