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

import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
from DISClib.Algorithms.Sorting import mergesort as mgs
import datetime
assert config

# Construccion de modelos

def newAnalyzer():
    analyzer = {'ufos': None, 'dateIndex': None, 'city': None}
    analyzer['ufos'] = lt.newList('ARRAY_LIST', cmpIds)
    analyzer['dateIndex'] = om.newMap(omaptype = 'RBT', comparefunction = cmpDates)
    analyzer['city'] = om.newMap(omaptype = 'RBT', comparefunction = cmpStrings)
    #analyzer['durations(sec)'] = map
    analyzer['timeIndex'] = om.newMap(omaptype = 'RBT', comparefunction = cmpDates)
    return analyzer

# Funciones para agregar informacion al catalogo

def addUFO(analyzer, ufo):
    lt.addLast(analyzer['ufos'], ufo)
    updateDateIndex(analyzer['dateIndex'], ufo)
    updateTimeIndex(analyzer['timeIndex'], ufo)
    updateCity(analyzer['city'], ufo)
    return analyzer

def updateDateIndex(map, ufo):
    ufodate = stringToDateTimeFormat(ufo['datetime']).date()
    entry = om.get(map, ufodate)
    if entry is None:
        datentry = lt.newList('ARRAY_LIST')
        om.put(map, ufodate, datentry)
    else:
        datentry = me.getValue(entry)
    lt.addLast(datentry, ufo)
    return map

def updateCity(map, ufo):
    entry = om.get(map, ufo['city'])
    if entry is None:
        datentry = lt.newList('ARRAY_LIST')
        om.put(map, ufo['city'], datentry)
    else:
        datentry = me.getValue(entry)
    lt.addLast(datentry, ufo)
    return map



def updateTimeIndex(map, ufo):
    ufotime = stringToDateTimeFormat(ufo['datetime']).time()
    entry = om.get(map, ufotime)
    if entry is None:
        datentry = lt.newList('ARRAY_LIST')
        om.put(map, ufotime, datentry)
    else:
        datentry = me.getValue(entry)
    lt.addLast(datentry, ufo)
    return map

# Funciones de consulta

def sightingsByCity(analyzer, city):
    sightings = lt.newList('ARRAY_LIST')
    pair = om.get(analyzer['city'], city)
    if pair is not None:
        sightings = me.getValue(pair)
    sightings = sortCatalogLst(sightings, lt.size(sightings), cmpDatesLst)
    return sightings

"""
def req2():
    return solucion
"""

def sightingsPerHour(analyzer, minTime, maxTime):
    sightings = lt.newList('ARRAY_LIST')
    timeRange = om.values(analyzer['timeIndex'], stringToTimeFormat(minTime).time(), stringToTimeFormat(maxTime).time())
    for time in lt.iterator(timeRange):
        time = sortCatalogLst(time, lt.size(time), cmpDatesLst)
        for sighting in lt.iterator(time):
            lt.addLast(sightings, sighting)
    return sightings

def sightingsByDateRange(analyzer, minDate, maxDate):
    sightings = lt.newList('ARRAY_LIST')
    timeRange = om.values(analyzer['dateIndex'], stringToDateFormat(minDate).date(), stringToDateFormat(maxDate).date())
    for date in lt.iterator(timeRange):
        date = sortCatalogLst(date, lt.size(date), cmpTimesLst)
        for sighting in lt.iterator(date):
            lt.addLast(sightings, sighting)
    return sightings

def ufosSize(analyzer):
    """
    Número de avistamientos
    """
    return lt.size(analyzer['ufos'])


def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer['dateIndex'])


def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer['dateIndex'])


def minKey(analyzer):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer['dateIndex'])


def maxKey(analyzer):
    """
    Llave mas grande
    """
    return om.maxKey(analyzer['dateIndex'])


# Funciones utilizadas para comparar elementos

def cmpIds(id1, id2):
    """
    Compara dos UFOS
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def cmpDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def cmpDatesLst(date1, date2):
    'Return True if Date1 < Date2'
    return stringToDateTimeFormat(date1['datetime']).date() < stringToDateTimeFormat(date2['datetime']).date()

def cmpTimesLst(date1, date2):
    'Return True if Date1 < Date2'
    return stringToDateTimeFormat(date1['datetime']).time() < stringToDateTimeFormat(date2['datetime']).time()

def cmpStrings(str1, str2):
    if str1 == str2:
        return 0
    elif str1 > str2:
        return 1
    else:
        return -1

# Funciones de ordenamiento

def sortCatalogLst(lst, size, parameter):
    sub_list = lt.subList(lst, 0, size)
    sub_list = sub_list.copy()
    sorted_list = mgs.sort(sub_list, parameter)
    return sorted_list

# Funciones Auxiliares

def stringToDateTimeFormat(stringDate):
    if stringDate == '':
        return datetime.datetime.strptime(1,1,1,1,1,1)
    else:
        return datetime.datetime.strptime(stringDate, '%Y-%m-%d %H:%M:%S')

def stringToTimeFormat(stringDate):
    if stringDate == '':
        return datetime.datetime.strptime(1,1,1,1,1,1)
    else:
        return datetime.datetime.strptime(stringDate, '%H:%M:%S')

def stringToDateFormat(stringDate):
    if stringDate == '':
        return datetime.datetime.strptime(1,1,1,1,1,1)
    else:
        return datetime.datetime.strptime(stringDate, '%Y-%m-%d')