"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(" Bienvenido")
    print(" 1 - Iniciar el catalogo. ")
    print(" 2 - Cargar información en el catálogo")
    print(' 3 - Req.1 --> Reproducciones basadas en una caracteristica dentro de un rango especifico.')
    print(' 4 - Req.2 --> Pistas recomendadas para usar en una fiesta.')
    print(' 5 - Req.3 --> Pistas recomendadas para usar mientras se estudia.')
    print(' 6 - Req.4 --> Estudiar los generos muiscales segun su Tempo.')
    print(' 7 - Req.5 --> Conocer el genero musical mas escuchado en un rango de tiempo.')
    print(" 0 - Salir.")
    print(" OJO    OJO    OJO    OJO ")
    print(" al momento de calificar el reto, la opcion 1 y 2 realizan carga de datos, pero ")
    print(" deben usar la opcion 3 para que muestre la altura y elementos de arbol, ya que ")
    print(" asi lo pense para hacerlo mas eficiente, si algo me cuentan.")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


database = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        database = controller.init()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        database = controller.loadevent(database)

    # Requerimiento 1.
    elif int(inputs[0]) == 3:
        print("\n")
        print('Caracteristicas Disponibles: ')
        print("\n")
        print(" --> Instrumentalness")
        print(" --> Acousticness")
        print(" --> Liveness")
        print(" --> Speechiness")
        print(" --> Energy")
        print(" --> Danceability")
        print(" --> Valence")
        print("\n")
        characteristic = input(' ---> Caracteristica del contenido: ')
        minvalue = input(' ---> Valor minimo de la caracteristica del contenido: ')
        maxvalue = input(' ---> Valor maximo de la caracteristica del contenido : ')
        mapRBT = controller.loadRBT(database, characteristic)
        print("\n")
        print('++++++ Req No. 1 results... ++++++')
        print(' >>> Altura del arbol: ' + str(controller.indexHeight(database)))
        print(' >>> Elementos en el arbol: ' + str(controller.indexSize(database)))



    
    # Requerimiento 2.
    elif int(inputs[0]) == 3:
        print("\n")
        minvalue_energy = input('  --> Valor mínimo de la característica Energy: ')
        maxvalue_energy = input('  --> Valor máximo de la característica Energy: ')
        minvalue_dance = input('  --> Valor mínimo de la característica Danceability: ')
        maxvalue_dance = input('  --> Valor máximo de la característica Danceability: ')
        pass

    # Requerimiento 3.
    elif int(inputs[0]) == 4:
        print("\n")
        minvalue_instru = input('  --> El valor mínimo del rango para Instrumentalness.: ')
        maxvalue_instru = input('  --> El valor máximo del rango para Instrumentalness: ')
        minvalue_tempo = input('  --> El valor mínimo del rango para el Tempo: ')
        maxvalue_tempo = input('  --> El valor máximo del rango para el Tempo: ')
        pass

    # Requerimiento 4.
    elif int(inputs[0]) == 5:
        print("\n")
        name_genero = input('  --> Nombre para el nuevo genero musical: ')
        minvalue_tempo = input('  --> El valor mínimo del rango para el Tempo: ')
        maxvalue_tempo = input('  --> El valor máximo del rango para el Tempo: ')
        pass
    
    # Requerimiento 5.
    elif int(inputs[0]) == 6:
        print("\n")
        minvalue_hour = input(' --> valor mínimo de la hora del día: ')
        maxvalue_hour = input(' --> valor máximo de la hora del día: ')
        pass

    else:
        sys.exit(0)
sys.exit(0)


