# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".

    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    resultado = requests.get(url)
    registros = resultado.json()
   
    users_x=[] #Lista de datos en X
    data_y=[]  # Lista de datos en Y
    completados=0
    idusuario=1
    
    for x in registros:
        if(int(x['userId']) == idusuario):  # Para los userId iguales
            completed = bool(x['completed'])  
            if(completed):
                completados+=1 # Cuento los completados
        else:
            users_x.append(idusuario) #agrego a la lista de eje x
            data_y.append(completados) #agrego a la lista de eje y
            idusuario= int(x['userId'])
            completados=0
            completed = bool(x['completed']) 
            if(completed):
                completados+=1 
         
    users_x.append(idusuario) # Agrego a la lista de x el ultimo userId
    data_y.append(completados)  # Agrego a la lista de y el ultimo contador de completados  
    
    print("Tabla de Datos")                
    print("X =", users_x)
    print("Y =", data_y)
    
### Gráfico ###
    fig = plt.figure()
    fig.suptitle('Libros completados por usuario', fontsize=14)
    ax = fig.add_subplot()
    ax.bar(users_x, data_y, color='green', label='Libros Leidos')
    ax.set_facecolor('navajowhite')
    ax.set_xlabel("ID Usuario")
    ax.set_ylabel("Completados")
    ax.grid(True, linestyle='--', color='grey')
    ax.legend()
    plt.xticks(users_x)
    plt.show()    
    
    print("terminamos")