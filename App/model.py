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
def initCatalog():
    catalog = {'events': None,
               'content_features': None,
               'sentiment_values': None,
               'listening_events': None,
               'genres': None}
    
    catalog['events'] = lt.newList('ARRAY_LIST')
    catalog['content_features'] = mp.newMap(20, maptype='PROBING', loadfactor=0.5)
    catalog['sentiment_values'] = mp.newMap()
    catalog['listening_events'] = mp.newMap()
    catalog['genres'] = mp.newMap(10, maptype='PROBING', loadfactor=0.5)

    return catalog


# Funciones para agregar informacion al catalogo
def addGenre(catalog, genrename, mintempo, maxtempo):
    genre = newGenre(genrename, mintempo, maxtempo)
    mp.put(catalog['genres'], genrename, genre)


def addUserGenre(catalog, genrename, mintempo, maxtempo):
    genre = newGenre(genrename, mintempo, maxtempo)
    mp.put(catalog['genres'], genrename, genre)
    pass


def assignGenre(catalog, event):
    for genre in lt.iterator(mp.valueSet(catalog['genres'])):
        if float(event['tempo']) >= genre['min_tempo'] and float(event['tempo']) <= genre['max_tempo']:
            lt.addLast(genre['events'], event)


def addEvent(catalog, event):
    lt.addLast(catalog['events'], event)
    updateFeatures(catalog['content_features'], event)


def updateFeatures(table, event):
    for feature in event:
        if mp.size(table) < len(event):
            tree = om.newMap(omaptype='RBT', comparefunction=cmpFunction)
            valueevents = lt.newList('ARRAY_LIST')
            lt.addLast(valueevents, event)
            om.put(tree, event[feature], valueevents)
            mp.put(table, feature, tree)
        else:
            tree = me.getValue(mp.get(table, feature))
            if om.contains(tree, event[feature]):
                valueevents = me.getValue(om.get(tree, event[feature]))
                lt.addLast(valueevents, event)
            else:
                valueevents = lt.newList('ARRAY_LIST')
                lt.addLast(valueevents, event)
                om.put(tree, event[feature], valueevents)


# Funciones para creacion de datos
def newGenre(name, mintempo, maxtempo):
    genre = {'name': name.lower(),
             'min_tempo': mintempo,
             'max_tempo': maxtempo,
             'events': lt.newList('ARRAY_LIST')}
    return genre


# Funciones de consulta
def getCharacteristicReproductions(catalog, characteristic, minrange, toprange):
    tree = me.getValue(mp.get(catalog['content_features'], characteristic))
    total = 0
    artists = lt.newList('ARRAY')
    for value in lt.iterator(om.values(tree, minrange, toprange)):
        total += lt.size(value)
        for event in lt.iterator(value):
            if not lt.isPresent(artists, event['artist_id']):
                lt.addLast(artists, event['artist_id'])
    total2 = lt.size(artists)
    artists.clear()
    return total, total2


def getStudyMusic(catalog, mininst, maxinst, mintempo, maxtempo):
    insttree = me.getValue(mp.get(catalog['content_features'], 'instrumentalness'))
    tempotree = me.getValue(mp.get(catalog['content_features'], 'tempo'))
    instrumentals = om.values(insttree, mininst, maxinst)
    tempos = om.values(tempotree, mintempo, maxtempo)
    tracks = lt.newList('ARRAY_LIST')


# Funciones utilizadas para comparar elementos dentro de una lista
def cmpFunction(data1, data2):
    if data1 == data2:
        return 0
    elif data1 > data2:
        return 1
    else:
        return -1


# Funciones de ordenamiento
