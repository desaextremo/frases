'''
Este programa crea 50 datos ficticios usando el paquete faker  y los
va ingresando en un diccionario mediante un ciclo for.

valida previamente si tienes el paquete faker instalado.

Si no tienes faker instalado, utiliza:

pip install faker
'''

from faker import Faker
import random
import json

# Inicializamos Faker
faker = Faker()

# Diccionario para almacenar los objetos generados
diccionario = {}

# Generamos 50 objetos con datos aleatorios
for i in range(1,51):
    objeto = {
        "id":i,
        "nombres": faker.first_name(),
        "apellidos": faker.last_name(),
        "direccion": faker.street_address(),
        "movil": faker.phone_number(),
        "email": faker.email(),
        "sexo": random.choice(["M", "F"])  # Seleccionamos aleatoriamente entre "M" y "F" para el sexo
    }
    diccionario[i] = objeto

print(f"Elemento con llave 1: {diccionario.get(1)}")

# Imprimimos el diccionario
for key, value in diccionario.items():
    print(key, value)

# Nombre del archivo JSON de salida
nombre_archivo = "datos.json"

# Escribir el diccionario en el archivo JSON

with open(nombre_archivo, "w") as archivo:
    json.dump(diccionario, archivo, indent=4)

'''
# Escribir manualmente el JSON en el archivo
with open(nombre_archivo, "w") as archivo:
    #escribir el corchete llave de inicio { del diccionario
    archivo.write("{\n")
    #para cada uno de los datos del diccionario leer sus claves y valores
    #y escribir en el archivo
    for key, value in diccionario.items():
        archivo.write(f"    {key}: {json.dumps(value, indent=4)},\n")
    
    #escribir el corchete llave de cierre } del diccionario
    archivo.write("}\n")
'''
print(f"El archivo JSON '{nombre_archivo}' ha sido creado correctamente.")