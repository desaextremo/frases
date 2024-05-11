import json

# Nombre del archivo JSON
nombre_archivo = "datos.json"

# Diccionario para almacenar los datos del archivo JSON
diccionario = {}

# Abrir el archivo JSON y cargar los datos en el diccionario
with open(nombre_archivo, "r") as archivo:
    diccionario = json.load(archivo)

# Imprimir el diccionario para verificar que los datos se cargaron correctamente
print(diccionario)
print("___________________________________________")
print(f"Elemento con llave 1: {diccionario.get("1")}")