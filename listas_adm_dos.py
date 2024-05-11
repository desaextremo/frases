'''
Una lista es una colección ordenada y mutable de elementos. 
Las listas pueden contener cualquier tipo de dato y pueden modificarse agregando, eliminando o modificando elementos.


append: agregar un elemento al final
remove: eliminar un elemento
actualizacion: nombrelista[indice] = valor

1   Crear menu de opciones
2   implementar ciclo para presentar menu de opciones
3   implementar funciones para cada opcion
4   Leer y escribir el contenido de la lista a un archivo
'''
from funciones_captura import *

def agregar_frase(frase):
    '''Solicita al usuario ingresar una cadena de caracteres.
    
    Parámetros:
        mensaje (str): Texto de la frase que se quiere agregar a la lista.
        
    Retorna:
        n/a
    '''
    frases.append(f"{frase}\n")
def listar_frases():
    '''Retorna una acadena de caracteres con el contenido de la lista
    parametros: n/a
    Retorno:
        str: La cadena de caracteres con el contenido de la lista    '''
    listado = "Lista de frases\n"
    for indice,frase in enumerate(frases):
        listado = listado + f"{indice} {frase}"

    return listado

def actualizar_frase(indice,frase):
    '''Actualiza el contenido o valor en una posicion de la lista.
    
    Parámetros:
        indice (int): Posicion o indice de la lista a modificar.
        frase (str): Texto de la frase a modificar.
        
    Retorna:
        n/a
    '''
    frases[indice] = frase

def eliminar_frase(indice):
    '''Elimina el contenido o valor en una posicion de la lista.
    
    Parámetros:
        indice (int): Posicion o indice de la lista a modificar.
        
    Retorna:
        n/a
    '''
    frases.pop(indice)

def abrir_archivo():
    '''
        Abre el archivo frases.txt en modo lectura, obtiene el contenido y lo carga en una lista
        Parámetros:
        n/a
        
        Retorna:
        lista (list): Lista con el contenido del archivo(frases)
    '''
    #Abro el archivo de frases
    nombre_archivo = "frases.txt"
    archivo = open(nombre_archivo,"r",encoding="utf8")
    lista = archivo.readlines()
    archivo.close()

    return lista
    
def guardar_archivo():
    '''
        Abre el archivo frases.txt en modo escritura, recorre la lista frase a frase
        y va escribiendo cada frase en el archivo
        Parámetros:
        n/a
        
        Retorna:
        n/a
    '''
    #abre el archivo modo escritura
    #Abro el archivo de frases
    nombre_archivo = "frases.txt"
    with open(nombre_archivo,"w",encoding="utf8") as archivo:

        #recorre la lista y va escribiendo cada frase en el archivo
        for frase in frases:
            #escribe cada una de las frases en el archivo
            archivo.write(f"{frase}")



#retona el contenido del archivo como una lista
frases = abrir_archivo()
#definir una lista vacia


#1 menu de opciones
menu = '''Frases celebres
1   Agregar frase
2   Actualizar frase
3   Eliminar frase
4   Listar frases
5   Salir
Selecciona un opción?\t'''

while(True):
    limpiar_pantalla()
    #capturar la eleccion del usuario
    opcion = presenta_menu(menu,1,5)
    #3   implementar funciones para cada opcion

    #1   Agregar frase
    if(opcion==1):
        limpiar_pantalla()
        print("1   Agregar frase")
        frase = leer_cadena("Ingresa el texto de la frase\t🗒️","Debes ingresar el texto de la frase...🛑")
        agregar_frase(frase)
        print(f"Frase:\n{frase}\nAdicionada correctamente...")
        tiempo_espera(2)
    #2   Actualizar frase
    elif(opcion==2):
        limpiar_pantalla()
        print("2   Actualizar frase")

        listado = listar_frases() + "\nIngresa el indice o posición a modificar\t"
        indice = leer_entero(listado,"Debes ingresar el inidice o posición...🛑")
        frase = leer_cadena("Ingresa el texto de la frase\t","Debes ingrear el texto para modificar la frase...🛑")
        actualizar_frase(indice,frase)
        print(f"Frase:\n{frase}\nActualizada correctamente...")
        tiempo_espera(2)
    #3   Eliminar frase
    elif(opcion==3):
        limpiar_pantalla()
        print("3   Eliminar frase")
        listado = listar_frases() + "\nIngresa el indice o posición a eliminar\t"
        indice = leer_entero(listado,"Debes ingresar el inidice o posición...🛑")
        eliminar_frase(indice)
        print(f"Frase:\n{frase}\nEliminada correctamente...")

        tiempo_espera(2)
    #4   Listar frases
    elif(opcion==4):
        limpiar_pantalla()
        print("4   Listar frases")
        print(listar_frases())
        tiempo_espera(2)
    #terminar    
    elif(opcion==5):
        limpiar_pantalla()
        print("5   Terminar")
        guardar_archivo()
        print("Archivo actualizado correctamente...")
        tiempo_espera(2)
        break

print("Hasta la vista baby☠️")