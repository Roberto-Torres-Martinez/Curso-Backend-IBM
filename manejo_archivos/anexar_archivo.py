print('***Anexar informacion al archivo')

nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo, 'a') as archivo:
    #Anexar informacion al archivo
    archivo.write('Anexando informacion... \n')
    archivo.write('Saliendo de anexar informacion...\n')

print('Se ha anexado informacion al archivo {nombre_archivo}')