import random

def selecciona_frase(frases):
    return random.choice(frases)

frases = ["La poesía de la tierra nunca ha muerto",
          "La naturaleza no hace nada incompleto ni nada en vano",
          "El buen hombre es el amigo de todos los seres vivos",
          "Los árboles que tardan en crecer llevan la mejor fruta",
          "La naturaleza sostiene la vida universal de todos los seres",
          "La creación de mil bosques está en una bellota",
          "Estudia la naturaleza, ama la naturaleza, acércate a la naturaleza. Nunca te fallará",
          "Nunca la sabiduría dice una cosa y la naturaleza otra",
          "La naturaleza no es un lugar para visitar. Es el hogar",
          "Cada flor es un alma que florece en la naturaleza",
          "Prefiero tener rosas en mi mesa que diamantes en mi cuello",
          "La naturaleza siempre vela por la preservación del universo",
          "La belleza del mundo natural está en los detalles",
          "La naturaleza provee excepciones a la regla",
          "Un pájaro no canta porque tiene una respuesta, canta porque tiene una canción",
          "Verde es el color principal del mundo, y a partir del cual surge su hermosura",
          "La naturaleza es una esfera infinita cuyo centro está en todas partes y la circunferencia en ninguna",
            "En la naturaleza no hay recompensas ni castigos, hay consecuencias",
            "Entender las leyes de la naturaleza no significa que seamos inmunes a sus operaciones",
            "Hasta ahora el hombre ha estado en contra de la naturaleza; desde ahora estará en contra de su propia naturaleza",
            "En la naturaleza está la preservación del mundo",
            "Hay algo fundamentalmente incorrecto en tratar a la tierra como si fuese un negocio en liquidación",
            "Algunas personas caminan bajo la lluvia, otros simplemente se mojanLos árboles son los esfuerzos de la tierra para hablar con el cielo que escucha",
            "En todo paseo con la naturaleza uno recibe mucho más de lo que busca",
            "Siempre he considerado la naturaleza como la ropa de Dios",
            "El agua y la tierra, los dos fluidos esenciales de los que depende la vida, se han convertido en latas globales de basura",
            "Podrán cortar todas las flores, pero no podrán detener la primavera",
            "Venimos hace muchísimos años intentando llamar la atención a la humanidad, de que no es posible la humanidad si no tenemos una nueva relación con la Madre Naturaleza",
            "El que nos encontremos tan a gusto en plena naturaleza proviene de que ésta no tiene opinión sobre nosotros",
            "Mantén tu amor hacia la naturaleza, porque es la verdadera forma de entender el arte",
            "Las tierras pertenecen a sus dueños, pero el paisaje es de quien sabe apreciarlo",
            "Si sirves a la Naturaleza, ella te servirá a ti"]

print(f"Tengo {len(frases)} frases sobre ecología y medio ambiente...")

'''
for frase in frases:
    print(f"{frase}")
'''

print("_____________________________________________________________________________")
#selecciona una frase aleatoria

#print(selecciona_frase(frases))

# Nombre del archivo de texto
nombre_archivo = "frases.txt"

# Abre el archivo en modo de escritura y escribe cada frase en una línea
with open(nombre_archivo, "w",encoding="utf8") as archivo:
    for frase in frases:
        archivo.write(f"{frase}\n")

print(f"Las frases han sido escritas en el archivo '{nombre_archivo}' correctamente.")