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
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newdatabase():
    database = {'songs': None,
                'contendindex': None
                }

    database['songs'] = lt.newList('ARRAYLIST', cmpfunction= None)
    database['contendindex'] = om.newMap(omaptype='RBT', comparefunction= None)
    return database
                

# Funciones para agregar informacion al catalogo


def addevent(database, event):
    """
    """ 
    lt.addLast(database['songs'], event)
    return database

def loadRBT(map, event, characteristic):
    characteristic = event[characteristic]
    entry = om.get(map, characteristic)
    if entry is None:
        datentry = newDataEntry(event)
        om.put(map, characteristic, datentry)
    else:
        datentry = me.getValue(entry)
    addeventmap(datentry, event)
    return map


# Funciones para creacion de datos

def addeventmap(datentry, event):
    lt.addLast(datentry['tracks'], event['track_id'])
    lt.addLast(datentry['artists'], event['artist_id'])
    return datentry


def newDataEntry(event):
    entry = {'tracks': None, 'artists': None}
    entry['tracks'] = lt.newList('ARRAYLIST')
    entry['artists'] = lt.newList('ARRAYLIST')
    return entry




# Funciones de consulta

def indexHeight(database):
    """
    Altura del arbol
    """
    return om.height(database['contendindex'])

def indexSize(database):
    """
    Numero de elementos en el indice
    """
    return om.size(database['contendindex'])

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
