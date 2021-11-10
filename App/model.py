"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import datetime
import config as cf
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.ADT import list as lt 
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as omap
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def CreateCatalog():
    """ Se crea el catálogo con toda la información en sus respectivas Estructuras

    Returns:
        dict: El catálogo se implementa como un diccionario 
    """
    catalog = {"sightings":None,"cities":None,"dates":None} #Se crea el catalogo. Diccionario con parejas llave-valor
    catalog["dates"] = omap.newMap(omaptype="RBT", comparefunction=cmpDateDefault) #Se crea un nuevo mapa dentro de la llave de dates
    catalog["datesByHour"] = omap.newMap(omaptype="RBT", comparefunction=cmpDateDefault) #Se crea un nuevo mapa dentro de la llave de dates
    catalog["cities"] = omap.newMap(omaptype="RBT") #Se crea un nuevo mapa dentro de la llave de ciudades
    catalog["coordinates"] = omap.newMap(omaptype="RBT") # Se crea un nuevo mapa para almacenar las coordenadas geográficas
    return catalog

# Funciones para agregar informacion al catalogo

def addCity(catalog, sighting): #Se crea la función, entra el catalogo y el avistamiento
    """ Agrega una ciudad al mapa de cities en donde la llave es el nombre de la ciudad

    Args:
        catalog (dict): catálogo con la información de los mapas
        sighting (str): cada avistamiento en forma de línea del csv
    """
    city = sighting["city"]
    if not omap.contains(catalog["cities"], city): #Se observa si en el mapa está la ciudad 
        sighting_list = lt.newList("ARRAY_LIST") #Se crea una lista vacía si no existe esa llave
        lt.addLast(sighting_list, sighting) #Se añade toda la información del avistamiento a la lista
        omap.put(catalog["cities"], city, sighting_list) #Se agrega en el mapa la lista
    else:
        sighting_list = me.getValue(omap.get(catalog["cities"], city)) #Se saca la lista que contiene la ciudad
        lt.addLast(sighting_list, sighting) #Se añade la información de dicho avistamiento

def addDates(catalog, sighting): #Se crea la función, entra el catalogo y el avistamiento
    """ Agrega las fechas al mapa de dates en donde la llave es la fecha de avistamiento en formato Y-M-D

    Args:
        catalog (dict): catálogo con la información de los mapas
        sighting (str): cada avistamiento en forma de línea del csv
    """
    sighting_YMD = sighting["datetime"].split()[0]
    sighting_date = datetime.datetime.strptime(sighting_YMD, '%Y-%m-%d') #Se convierte el formato de la fecha
    if not omap.contains(catalog["dates"], sighting_date): #Se observa si en el mapa está la fecha de lo contrario
        sighting_list = lt.newList("ARRAY_LIST") #Se crea una lista vacía si no existe esa llave
        lt.addLast(sighting_list, sighting) #Se añade toda la información del avistamiento a la lista
        omap.put(catalog["dates"], sighting_date, sighting_list) #Se agrega en el mapa la lista
    else:
        sighting_list = me.getValue(omap.get(catalog["dates"], sighting_date)) #Se saca la lista que contiene la fecha de avistamiento
        lt.addLast(sighting_list, sighting) #Se añade la información de dicho avistamiento

def addDatesByHour(catalog, sighting): #Se crea la función, entra el catalogo y el avistamiento
    """ Agrega las fechas al mapa de dates en donde la llave es la fecha de avistamiento en formato H-M-S

    Args:
        catalog (dict): catálogo con la información de los mapas
        sighting (str): cada avistamiento en forma de línea del csv
    """
    sighting_HMS = sighting["datetime"].split()[1]
    sighting_date = datetime.datetime.strptime(sighting_HMS, '%H:%M:%S') #Se convierte el formato de la fecha
    if not omap.contains(catalog["datesByHour"], sighting_date): #Se observa si en el mapa está la fecha de lo contrario
        sighting_list = lt.newList("ARRAY_LIST") #Se crea una lista vacía si no existe esa llave
        lt.addLast(sighting_list, sighting) #Se añade toda la información del avistamiento a la lista
        omap.put(catalog["datesByHour"], sighting_date, sighting_list) #Se agrega en el mapa la lista
    else:
        sighting_list = me.getValue(omap.get(catalog["datesByHour"], sighting_date)) #Se saca la lista que contiene la fecha de avistamiento
        lt.addLast(sighting_list, sighting) #Se añade la información de dicho avistamiento

