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

#-----------------------------------
#Ruta a los archivos
#-----------------------------------
#context_content_features-small.csv
songFile = 'context_content_features-small.csv'
cont = None
#-----------------------------------
#Menu
#-----------------------------------
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Requerimiento 1")
    print("3 - Informacion del arbol")
    print("4- Música para festejar")
    print("5- Música para estudiar")
    print("6- Canciones y artistas por géneros")
    print("7- Género más escuchado en un tiempo")
    print("Presione cualquier otra tecla para salir")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        cont = controller.init()
        controller.loadData(cont, songFile)
        print("Cargando información de los archivos ....")
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))

    elif int(inputs[0]) == 2:
        print("buscando artistas en un rango de instrumentalness")
        initialInstru = float(input("limite inferior: "))
        finalInstru = float(input("limite superior: "))
        print(finalInstru)
        retorno = controller.Requerimiento1(cont, initialInstru, finalInstru)
        print('numero de artistas: ', retorno[0], '   \nnumero de visualizaciones: ', retorno[1])
    elif int(inputs[0]) == 3:
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))        
    else:
        sys.exit(0)
sys.exit(0)
