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
assert cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

ufosFile = 'UFOS//UFOS-utf8-small.csv'
cont = None


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():

    print("\n••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")

    print("\nBienvenido.\n")

    print("-----------------------------------------------------------------------------")

    print("\n1 - Inicializar el catalogo.\n")

    print("-----------------------------------------------------------------------------")

    print("\n2 - Cargar información en el catalogo.\n")

    print("-----------------------------------------------------------------------------")

    print("\n3 - Requerimiento 1.\n\nMostrar:\n\n•El total de ciudades donde se han presentado avistamientos.\n\n•Un top de 5 ciudades donde mas avistamientos se han presentado\nde manera descendente por criterio de cantidad.\n\n•La cantidad de avistamientos en una ciudad especifica.\n\n•Una lista de los tres avistamientos mas antiguos y los tres\nmas recientes de una ciudad en especifico.\n")

    print("-----------------------------------------------------------------------------")

    print("\n4 - Requerimiento 2.\n\nMostrar:\n\n•Un top de 5 avistamientos de duracion mas larga en segundos de manera\ndescendiente por criterio de duracion junto con el conteo de avistamientos\nque duraron este mismo tiempo.\n\nSobre una intervalo determinado de duracion en segundos,\n\n• La cantidad de avistamientos en ese intertvalo.\n\n•Una lista de los tres avistamientos mas antiguos y los tres mas\nrecientes que se encuentren en ese intervalo.\n")

    print("-----------------------------------------------------------------------------")

    print("\n5 - Requerimiento 3.\n\nMostrar:\n\n• Un top de 5 avistamientos registrados a una hora mas tardia de orden\ndescendiente y con criterio la hora regitrada junto con el conteo\nde avistamientos presentados en esta misma hora.\n\n• El conteo de avistamientos registrados en un intervalo de horas\ndeterminadas.\n\n• Una lista de los 3 avistamientos mas antiguos y de los 3 avistamientos\nmas recientes regitrados en este intervalo de tiempo.\n")

    print("-----------------------------------------------------------------------------")

    print("\nInserte cualquier otro caracter para salir de la aplicacion.\n")

    print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")

catalog = None

"""
Menu principal
"""

loop = True

while loop:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    if inputs[0] == "1":
        print("\nInicializando....")
        cont = controller.init()

    elif inputs[0] == "2":
        print("\nCargando información de crimenes ....")
        controller.loadData(cont, ufosFile)
        
        print('Total de avistamientos cargados: ' + str(controller.getCasesSize(cont)))
        print('Primeros 5 avistamientos: ')
        print('Ultimos 5 avistamientos: ')
        print(me.getValue(mp.get(cont, "cases")))

    elif inputs[0] == "3":
        city = input("Inserte la ciudad en la cual desea consultar la información.")
        print(controller.getCasesByCity(cont, city))

    elif inputs[0] == "4":
        beginSeconds = input("Inserte la fecha incial en formato AAAA-MM-DD: ")
        endSeconds = input("Inserte la fecha final en formato AAAA-MM-DD: ")
        print(controller.getCasesBetweeenSeconds(cont, beginSeconds, endSeconds))

    elif inputs[0] == "5":
        beginHour = input("Inserte la fecha incial en formato AAAA-MM-DD: ")
        endHour = input("Inserte la fecha final en formato AAAA-MM-DD: ")
        print(controller.getCasesBetweeenHours(cont, beginHour, endHour))


    else:
        print("\nSaliendo de la aplicacion...\n")
        loop = False
