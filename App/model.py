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
        pass



# Funciones para creacion de datos
def newGenre(name, mintempo, maxtempo):
    genre = {'name': name.lower(),
             'min_tempo': mintempo,
             'max_tempo': maxtempo,
             'events': lt.newList('ARRAY_LIST')}
    return genre


# Funciones de consulta
def getStudyMusic(mininst, maxinst, mintempo, maxtempo):
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
