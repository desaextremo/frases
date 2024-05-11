'''
1 Define una lista vacia
2 crea un menu de opciones para adm la lista
  1 Crear frase
  2 Actualizar frase
  3 Eliminar frase
  4 Salir
3 Implementar funciones para adm la lista

append(elemento): Agrega un elemento al final de la lista.
remove(valor): Elimina la primera aparición del valor especificado.
pop([índice]): Elimina y devuelve el elemento en la posición especificada (o el 
                 último si no se especifica ninguna posición).
• index(valor): Devuelve el índice de la primera aparición del valor especificado.
• count(valor): Devuelve el número de veces que aparece un valor en la lista.

4 Usar archivos para almacenar la información de la lista

open:abrir un archivo, r: modo lectura
                       w:modo escritura
'''
from funciones_captura import *


def ingresar_frase(frases):
    """
    Permite agregar una frase al listado de frases.
    
    Parámetros:
        frases (list): Recibe como parametro el nombre de la lista    
    Retorna: No retorna valor
    """
    frase = leer_cadena("Ingresa la frase:","Debes ingresar una frase...🛑")
    frases.append(frase)

def listar_frases(frases):
    """
    Imprime el contenido de la lista de frases
    
    Parámetros:
        frases (list): Recibe como parametro el nombre de la lista    
    Retorna: 
    str: La cadena de caracteres con el contenido de la lista.
    """
    listado="Listado de frases\n"
    #ciclo for y enumerate('lista') para obtener indice o posicion y el contenido
    for indice,frase in enumerate(frases):
        listado=listado + f"Indice: {indice} \t Frase: {frase}\n"

    return listado

# Nombre del archivo de texto
nombre_archivo = "frases.txt"

#abro mi archivo de solo lectura
archivo = open(nombre_archivo, "r",encoding="utf8")

#leo los datos del archivo y creo una lista
frases = archivo.readlines()
#cierro el archivo
archivo.close()

#2  menu de opciones
menu ='''Frases Celebres\n
1 Crear frase
2 Actualizar frase
3 Eliminar frase
4 Listar Frases
5 Salir
Selecciona una opción:\t'''

while(True):
    limpiar_pantalla()
    opcion = presenta_menu(menu,1,5)

    #validar eleccion del usuario

    #1 Crear frase
    if (opcion==1):
        limpiar_pantalla()
        print("Ingresar una frase\n")
        ingresar_frase(frases)
        print(listar_frases(frases))
        tiempo_espera(2)
    #2 Actualizar frase
    elif (opcion==2):
        limpiar_pantalla()
        print("Actualizar una frase\n")
        listado = listar_frases(frases) + "\nSelecciona la posisción de la frase que quieres modificar?\t"
        #solicita la posicion de la frase a modificar
        indice=leer_entero(listado,"Debes seleccionar la posición de la frase que quieres  modificar")
        #solicita el nuevo texto para la frase modificar
        texto_frase = leer_cadena(f"Ingresa el texto para la frase en la posicion {indice}\t",
                                  f"Debes ingresar el texto para la frase en la posición {indice}\t")
        #modifica el texto de la frase
        frases[indice] = texto_frase

        print(listar_frases(frases))
        tiempo_espera(2)
    #3 Eliminar frase
    elif (opcion==3):
        limpiar_pantalla()
        listado = listar_frases(frases) + "\nSelecciona la posisción de la frase que quieres eliminar?\t"
        #solicita la posicion de la frase a modificar
        indice=leer_entero(listado,"Debes seleccionar la posición de la frase que quieres eliminar")

        frases.pop(indice)
        print(listar_frases(frases))
        tiempo_espera(2)
    #4 Listar frases
    elif (opcion==4):
        limpiar_pantalla()
        print(listar_frases(frases))
        tiempo_espera(2)
    #5 Salir
    elif (opcion==5):
        limpiar_pantalla()
        print("Seleccionaste salir...")

        #abre el archivo de frases.txt en modo escritura
        with open(nombre_archivo,"w",encoding="utf8") as archivo:
            #recorro el listado de fases y voy escribiendo cada una en el archivo
            for frase in frases:
                #escribo en el archivo
                archivo.write(f"{frase}")

        print("Se ha registrado la información en el archivo de frases...")
        break

print("hasta la vista Baby...☠️")





