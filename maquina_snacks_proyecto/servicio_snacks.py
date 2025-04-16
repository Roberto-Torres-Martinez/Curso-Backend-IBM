import os.path
from snack import Snack

class ServicioSnacks:
    nombre_archivo = 'snacks.txt'
    def __init__(self):
        self.snacks = []
        # Revisar si existe el archivo de snakcs
        # Si existe obtenemos los snacks del archivo
        if os.path.isfile(self.nombre_archivo):
            self.snacks = self.obtener_snacks()
        # Si no, cargamos algunos snacks iniciales
        else:
            self.cargar_snacks_iniciales()
    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack('Patatas', 1.50),
            Snack('Refresco', 1.25),
            Snack('Sandwich', 2.50)
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)
    def guardar_snacks_archivo(self, snacks):
        try:
            with open(self.nombre_archivo, 'a') as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n')
        except Exception as e:
            print(f'Error al guardar snacks en archivo: {e}')
    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    id_snack, nombre, precio = linea.strip().split(',')
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
        except Exception as e:
            print('Error al leer archivo de snacks: {e}')
        return snacks
    def agregar_snack(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])
    def mostrar_snacks(self):
        print('---Snacks en el inventario---')
        for snack in self.snacks:
            print(snack)
    def get_snacks(self):
        return self.snacks