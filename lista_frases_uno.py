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
'''
from funciones_captura import limpiar_pantalla,leer_cadena

limpiar_pantalla()

#define una lista vacia
frases = []

#asi puedo agregar un elemento a una lista
frases.append("La poesía de la tierra nunca ha muerto")
frases.append("La naturaleza no hace nada incompleto ni nada en vano")


#for para recorrer una lista
print("ciclo for para obtener indice o posicion y el contenido\npero definiendo e incrementando variable 'indice'")
indice = 0
for frase in frases:
    print(f"Indice:\t{indice}\nFrase: \t{frase}")
    indice = indice +1

print("______________________________________________________________")
print("ciclo for y enumerate() para obtener indice o posicion y el contenido")
#ciclo for y enumerate('lista') para obtener indice o posicion y el contenido
for indice,frase in enumerate(frases):
    print(f"Indice:\t{indice}\nFrase: \t{frase}")

#eliminar una frase
frases.pop(0)

print("______________________________________________________________")
print("Lista elementos despues del borrado")
#Lista elementos despues del borrado
for indice,frase in enumerate(frases):
    print(f"Indice:\t{indice}\nFrase: \t{frase}")

#actualizacion de elementos de la lista
frases[0] = "Algunas personas caminan bajo la lluvia, otros simplemente se mojan"

print(f"frase modificada:\n{frases[0]}")