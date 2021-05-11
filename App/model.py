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
from random import randint
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():

    analyzer = {'id_canciones': None,
                'autores': None,
                'map_id': None,
                'caracteristicas': None
                }

    analyzer['id_canciones'] = lt.newList('SINGLE_LINKED', compareElements)
    analyzer['autores'] = lt.newList('SINGLE_LINKED', compareElements)
    analyzer['map_id'] = mp.newMap(numelements= 10000, prime= 109345121, maptype= 'CHAINING', loadfactor= 0.5, comparefunction= compareIds)
    analyzer['caracterisiticas'] = mp.newMap(numelements= 10000, prime= 109345121, maptype= 'CHAINING', loadfactor= 0.5, comparefunction= compareElements)
    
    return analyzer

# Funciones para agregar informacion al catalogo

def addCanciones(analyzer, cancion, autor):

    if cancion['track_id'] not in analyzer['id_canciones']:

        if cancion['autor'] not in analyzer['autores']:

            lt.addLast(analyzer['id_canciones'], cancion)
            lt.addLast(analyzer['autores'], autor)

            mp.put(analyzer['map_id'], cancion['track_id'], (analyzer['caracteristicas'], cancion['autor']))


def addCaracterisitica(analyzer, caracteristica):

    value = newCaracteristica(caracteristica[' name'], caracteristica['valor'])
    mp.put(analyzer['caracteristicas'], value['name'],value['valor'] )



# Funciones para creacion de datos
def newCaracteristica(caracteristica, valor):
    caracteristica={'name' : ' ','valor' : 0 }
    caracteristica['name'] = caracteristica
    caracteristica['valor'] = valor

    return caracteristica


# Funciones de consulta
def requerimiento1 (analyzer, caracteristica, valor_min, valor_max):

    table = analyzer['map_id']
    n = mp.size(analyzer['map_id'])
    count_aut = 0
    count_canc = 0
    i=0
    while i < n:

        carac = me.getValue(table,i)[0]
        author = me.getValue(table,i)[1]
        authors = lt.newList()
        value = me.getValue(carac, caracteristica)

        if valor_min <= value <= valor_max:
            count_canc +=1

            if author not in authors:
                count_aut +=1
                lt.addLast(authors, author) 
    
    return count_aut, count_canc

def requerimiento2 (analyzer, min_energy, max_energy, min_danceability, max_danceability):

    table = analyzer['map_id']
    n= mp.size(table)
    track_id = mp.keySet(table)
    tracks = mp.newMap(numelements=n,prime= 109345121, maptype= 'CHAINING', loadfactor= 0.5, comparefunction= compareElements) 
    i=0
    track_count = 0

    while i < n:

        carac = me.getValue(table,i)[0]
        v_energy = me.getValue(carac, 'energy')
        v_dance = me.getValue(carac, 'danceability')

        if min_energy <= v_energy <= max_energy and min_danceability <= v_dance <= max_danceability:
            
            if track_id not in mp.keySet(tracks):
                val = lt.newList()
                lt.addLast(val, v_energy)
                lt.addLast(val, v_dance)
                mp.put(tracks,track_id, val)

                track_count +=1
        
        i+=1
        rta = random(tracks)

    return rta, track_count

def random(table):

    n = mp.size(table)
    numero = randint(0, n-1)
    i= 0
    rta = lt.newList()

    while i < 5:

        pareja = mp.get(table, numero[i])
        lt.addLast(rta, pareja)
        i+=1

    return rta



    


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def compareIds(id1, id2):

    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareElements(ele1, ele2):

    if (ele1 == ele2):
        return 0
    elif (ele1 > ele2):
        return 1
    else:
        return -1