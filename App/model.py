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


from DISClib.DataStructures.arraylist import size, subList
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.ADT import orderedmap as om
from datetime import date, datetime as dtime
from DISClib.Algorithms.Trees import traversal
import datetime
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def InitCatalog():
    catalog = {'UFO_sightings': None,
                'duration_UFO': None,
                'datetime_UFO': None,
                'hour_UFO': None,
                'cities': None}
    catalog['UFO_sightings'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['duration_UFO'] = om.newMap(omaptype='RBT', comparefunction= cmpSeconds)
    catalog['datetime_UFO'] = om.newMap(omaptype='RBT', comparefunction= cmpDate)
    catalog['hour_UFO'] = om.newMap(omaptype="RBT", comparefunction= cmpHour) #Falta por agregar
    catalog['cities'] = om.newMap(omaptype="RBT")

    return catalog

# Funciones para agregar informacion al catalogo
def addUFO(catalog, ufo_event):
    lt.addLast(catalog['UFO_sightings'], ufo_event)
    updateDuration(catalog['duration_UFO'], ufo_event)
    updateDatetime(catalog['datetime_UFO'], ufo_event)
    updateHour(catalog['hour_UFO'], ufo_event)
    addCity(catalog['cities'], ufo_event)

def updateDuration(orderedmap, ufo_event):
    #EN ESTA FUNCIÓN LA VARIABLE DURATION_EVENT TOMA LA DURACIÓN EN SEGUNDOS
    duration_event = ufo_event['duration (seconds)']
    duration_entry = om.get(orderedmap, duration_event)
    if duration_entry is None:
        duration_list = lt.newList()
        lt.addLast(duration_list, ufo_event)
        om.put(orderedmap, duration_event, duration_list)
    else: 
        value_entry = me.getValue(duration_entry)
        lt.addLast(value_entry, ufo_event)
    return orderedmap

def updateDatetime(orderedmap, ufo_event):
    occurreddate = ufo_event['datetime']
    ufodate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    time_entry = om.get(orderedmap, ufodate.date())
    if time_entry is None:
        ufodate_list = lt.newList()
        lt.addLast(ufodate_list, ufo_event)
        om.put(orderedmap,ufodate.date(),ufodate_list)
    else:
        value_entry = me.getValue(time_entry)
        lt.addLast(value_entry, ufo_event)
    return orderedmap
def updateHour(orderedmap, ufo_event):
    hour_event = ufo_event['datetime']
    ufodate = datetime.datetime.strptime(hour_event, '%Y-%m-%d %H:%M:%S')
    time_entry = om.get(orderedmap, ufodate.time())
    if time_entry is None:
        ufodate_list = lt.newList()
        lt.addLast(ufodate_list, ufo_event)
        om.put(orderedmap,ufodate.time(),ufodate_list)
    else:
        value_entry = me.getValue(time_entry)
        lt.addLast(value_entry, ufo_event)
    return orderedmap
def addCity(map, ufo_event):
    city= ufo_event["city"]
    if om.contains(map,city) == False:
        lista_ciudad= lt.newList("ARRAY_LIST")
        lt.addLast(lista_ciudad,ufo_event)
        om.put(map,city,lista_ciudad)
    else:
        lista_ciudad= om.get(map,city)["value"]
        lt.addLast(lista_ciudad,ufo_event)

    return map
    
# Funciones para creacion de datos

# Funciones de consulta
def total_sightings(catalog):
    total= lt.size(catalog["UFO_sightings"])
    primeros5= lt.subList(catalog["UFO_sightings"],1,5)
    ultimos5= lt.subList(catalog["UFO_sightings"],-4,5)

    return total, primeros5, ultimos5

def datetimesize(catalog): #no
    return om.size(catalog['datetime_UFO'])

def durationsize(catalog): #no
    return om.size(catalog['duration_UFO'])

def sightings_by_city(catalog,city): 
    list_sightings_city= om.get(catalog["cities"],city)["value"]
    merge.sort(list_sightings_city,cmpByDatetime)
    primeros3= lt.subList(list_sightings_city,1,3)
    ultimos3= lt.subList(list_sightings_city,-2,3)
    
    return om.size(catalog["cities"]),lt.size(list_sightings_city),primeros3,ultimos3

def size_city_tree(catalog):
    elementos= om.size(catalog["cities"])
    altura= om.height(catalog["cities"])

    return elementos, altura
#Requerimiento 3 - Jesed Dominguez
def older_hour(orderedmap):
    dates_tree = orderedmap['hour_UFO']
    #Para que imprima la hora más tardía con el número de avistamientos
    older_hour = traversal.inorder(dates_tree)
    return older_hour
    #Para listar avistamientos dentro de horas
def hours_in_range(orderedmap, lowhour, highhour):
    dates_tree = orderedmap['hour_UFO']
    hours_sightings = lt.newList('ARRAY_LIST')
    mindate = datetime.datetime.strptime(lowhour, '%H:%M:%S')
    maxdate = datetime.datetime.strptime(highhour, '%H:%M:%S')
    mindate = mindate.time()
    maxdate = maxdate.time()
    lst_range = om.values(dates_tree,mindate,maxdate)
    for i in lt.iterator(lst_range):
        merge.sort(i,cmpByDatetime)
        for j in lt.iterator(i):
            lt.addLast(hours_sightings, j)
    return hours_sightings

#Requerimiento 4
def older_sightings(orderedmap):
    dates_tree = orderedmap['datetime_UFO']
    #Para que imprima la fecha más antigua con el número de avistamientos
    older_date = traversal.inorder(dates_tree)
    return older_date
    #Para listar avistamientos dentro de fechas
def dates_in_range(orderedmap, lowdate, highdate):
    dates_tree = orderedmap['datetime_UFO']
    mindate = datetime.datetime.strptime(lowdate, '%Y-%m-%d')
    maxdate = datetime.datetime.strptime(highdate, '%Y-%m-%d')
    mindate = mindate.date()
    maxdate = maxdate.date()
    lst_range = om.values(dates_tree,mindate,maxdate)
    sub_dates = lst_range
    Primeros = lt.subList(lst_range,1,3)
    Ultimos = lt.newList('ARRAY_LIST')
    j = 0
    while j < 3:
        last = lt.removeLast(sub_dates)
        lt.addLast(Ultimos, last)
        j += 1
    Ultimos = merge.sort(Ultimos, cmpDatetolst)
    return lst_range,Primeros,Ultimos
#Funciones generales
#Para el número de avistamientos dentro del rango
def size_in_range(lst):
    cont = lt.size(lst)
    return cont
# Funciones de comparación
def cmpByDatetime(sighting1, sighting2):
    datetime1= time.strptime(sighting1["datetime"], "%Y-%m-%d %H:%M:%S")
    datetime2= time.strptime(sighting2["datetime"], "%Y-%m-%d %H:%M:%S")
    return datetime1 < datetime2

def cmpFloats(float1, float2):
    float1 = float(float1)
    float2 = float(float2)
    if (float1 == float2):
        return 0
    elif (float1 > float2):
        return 1
    else:
        return -1

def cmpHour(hour1, hour2):
    if (hour1 == hour2):
        return 0
    elif (hour1 > hour2):
        return 1
    else:
        return -1

def cmpSeconds(duration1, duration2):
    duration1 = float(duration1)
    duration2 = float(duration2)

    if (duration1 == duration2):
        return 0
    elif (duration1 > duration2):
        return 1
    else:
        return -1

def cmpDate(ufo1, ufo2):

    if (ufo1 == ufo2):
        return 0
    elif (ufo1 > ufo2):
        return 1
    else:
        return -1

def cmpDatetolst(ufo1, ufo2):
    ufo1= time.strptime(ufo1["first"]['info']["datetime"], "%Y-%m-%d %H:%M:%S")
    ufo2= time.strptime(ufo2["first"]['info']["datetime"], "%Y-%m-%d %H:%M:%S")
    if (ufo1 == ufo2):
        return 0
    elif (ufo1 > ufo2):
        return 1
    else:
        return -1

# Funciones de ordenamiento
