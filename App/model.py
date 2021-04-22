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


from typing import final
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    analyzer = {"songs":None, "instrumentalness":None}
    analyzer["songs"] = lt.newList("ARRAY_LIST")
    analyzer["instrumentalness"] = om.newMap(omaptype="RBT", comparefunction=compare_instrumentalness)
    return analyzer

# Funciones para agregar informacion al catalogo
def add_song(analyzer, song):
    lt.addLast(analyzer["songs"], song)
    update_instrumentalness_index(analyzer["instrumentalness"], song)
    return analyzer


def update_instrumentalness_index(map, song):
    instrumentalness = float(song["instrumentalness"])
    entry = om.get(map, instrumentalness)
    if entry is None:
        instruEntry = newDataEntry(song)
        om.put(map, instrumentalness, instruEntry)
    else:
        instruEntry = me.getValue(entry)
    addInstruIndex(instruEntry, song)
    return map

def addInstruIndex(instruEntry, song):
    lst = instruEntry["lstSongs"]
    lt.addLast(lst, song)
    ArtistIndex = instruEntry["ArtistIndex"]
    ArtistEntry = mp.get(ArtistIndex, song["artist_id"])
    if(ArtistEntry is None):
        entry = newArtistEntry(song["artist_id"], song)
        lt.addLast(entry["lstSongs"], song)
        mp.put(ArtistIndex, song["artist_id"], entry)
    else:
        entry = me.getValue(ArtistEntry)
        lt.addLast(entry["lstSongs"], song)
    return instruEntry


def newDataEntry(song):
    entry = {"ArtistIndex": None, "lstSongs":None}
    entry["ArtistIndex"] = mp.newMap(maptype="CHAINING", comparefunction=compareArtistId)
    entry["lstSongs"] = lt.newList("ARRAY_LIST", compare_instrumentalness)
    return entry


def newArtistEntry(artist_id, song):
    sEntry = {"Artist":None, "lstSongs":None}
    sEntry["Artist"] = artist_id
    sEntry["lstSongs"] = lt.newList("ARRAYLIST", compareArtistId)
    return sEntry
# Funciones para creacion de datos

# Funciones de consulta
def crimesSize(analyzer):
    """
    Número de crimenes
    """
    return lt.size(analyzer['songs'])


def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer['instrumentalness'])


def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer['instrumentalness'])


def minKey(analyzer):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer['instrumentalness'])


def maxKey(analyzer):
    """
    Llave mas grande
    """
    return om.maxKey(analyzer['instrumentalness'])



def Requerimiento1(analyzer, initialInstru, finalInstru):
    lst = om.values(analyzer["instrumentalness"], initialInstru, finalInstru)
    totArtists = 0
    totRepros = 0
    for lstInstru in lt.iterator(lst):
        totRepros += lt.size(lstInstru["lstSongs"])
        totArtists += mp.size(lstInstru["ArtistIndex"])
    return totArtists, totRepros

    
# Funciones utilizadas para comparar elementos dentro de una lista
def compare_instrumentalness(ins1, ins2):
    if (ins1 == ins2):
        return 0
    elif (ins1 > ins2):
        return 1
    else:
        return -1 

def compareArtistId(id1, id2):
    Artist = me.getKey(id2)
    if (id1 == Artist):
        return 0
    elif (id1 > Artist):
        return 1
    else:
        return -1 
# Funciones de ordenamiento
