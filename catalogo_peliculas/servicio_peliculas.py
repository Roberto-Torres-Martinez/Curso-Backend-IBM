import os

class ServicioPeliculas:
    # nombre_archivo = 'peliculas.txt'
    
    def __init__(self):
        self.nombre_archivo = 'peliculas.txt'
    #     self.peliculas = []
        
    #     if os.path.isfile(self.nombre_archivo):
    #         self.peliculas = self.obtener_peliculas()
    #     else:
    #         self.cargar_peliculas_iniciales()
    
    # def cargar_peliculas_iniciales(self):
    #     peliculas_iniciales = [
    #         Pelicula('Gladiator'),
    #         Pelicula('El Padrino'),
    #         Pelicula('La Lista De Schindler')
    #     ]
    #     self.peliculas.extend(peliculas_iniciales)
    #     self.guardar_peliculas_archivo(peliculas_iniciales)
        
    def agregar_pelicula(self, pelicula):
        with open(self.nombre_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
    
    def listar_peliculas(self):
            with open(self.nombre_archivo, 'r', encoding='utf8') as archivo:
                print('---Listado de Peliculas---')
                print(archivo.read())
            
    def eliminar_archivo_peliculas(self):
        os.remove(self.nombre_archivo)
        print(f'Archivo eliminado: {self.nombre_archivo}')
            
    
        