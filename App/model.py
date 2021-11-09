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
    analyzer = {'ufos': None, 'dateIndex': None}
    analyzer['ufos'] = lt.newList('ARRAY_LIST', cmpIds)
    analyzer['dateIndex'] = om.newMap(omaptype='RBT', comparefunction = cmpDates)
    return analyzer


# Funciones para agregar informacion al catalogo

def addUFO(analyzer, ufo):
    lt.addLast(analyzer['ufos'], ufo)
    updateDateIndex(analyzer['dateIndex'], ufo)
    return analyzer

def updateDateIndex(map, ufo):
    ufodate = stringToDateFormat(ufo['datetime']).date()
    om.put(map, ufodate, ufo)

# Funciones para creacion de datos

# Funciones de consulta

def sightingsByCity(analyzer, city):
    sightings = lt.newList('ARRAY_LIST')
    for sighting in lt.iterator(analyzer['ufos']):
        if sighting['city'] == city:
            lt.addLast(sightings, sighting)
    sightings = sortCatalogLst(sightings, lt.size(sightings), cmpDatesLst)
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
    return stringToDateFormat(date1['datetime']).date() < stringToDateFormat(date2['datetime']).date()

# Funciones de ordenamiento

def sortCatalogLst(lst, size, parameter):
    sub_list = lt.subList(lst, 0, size)
    sub_list = sub_list.copy()
    sorted_list = mgs.sort(sub_list, parameter)
    return sorted_list 

# Funciones Auxiliares

def stringToDateFormat(stringDate):
    if stringDate == '':
        return datetime.datetime.strptime(1,1,1,1,1,1)
    else:
        return datetime.datetime.strptime(stringDate, '%Y-%m-%d %H:%M:%S')
