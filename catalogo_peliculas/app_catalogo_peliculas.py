from servicio_peliculas import ServicioPeliculas
from pelicula import Pelicula

class AppCatalogoPeliculas:
    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()
        
    def mostrar_menu(self):
        print('**Catalogo de Peliculas***')
        while True:
            try:
                print('''
                      1. Agregar Película
                      2. Listar Películas
                      3. Eliminar Catálogo de Películas
                      4. Salir''')
                opcion = int(input('Escribe tu Opción (1-4): '))
                if opcion == 1:
                    nombre_pelicula = input('Escribe el Nombre de la Película: ')
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print('Saliste del Menú')
                    break
                else:
                    print('Opción Inválida, Introduce una Opción Entre 1 y 4.')
            except ValueError:
                print('Error: Introduce un número válido')
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
                
if __name__ == '__main__':
    app = AppCatalogoPeliculas()
    app.mostrar_menu()