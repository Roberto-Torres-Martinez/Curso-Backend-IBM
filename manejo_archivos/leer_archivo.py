print('***Leer archivo con python***')

nombre_archivo = 'mi_archivo.txt'

#Leer archivo usando el metodo readlines
with open(nombre_archivo, 'r') as archivo:
    #Leer todas las lineas del archivo
    #print(archivo.readlines())
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip()) #strip quita los espacios en blanco, tabuladores y saltos de linea que tengamos al inicio o al final de una cadena

#Leer el contenido del archivo usando el metodo read
print('Leyendo el contenido con el metodo read')
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read().strip())