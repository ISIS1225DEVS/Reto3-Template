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
from DISClib.ADT import orderedmap as om

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    analyzer = {"songs":None, "instrumentalness":None}
    analyzer["songs"] = lt.newList("ARRAY_LIST", cmpfunction=compareTrackId)
    analyzer["instrumentalness"] = om.newMap(omaptype="RBT", comparefunction=compareeFunction)
    analyzer["acousticness"] = om.newMap(omaptype='RBT', comparefunction=compareeFunction)
    analyzer["liveness"] = om.newMap(omaptype='RBT', comparefunction=compareeFunction)
    analyzer["speechiness"] = om.newMap(omaptype='RBT', comparefunction=compareeFunction)
    analyzer["energy"] = om.newMap(omaptype='RBT', comparefunction=compareeFunction)
    analyzer["danceability"] = om.newMap(omaptype='RBT', comparefunction=compareeFunction)
    analyzer["valence"] = om.newMap(omaptype='RBT', comparefunction=compareeFunction)
    return analyzer

# Funciones para agregar informacion al catalogo
def add_song(analyzer, song):
    lt.addLast(analyzer["songs"], song)
    return analyzer

def createIndex(analyzer, caract):
    for song in lt.iterator(analyzer["songs"]):
        updateIndex(analyzer[caract], song, caract)
    return analyzer

def updateIndex(map, song, caract):
    instrumentalness = float(song[caract])
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
    SongIdIndex = instruEntry["songIdIndex"]
    ArtistEntry = mp.get(ArtistIndex, song["artist_id"])
    SongIdEntry = mp.get(SongIdIndex, song["track_id"])

    if(SongIdEntry is None):
        eentry = newSongIdEntry(song["track_id"])
        mp.put(SongIdIndex, song['track_id'], eentry)

    if(ArtistEntry is None):
        entry = newArtistEntry(song["artist_id"], song)
        lt.addLast(entry["lstSongs"], song)
        mp.put(ArtistIndex, song["artist_id"], entry)
    if(ArtistEntry is not None):
        entry = me.getValue(ArtistEntry)
        lt.addLast(entry["lstSongs"], song)
    return instruEntry


def newDataEntry(song):
    entry = {"ArtistIndex": None, "lstSongs":None, 'songIdIndex':None}
    entry["ArtistIndex"] = mp.newMap(maptype="CHAINING", comparefunction=compareArtistId)
    entry["lstSongs"] = lt.newList("ARRAY_LIST" , cmpfunction=compareTrackId)
    entry['songIdIndex'] = mp.newMap(maptype='CHAINING', comparefunction=compareSongId)
    return entry


def newArtistEntry(artist_id, song):
    sEntry = {"Artist":None, "lstSongs":None}
    sEntry["Artist"] = artist_id
    sEntry["lstSongs"] = lt.newList("ARRAYLIST", compareArtistId)
    return sEntry

def newSongIdEntry(songId):
    sEntry = {'songId':None}
    sEntry["songId"] = songId
    return sEntry

# Funciones para creacion de datos

# Funciones de consulta
def Requerimiento1(analyzer, initialInstru, finalInstru, caract):
    if(om.size(analyzer[caract]) == 0):
        createIndex(analyzer, caract)
    lst = om.values(analyzer[caract], initialInstru, finalInstru)
    totArtists = 0
    totRepros = 0
    totPistasUnicas = 0
    for lstInstru in lt.iterator(lst):
        totRepros += lt.size(lstInstru["lstSongs"])
        totArtists += mp.size(lstInstru["ArtistIndex"])
        totPistasUnicas += mp.size(lstInstru['songIdIndex'])
    return totArtists, totRepros, totPistasUnicas

def Requerimiento2(analyzer, menorEnergy, mayorEnergy, menorDance, mayorDance):
    if(om.size(analyzer['energy']) == 0):
        createIndex(analyzer, 'energy')
        print('RBT de Energy creado')
    else:
        print('RBT de Energy ya existe')
    if(om.size(analyzer['danceability']) == 0):
        createIndex(analyzer, 'danceability')
        print('RBT de Energy creado')
    else:
        print('RBT de danceability ya existe')
    
    lstEnergy = om.values(analyzer["energy"], menorEnergy, mayorEnergy)
    lstDance = om.values(analyzer['danceability'], menorDance, mayorDance)

    lstEnergyDance = lt.newList(datastructure='ARRAY_LIST',  cmpfunction=compareTrackId)

    for lstDan in lt.iterator(lstDance):
        for lst in lt.iterator(lstEnergy):
            for songId in lt.iterator(mp.keySet(lstDan['songIdIndex'])):
                esta1= 0
                if(mp.contains(lst['songIdIndex'], songId)==True):
                    esta1 = 1
                if esta1 == 1:
                    lt.addLast(lstEnergyDance, songId)

    return print(lt.size(lstEnergyDance))
            
    
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





    
# Funciones utilizadas para comparar elementos dentro de una lista
def compareeFunction(ins1, ins2):
    if (ins1 == ins2):
        return 0
    elif (ins1 > ins2):
        return 1
    else:
        return -1 

def compareTrackId(song1, song2):
    return song1['track_id'], song2['track_id']

def compareArtistId(id1, id2):
    Artist = me.getKey(id2)
    if (id1 == Artist):
        return 0
    elif (id1 > Artist):
        return 1
    else:
        return -1 
def compareSongId(id1, id2):
    songId = me.getKey(id2)
    if (id1 == songId):
        return 0
    elif (id1 > songId):
        return 1
    else:
        return -1   
# Funciones de ordenamiento
