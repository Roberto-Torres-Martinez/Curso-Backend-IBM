#Crear un archivo
nombre_archivo = 'mi_archivo.txt'

#Bloque with cierra automaticamente cualquier recurso abierto en este bloque

with open(nombre_archivo, 'w') as archivo:
    archivo = open(nombre_archivo, 'w')
    archivo.write('Escribiendo en el archivo\n')
    archivo.write('Agregando informacion al archivo\n')

print(f'Se creó el archivo: {nombre_archivo}')