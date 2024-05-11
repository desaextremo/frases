#abre el el archivo
archivo_frases = open("frases.txt", "r",encoding="utf8")

#Ler todas las frases del archivo y crea una lista
frases = archivo_frases.readlines()

#cierra el archivo
archivo_frases.close()