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
from DISClib.ADT import map as mp
from prettytable import PrettyTable
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")

def initCatalog():
    """
    Retorna un nuevo catálogo vacío
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los datos en el catálogo pasado por parámetro
    """
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)

        ufo_list = mp.get(catalog, "ufo_sightings")["value"]
        total_sightings = lt.size(ufo_list)

        # Filtro para imprimir los primeros y últimos 5 observaciones con sus características
        shown_sightings = lt.newList()
        first_five = lt.subList(ufo_list, 1, 5)
        last_five = lt.subList(ufo_list, total_sightings - 5, 5)
        first_iterator = lt.iterator(first_five)
        last_iterator = lt.iterator(last_five)

        for sighting in first_iterator:
            lt.addLast(shown_sightings, sighting)
        
        for sighting in last_iterator:
            lt.addLast(shown_sightings, sighting)

        shown_iterator = lt.iterator(shown_sightings)

        # Configuración de la tabla de observaciones
        sightings_table = PrettyTable()
        sightings_table.field_names = ["datetime", "city", "state", "country", "shape", "duration (seconds)", "duration (hours/min)", "comments", "date posted", "latitude", "longitude"]

        for shown_sighting in shown_iterator:

            datetime = mp.get(shown_sighting, "datetime")["value"]
            city = mp.get(shown_sighting, "city")["value"]
            state = mp.get(shown_sighting, "state")["value"]
            country = mp.get(shown_sighting, "country")["value"]
            shape = mp.get(shown_sighting, "shape")["value"]
            duration_seconds = mp.get(shown_sighting, "duration (seconds)")["value"]
            duration_hours_min = mp.get(shown_sighting, "duration (hours/min)")["value"]
            comments = mp.get(shown_sighting, "comments")["value"]
            date_posted = mp.get(shown_sighting, "date posted")["value"]
            latitude = mp.get(shown_sighting, "latitude")["value"]
            longitude = mp.get(shown_sighting, "longitude")["value"]

            sightings_table.add_row([datetime, city, state, country, shape, duration_seconds, duration_hours_min, comments, date_posted, latitude, longitude])

        # Impresión de datos
        print(f"El total de avistamientos cargados es de {total_sightings}.\n")
        print("----------------------------------------------------------")
        print("Los primeros y últimos 5 avistamientos cargados con sus características son:\n")
        print(sightings_table)


    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
