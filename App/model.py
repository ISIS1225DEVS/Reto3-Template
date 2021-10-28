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


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def initCatalog():
    catalog = {'avistamiento': None,'dateIndex': None}

    catalog['avistamiento'] = lt.newList('SINGLE_LINKED', compare)
    catalog['dateIndex'] = om.newMap(omaptype='BST', comparefunction=compare)
    catalog['City']=om.newMap(omaptype='BST',comparefunction=compare)
    return catalog

# Funciones para agregar informacion al catalogo
def AddAvist(catalog, avistamiento):
    lt.addLast(catalog['avistamiento'], avistamiento)
    City  = avistamiento['City']
    State = om.contains(catalog['City'], City)
    if not State:
        Ltcity = lt.newList()
        lt.addLast(listaCiudad, avistamiento)
        om.put(catalog['City'],City,Ltcity)
    else:
        Ltcity = om.get(catalog['City'], City)['value']
        lt.addLast(Ltcity, avistamiento)
        om.put(catalog['City'], City, Ltcity)

# Funciones para creacion de datos

# Funciones de consulta
def avistCiudad(catalog, City):
    NumberOfcities=0
    NumberAvistCiudad=0
    cityLt= lt.newList()
    for City  in lt.iterator(catalog['City']):
        NumberOfcities+=1
        if catalog['City'] == City:
            for i in catalog['City']:
                NumberAvistCiudad+= 1
                Dat =lt.newList()
                lt.addLast(Dat, i['Datetime'])
                lt.addLast(Dat, i['City'])
                lt.addLast(Dat, i['Country'])
                lt.addLast(Dat, i['Duration'])
                lt.addLast(Dat, i['Shape'])
                lt.addLast(cityLt, Dat)
    return cityLt


def ltDates(cityLt):
    ltDates= lt.newList()
    for i in ltDates:
        lt.addLast(ltDates, i['Datetime'])
    return ltDates

def Orderedlt(ltDates):
    Orderedlt=sa.sort(ltDates, compare)
    return ltDates

def OrderedArtist(Orderedlt, cityLt ):
    ordered = lt.newList
    for date in Orderedlt:
        for i in cityLt:
            if date == i['Datetime']:
                lt.addLast(ordered, i)
    return ordered

def top3fi(ordered):
    firsts=lt.subList(ordered, 1, 3)
    return firsts

def top3la(ordered):
    latests=lt.subList(ordered, (lt.size(ordered))-2, 3)
    return latests
# Funciones utilizadas para comparar elementos dentro de una lista

def compare(v1, v2):
    if (v1 == v2):
        return 0
    elif v1 > v2:
        return 1
    else:
        return -1

# Funciones de ordenamiento


