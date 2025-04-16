#Crear un archivo
nombre_archivo = 'mi_archivo.txt'

#Abrir archivo en modo escritura
archivo = open(nombre_archivo, 'w')
archivo.write('Escribiendo en el archivo\n')
archivo.write('Agregando informacion al archivo\n')
archivo.close()

print(f'Se creó el archivo: {nombre_archivo}')