def addCoordinates(catalog, sighting):
    #breakpoint()
    longitude = float(format(float(sighting["longitude"]), '.2f'))
    latitude = float(format(float(sighting["latitude"]), '.2f'))
    if not omap.contains(catalog["coordinates"], longitude): # Si el mapa no contiene la longitud que entra por parámetro
        latitude_map = omap.newMap(omaptype="RBT")
        sighting_list = lt.newList("ARRAY_LIST") #Se crea una lista vacía si no existe la llave de longitud
        lt.addLast(sighting_list, sighting) #Se añade toda la información del avistamiento a la lista
        omap.put(latitude_map, latitude, sighting_list)
        omap.put(catalog["coordinates"], longitude, latitude_map) #Se agrega en el mapa el mapa de la latitud
    else: # En caso de que ya exista la longitud, se busca el value que es el mapa de latitudes
        latitude_map = me.getValue(omap.get(catalog["coordinates"], longitude)) #Se saca el mapa que contiene la longitud encontrada
        if not omap.contains(latitude_map, latitude): # En caso de que no exista como key la latitud en el mapa de latitudes
            sighting_list = lt.newList("ARRAY_LIST") #Se crea una lista vacía si no existe esa llave
            lt.addLast(sighting_list, sighting) #Se añade toda la información del avistamiento a la lista
            omap.put(latitude_map, latitude, sighting_list) #Se agrega en el mapa la lista
        else: # Existe la key de latitud para una longitud dada
            sighting_list = me.getValue(omap.get(latitude_map, latitude)) #Se saca la lista que contiene la fecha de avistamiento
            lt.addLast(sighting_list, sighting) #Se añade la información de dicho avistamiento

# Funciones de consulta
def largestCity(orderedmap):
    """Recorre la lista de llaves y obtiene la ciudad con mayor número de avistamientos

    Args:
        orderedmap (omap): Mapa ordenado de las ciudades del catálogo

    Returns:
        String: La ciudad con mayor cantidad de avistamientos
    """
    largest_city = lt.getElement( omap.keySet(orderedmap),1)
    largest = lt.size(me.getValue(omap.get(orderedmap, largest_city)))
    for city in lt.iterator(omap.keySet(orderedmap)):
        length = lt.size(me.getValue(omap.get(orderedmap, city)))
        if length > largest:
            largest_city = city
            largest = lt.size(me.getValue(omap.get(orderedmap, largest_city)))
    return largest_city

def oldestDate(orderedmap):
    oldest_date = omap.minKey(orderedmap)
    return oldest_date, lt.size(me.getValue(omap.get(orderedmap,oldest_date)))

def oldestDateByHour(orderedmap):
    oldest_time = omap.maxKey(orderedmap)
    return oldest_time, lt.size(me.getValue(omap.get(orderedmap,oldest_time)))

def cities(orderedmap, city):
    """Ordena los avistamientos de una ciudad indicada por el usuario
    y obtiene el número de avistamientos, y la información de los 3 primeros y últimos 3 de la lista

    Args:
        orderedmap (omap): Mapa ordenado de las ciudades
        city (str): Ciudad ingresada como input

    Returns:
        int: El tamaño de la lista, que indica el total de avistamientos para esa ciudad
        Array List: Sublista de las 3 primeras posiciones
        Array List: Sublista de las 3 últimas posiciones
    """
    sightings = me.getValue(omap.get(orderedmap, city))
    sightings_size = lt.size(sightings)
    try:
        merge.sort(sightings, cmpSightByDate)
        first_3 = lt.subList(sightings, 1,3)
        last_3 = lt.subList(sightings, (sightings_size-2), 3)
    except:
        print("No hay avistamientos suficientes.")
    return sightings_size, first_3, last_3

