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
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as merge
from prettytable import PrettyTable
assert cf
import datetime
import time

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo.")
    print("2- Requerimiento 1 (Grupal): Contar los avistamientos en una ciudad.")
    print("3- Requerimiento 2 (Individual): Contar los avistamientos por duración.")
    print("4- Requerimiento 3 (Individual): Contar avistamientos por Hora/Minutos del día.")

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

            datetimes = mp.get(shown_sighting, "datetime")["value"]
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

            sightings_table.add_row([datetimes, city, state, country, shape, duration_seconds, duration_hours_min, comments, date_posted, latitude, longitude])

        # Impresión de datos
        print(f"El total de avistamientos cargados es de {total_sightings}.\n")
        print("----------------------------------------------------------")
        print("Los primeros y últimos 5 avistamientos cargados con sus características son:\n")
        print(sightings_table)


    elif int(inputs[0]) == 2:

        city= input("Digite la ciudad a consultar: ")
        print()
        respuestas= controller.contar_avistamientos(catalog, city)
        llaves= lt.getElement(respuestas, 4)
        mapa= lt.getElement(respuestas, 3)
        avistamientos_ciudad= lt.getElement(respuestas, 2)
        total_avistamientos= lt.getElement(respuestas, 1)
        print('===================== Req No. 1 Inputs =====================\n')
        print(f"UFO Sightings in the city of: " + city)
        print("\n===================== Req No. 1 Answer =====================")
        print("There are " + str(total_avistamientos) + " different cities with UFO sightings.")
        print("There are " + str(avistamientos_ciudad) + " sightings at: " + city)
        print("the first 3 and the last 3 UFO sightings are:")
        x= 1
        y= 2
        while x <= 3:
            llave= lt.getElement(llaves, x)
            print("=======================================================")
            print("Datetime: " + str (mp.get(om.get(mapa, llave)["value"], "datetime")["value"]))
            print("City: " + str(mp.get(om.get(mapa, llave)["value"], "city")["value"]))
            print("State: " + str(mp.get(om.get(mapa, llave)["value"], "state")["value"]))
            print("Country: " + str(mp.get(om.get(mapa, llave)["value"], "country")["value"]))
            if mp.get(om.get(mapa, llave)["value"], "shape") != None:
                print(f"Shape: " + str(mp.get(om.get(mapa, llave)["value"], "shape")["value"]))
            else:
                print("Unknwon")
            print(f"Duration (seconds): " + str(mp.get(om.get(mapa, llave)["value"], "duration (seconds)")["value"]))
            print("=======================================================")
            x+=1
        while y >= 0:
            llave= lt.getElement(llaves, lt.size(llaves) - y)
            print("=======================================================")
            print("Datetime: " + str (mp.get(om.get(mapa, llave)["value"], "datetime")["value"]))
            print("City: " + str(mp.get(om.get(mapa, llave)["value"], "city")["value"]))
            print("State: " + str(mp.get(om.get(mapa, llave)["value"], "state")["value"]))
            print("Country: " + str(mp.get(om.get(mapa, llave)["value"], "country")["value"]))
            if mp.get(om.get(mapa, llave)["value"], "shape") != None:
                print(f"Shape: " + str(mp.get(om.get(mapa, llave)["value"], "shape")["value"]))
            else:
                print("Unknwon")
            print(f"Duration (seconds): " + str(mp.get(om.get(mapa, llave)["value"], "duration (seconds)")["value"]))
            print("=======================================================")
            y-=1
        
    elif int(inputs[0]) == 3:

        pass

    elif int(inputs[0]) == 4:

        hora_inicial= input("Digite el limite inferior en formato HH:MM\n") + ":00"
        hora_inicial= datetime.datetime.strptime(hora_inicial, "%H:%M:%S")
        hora_final= input("Digite el limite inferior en formato HH:MM\n") + ":00"
        hora_final= datetime.datetime.strptime(hora_final, "%H:%M:%S")
        start_time = time.process_time()
        respuestas= controller.contar_avistamientos_hora(catalog, hora_inicial, hora_final)
        end_time= time.process_time()
        elapsed_time_mseg = round((end_time - start_time) * 1000, 3)
        contador_rango= lt.getElement(respuestas, 1)
        mapa_tarde= lt.getElement(respuestas, 2)
        llaves1= lt.getElement(respuestas, 3)
        mapa_rango= lt.getElement(respuestas, 4)
        llaves2= lt.getElement(respuestas, 5)
        print('===================== Req No. 3 Inputs =====================\n')
        print(f"UFO sightings between {hora_inicial} and {hora_final}")
        print("\n===================== Req No. 3 Answer =====================")
        print(f"There are {om.size(mapa_tarde)} different UFO sightings times [HH:MM:SS]...")
        print("The 5 latest times in which UFOs have been sighted are: ")
        print()
        tabla= PrettyTable()
        tabla.field_names= ["Time", "Count"]
        x= 0
        for hours in lt.iterator(llaves1):      
            tabla.add_row([hours, me.getValue(om.get(mapa_tarde, hours))])  
            x+=1
            if x == 5:
                break
        print(tabla)
        print()
        print(f"There are {contador_rango} different UFO sightings between the times stipulated")
        print("The 3 first and last UFO sightings between the range stipulated are: ")
        lista_max= lt.newList(datastructure="ARRAY_LIST")
        lista_min= lt.newList(datastructure="ARRAY_LIST")
        x= 1
        while x <=3:
            lt.addLast(lista_max, lt.getElement(llaves2, x))
            x+=1
        x=0 
        while x<=2:
            lt.addLast(lista_min, lt.getElement(llaves2, lt.size(llaves2)-x))
            x+=1

        for dates in lt.iterator(lista_min):
            city= mp.get(om.get(mapa_rango, dates)["value"], "city")["value"]
            state= mp.get(om.get(mapa_rango, dates)["value"], "state")["value"]
            country= mp.get(om.get(mapa_rango, dates)["value"], "country")["value"]
            shape= mp.get(om.get(mapa_rango, dates)["value"], "shape")["value"]
            duration= mp.get(om.get(mapa_rango, dates)["value"], "duration (seconds)")["value"]
            print("========================================================")
            print(f"Datetime: {dates}")
            print(f"City: {city}")
            print(f"State: {state}")
            print(f"Country: {country}")
            print(f"Shape: {shape}")
            print(f"Duration (seconds): {duration}")
            print("========================================================")

        for dates in lt.iterator(lista_max):
            city= mp.get(om.get(mapa_rango, dates)["value"], "city")["value"]
            state= mp.get(om.get(mapa_rango, dates)["value"], "state")["value"]
            country= mp.get(om.get(mapa_rango, dates)["value"], "country")["value"]
            shape= mp.get(om.get(mapa_rango, dates)["value"], "shape")["value"]
            duration= mp.get(om.get(mapa_rango, dates)["value"], "duration (seconds)")["value"]
            print("========================================================")
            print(f"Datetime: {dates}")
            print(f"City: {city}")
            print(f"State: {state}")
            print(f"Country: {country}")
            print(f"Shape: {shape}")
            print(f"Duration (seconds): {duration}")
            print("========================================================")
        
        print()
        print(f"Elapsed time (ms): {elapsed_time_mseg}")
        print()
    else:
        sys.exit(0)
sys.exit(0)
