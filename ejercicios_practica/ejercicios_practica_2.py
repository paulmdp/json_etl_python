# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvstock = open(archivo, 'r')
    stock = list(csv.DictReader(csvstock))
    total_tornillos = 0
    for registro in range(len(stock)):
        row = stock[registro]
        total_tornillos += int(row.get('tornillos'))    
    print('Stock total de tornillos:', total_tornillos)
     
def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvprop = open(archivo, 'r')
    prop = list(csv.DictReader(csvprop))
    deptos_2a = 0
    deptos_3a = 0
       
    for registro in range(len(prop)):
        row = prop[registro]
        try:
            if(int(row.get('ambientes'))==2):
                deptos_2a += 1
            if(int(row.get('ambientes'))==3):
                deptos_3a += 1
        except:
            print("ups! Valor vacio")
            
    print("Departamentos con 2 ambientes:", deptos_2a)
    print("Departamentos con 3 ambientes:", deptos_3a)
           
            
        
        

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