def dates_range(orderedmap, lowlim, upper_lim):
    """Obtiene una lista con los valores del mapa ordenado de fechas para un rango dado 

    Args:
        orderedmap (omap): Mapa ordenado de las fechas
        lowlim (str): Rango inferior para la búsqueda de fechas
        upper_lim (str): Rango superior para la búsqueda de fechas

    Returns:
        int: El tamaño de la lista, que indica el total de avistamientos en el rango dado
        Array List: Sublista de la lista de values para las 3 primeras posiciones
        Array List: Sublista de la lista de values para las 3 últimas posiciones
    """
    try:
        value_list = omap.values(orderedmap, formatDate(lowlim), formatDate(upper_lim))
        value_size = lt.size(value_list)
        first_3 = lt.subList(value_list, 1,3)
        last_3 = lt.subList(value_list, (value_size-2), 3)
    except:
        print("No hay avistamientos suficientes.")
    return value_size, first_3, last_3

def dates_rangeByHour(orderedmap, lowlim, upper_lim):
    """Obtiene una lista con los valores del mapa ordenado de fechas para un rango dado 

    Args:
        orderedmap (omap): Mapa ordenado de las fechas
        lowlim (str): Rango inferior para la búsqueda de fechas
        upper_lim (str): Rango superior para la búsqueda de fechas

    Returns:
        int: El tamaño de la lista, que indica el total de avistamientos en el rango dado
        Array List: Sublista de la lista de values para las 3 primeras posiciones
        Array List: Sublista de la lista de values para las 3 últimas posiciones
    """
    try:
        value_lists = omap.values(orderedmap, formatDateByHour(lowlim), formatDateByHour(upper_lim))
        value_size = 0
        for list in lt.iterator(value_lists):
            value_size += lt.size(list)
        first_3 = lt.subList(value_lists, 1,3)
        last_3 = lt.subList(value_lists, (lt.size(value_lists)-2), 3)
    except:
        print("No hay avistamientos suficientes.")
    return value_size, first_3, last_3

def coordinates(orderedmap,long_min, long_max, lat_min, lat_max):
    try:
        maps_list = omap.values(orderedmap, float(long_min), float(long_max)) # lista de mapas con longitudes en el rango dado
        contador = 0
        list_sights = lt.newList(datastructure="ARRAY_LIST")
        for map in lt.iterator(maps_list):
            coordinates_list = omap.values(map, float(lat_min), float(lat_max))
            if lt.size(coordinates_list) > 0:
                contador += lt.size(coordinates_list)
                lt.addLast(list_sights, coordinates_list)
    except:
        print("Error en la función coordinates: model")
    return contador, list_sights

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpSightByDate(sight1, sight2):
    """Compara las fechas de 2 avistamientos

    Args:
        sight1 ([dict]): [Información del avistamiento 1]
        sight2 ([dict]): [Información del avistamiento 2]

    Returns:
        [boolean]: [True si el avistamiento 1 es menor que el avistamiento 2]
    """
    try:
        format = "%Y-%m-%d"
        d1 = sight1["datetime"]
        d2 = sight2["datetime"]
        dt_object1 = datetime.datetime.strptime(d1, format)
        dt_object2 = datetime.datetime.strptime(d2, format)
        return (dt_object1 < dt_object2)
    except:
        print("Error en el formato de las fechas")

def cmpDateDefault(date1, date2):
    """Compara las fechas de 2 avistamientos

    Args:
        date1 ([datetime.datetime]): [Fecha del avistamiento 1]
        date2 ([datetime.datetime]): [Fecha del avistamiento 2]

    Returns:
        [int]: [Default values]
    """
    try:
        if date1 == date2:
            return 0
        elif date1 < date2:
            return -1
        else:
            return 1
    except:
        print("Error en el formato de las fechas")

def formatDate(date1):
    """Formatea una fecha de tipo string a datetime

    Args:
        date1 (str): Fecha en formato str

    Returns:
        datetime: Fecha en formato datetime
    """
    format = "%Y-%m-%d"
    return datetime.datetime.strptime(date1, format)

def formatDateByHour(date1):
    """Formatea una fecha de tipo string a datetime

    Args:
        date1 (str): Fecha en formato str

    Returns:
        datetime: Fecha en formato datetime
    """
    format = "%H:%M"
    return datetime.datetime.strptime(date1, format)
# Funciones de ordenamiento
