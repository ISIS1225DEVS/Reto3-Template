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
from DISClib.Algorithms.Sorting import mergesort as marg
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newdatabase():
    database = {'contendindex': None,
                'genre': None}

    database['contendindex'] = mp.newMap(10,
                                    maptype= 'PROBING',
                                    loadfactor= 0.9,
                                    comparefunction= None)
    database['genre'] = {'reggae':[60,90],
                         'down-tempo':[70,100],
                         'chill-out':[90,120], 
                         'hip-hop':[85,115],
                         'jazz-and-funk':[120,125], 
                         'pop':[100,130], 
                         'r&b':[60,80], 
                         'rock':[110,140], 
                         'metal':[100,160]}
    return database
                

# Funciones para agregar informacion al catalogo


def addevent(database, event):
    """
    se cargan los datos en el la estructura de datos
    que en este caso es un map el cual contiene toda la informacion.
    """

    hashtable = database['contendindex']
    tempo = event['tempo']
    energy =event['energy']
    valence = event['valence']
    liveness = event['liveness']
    speechiness = event['speechiness']
    acousticness = event['acousticness']
    danceability = event['danceability']
    instrumentalness = event['instrumentalness']

    loadhashtable(hashtable, tempo, event, 'tempo')
    loadhashtable(hashtable, energy, event, 'energy')
    loadhashtable(hashtable, valence, event, 'valence')
    loadhashtable(hashtable, liveness, event, 'liveness')
    loadhashtable(hashtable, speechiness, event, 'speechiness')
    loadhashtable(hashtable, acousticness, event, 'acousticness')
    loadhashtable(hashtable, danceability, event, 'danceability')
    loadhashtable(hashtable, instrumentalness, event, 'instrumentalness')
    return database


def loadhashtable(database, information, event, characteristic): # hashtable 
    entry = mp.get(database, characteristic)
    if (entry is None):
        RBT = newRbt()  
        loadRBT(RBT, information, event, characteristic)
        mp.put(database, characteristic, RBT)
    else:
        RBT = me.getValue(entry)
        loadRBT(RBT, information, event, characteristic)
    return database 

 
def loadRBT(RBT, information, event, characteristic):  #arbol binario       
    entry = om.get(RBT, information)
    if entry is None:
        datentry = newDataEntry(event)
        om.put(RBT, information, datentry)
    else:
        datentry = me.getValue(entry)
    addeventmap(datentry, event)
    return RBT




# Funciones para creacion de datos

def newDataEntry(event):
    entry = {'tracks': None, 'artists': None, 'events': None}
    entry['tracks'] = lt.newList('ARRAY_LIST')
    entry['artists'] = mp.newMap(20000,  #poner 500
                                   maptype='PROBING',
                                   loadfactor=0.9,
                                   comparefunction= None)
    entry['events'] = None
    return entry

    
def addeventmap(datentry, event):
    lt.addLast(datentry['tracks'], event)
    entry = mp.get(datentry['artists'], event['artist_id'])
    if (entry is None):
        mp.put(datentry['artists'], event['artist_id'], {})
    return datentry


def newRbt():
    tree = om.newMap(omaptype='RBT',
                    comparefunction= None)
    return tree

def createhahstable(elements):
    hashtable = mp.newMap(elements,
                            maptype='PROBING',
                            loadfactor=0.9,
                            comparefunction= None)
    return hashtable



# Funciones de consulta

def indexHeight(database):
    return om.height(database['contendindex'])

def indexSize(database):
    return om.size(database['contendindex'])

def Requerimiento1(database, characteristic, minvalue, maxvalue):
    hahstable = database['contendindex']
    RBT = mp.get(hahstable, characteristic.lower())
    RBT = me.getValue(RBT)
    lst = om.values(RBT, minvalue, maxvalue)
    totalevets = 0
    maptartist = createhahstable(20000) #poner 2000

    for event in lt.iterator(lst):
        totalevets += lt.size(event['tracks'])
        listartist = mp.keySet(event['artists'])
        for event in lt.iterator(listartist):
            countuniqueartist(maptartist, event)

    return totalevets, lt.size(mp.valueSet(maptartist))


