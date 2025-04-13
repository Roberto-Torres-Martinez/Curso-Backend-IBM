print('***Manejo de Excepciones***')

def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        print(f'Resultado de la división: {resultado}')
    except ZeroDivisionError:
        print('Error: No se puede dividir entre 0')
    
dividir(10, 2)
dividir(10, 0)

def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        print(f'Resultado de la división: {resultado}')
    except ZeroDivisionError:
        print('Error: No se puede dividir entre 0')
    except TypeError:
        print('Error: Los operandos deben ser numéricos no str')
    
dividir(10, 2)
dividir(10, '0')

def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        print(f'Resultado de la división: {resultado}')
    except Exception as error:
        print(f'Ocurrio un Error: {error}')
    finally:
        print(f'Terminamos de procesar la excepción')
    
dividir(10, 2)
dividir(10, '0')