﻿"""
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
from DISClib.ADT import orderedmap as om
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

ufosfile = 'UFOS-utf8-small.csv'
cont = None

def printMenu():
    print("\n")
    print("********************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador y Cargar información de crimenes.")
    print("2- Contar los avistamientos en una ciudad.")
    print("3- Contar los avistamientos por duración.")
    print("4- Contar avistamientos por Hora/Minutos del día.")
    print("5- Contar los avistamientos en un rango de fechas.")
    print("6- Contar los avistamientos de una Zona Geográfica.")
    print("0- Salir")
    print("********************************************")

def printReq1Results(sightingsList):
    size = lt.size(sightingsList)
    i = size
    j = 1
    print('Primeros 3: \n')
    while j < 4:
        sighting = lt.getElement(sightingsList ,j)
        print(' -Tiempo y Fecha: ' + sighting['datetime'] + ' -Ciudad: ' + sighting['city'] + ' -Estado: ' +  sighting['state'] + ' -Pais: ' + sighting['country'] + ' -Forma: ' + sighting['shape'] + ' -Duracion(s): ' + sighting['duration (seconds)'])
        j += 1
        print()
    print('Ultimos 3: \n')
    while i > size - 3:
        sighting = lt.getElement(sightingsList ,i)
        print(' -Tiempo y Fecha: ' + sighting['datetime'] + ' -Ciudad: ' + sighting['city'] + ' -Estado: ' +  sighting['state'] + ' -Pais: ' + sighting['country'] + ' -Forma: ' + sighting['shape'] + ' -Duracion(s): ' + sighting['duration (seconds)'])
        i -= 1
        print()


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        cont = controller.init()
        print("\nCargando información de UFOS ....")
        controller.loadData(cont, ufosfile)
        print('Avistamientos cargados: ' + str(controller.ufosSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))

    elif int(inputs[0]) == 2:
        ciudad = input('Avistamientos de OVNIS en la ciudad de: ')
        sightingsByCity = controller.sightingsByCity(cont, ciudad)
        printReq1Results(sightingsByCity)

    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass
    else:
        sys.exit(0)
sys.exit(0)