def Requerimiento3(database, mini, maxi, mint, maxt):
    hahstable = database['contendindex']
    RBTI = mp.get(hahstable, 'instrumentalness')
    RBTT = mp.get(hahstable, 'tempo')
    RBTI = me.getValue(RBTI)
    RBTT = me.getValue(RBTT)
    lstI = om.values(RBTI, mini, maxi)
    lstT = om.values(RBTT, mint, maxt)
    mapsongs = createhahstable(2000)
                    
    for event in lt.iterator(lstI):
        for event in lt.iterator(event['tracks']):
            entry = mp.get(mapsongs, event['track_id'])
            if ((entry is None) and (mini<=event['instrumentalness']<=maxi) and (mint<=event['tempo']<=maxt)):
                mp.put(mapsongs, event['track_id'], event)

    for event in lt.iterator(lstT):
        for event in lt.iterator(event['tracks']):
            entry = mp.get(mapsongs, event['track_id'])
            if ((entry is None) and (mini<=event['instrumentalness']<=maxi) and (mint<=event['tempo']<=maxt)):
                mp.put(mapsongs, event['track_id'], event)
    return lt.size(mp.valueSet(mapsongs)), mp.valueSet(mapsongs)


def Requerimiento4(database, listg, newg, minT, maxT):
    genre = database['genre'] # diccionario con los generos
    hahstable = database['contendindex']
    RBTT = mp.get(hahstable, 'tempo')
    RBTT = me.getValue(RBTT)
    maptracks = createhahstable(12)  #numeros 
    Totalrp = findreproductions(maptracks, genre, RBTT,listg, newg, minT, maxT)
    keys = mp.keySet(maptracks)
    return Totalrp, mp.valueSet(maptracks)

def findreproductions(maptracks,genre, RBTT,listg, newg, minT, maxT):
    Totalrp = 0
    for element in listg:
        a = int((genre[element][0]))
        b = int((genre[element][1]))
        lstT = om.values(RBTT, a, b) #obtener los valores en cada genero recibido
        for event in lt.iterator(lstT): #diccionario con la informacion {list, hasht}
            Totalrp += lt.size(event['tracks'])
            for event in lt.iterator(event['tracks']):
                for element in listg:
                    a = int((genre[element][0]))
                    b = int((genre[element][1]))
                    if (float(a)<=float(event['tempo'])<=float(b)): 
                        countreproductions(maptracks, element, event['artist_id'], a, b)

    if (newg != 'none'):
        lstT = om.values(RBTT, minT, maxT)
        for event in lt.iterator(lstT):
            Totalrp += lt.size(event['tracks'])
            for event in lt.iterator(event['tracks']):
                for element in listg:
                    a = int((genre[element][0]))
                    b = int((genre[element][1]))
                    if (float(a)<=float(event['tempo'])<=float(b)): # element es el genero 
                        countreproductions(maptracks, element, event['artist_id'], a, b) 
    return Totalrp


def countuniqueartist(hahsT,event):
    entry = mp.get(hahsT, event)
    if (entry is None):
        mp.put(hahsT, event, 0)

def countreproductions(maptracks, element, id, a, b): #hashtable para contar repoduccciones por genero 
    entry = mp.get(maptracks, element)
    if (entry is None):
        datentry = {'genre':element, 'range':(a,b), 'rep':1, 'Uartist': createhahstable(5200)}
        countuniqueartist(datentry['Uartist'],id)
        mp.put(maptracks, element, datentry)
    else:
        datentry= me.getValue(entry)
        datentry['rep'] +=  1
        countuniqueartist(datentry['Uartist'],id)
        






        



    







    



# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def compareevents(event1, event2):
    pass
