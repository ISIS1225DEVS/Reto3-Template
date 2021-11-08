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

import datetime
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from DISClib.ADT import orderedmap as om
# Construccion de modelos

def initCatalog():
    """
    Retorna un nuevo catálogo vacío
    """

    # Estructura del catálogo
    catalog = mp.newMap()

    # Definición de la estructura de datos
    mp.put(catalog, "ufo_sightings", lt.newList())

    # Resultado
    return catalog

# Funciones para agregar informacion al catalogo

def addSighting(catalog, sighting):
    """
    Añade una observación de un UFO en el catálogo sin retornarlo
    """

    # Adición de información de la observación
    sighting_info = newSighting(sighting)
    
    # Adición de la observación a la lista del catálogo
    ufo_list = mp.get(catalog, "ufo_sightings")["value"]
    lt.addLast(ufo_list, sighting_info)
    mp.put(catalog, "ufo_sightings", ufo_list)
    


# Funciones para creacion de datos

def newSighting(sighting):
    """
    Añade la información de una observación en una estructura de datos
    """
    # Estructura de datos de la observación
    sighting_info = mp.newMap()

    # Definición de llaves
    for key, value in sighting.items():
        mp.put(sighting_info, key, value)

    # Resultado
    return sighting_info

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def contar_avistamientos(catalog, city):

    avistamientos_ciudad= 0
    mapa_ciudades= mp.newMap(numelements= 11, loadfactor= 8)
    lt_ciudad= lt.newList(datastructure= "ARRAY_LIST")
    for diccionarios in lt.iterator(mp.get(catalog, "ufo_sightings")["value"]):
            
        if mp.contains(mapa_ciudades, me.getValue(mp.get(diccionarios, "city"))):
            mp.put(mapa_ciudades, me.getValue(mp.get(diccionarios, "city")), mp.get(mapa_ciudades, me.getValue(mp.get(diccionarios, "city")))["value"] +1) 
        else:
            mp.put(mapa_ciudades, me.getValue(mp.get(diccionarios, "city")), 1) 

        if(me.getValue(mp.get(diccionarios, "city"))) == city:
            avistamientos_ciudad +=1
            lt.addLast(lt_ciudad, diccionarios)

    total_avistamientos= mp.size(mapa_ciudades)
    mapa= om.newMap(comparefunction= compareDates)
    for x in lt.iterator(lt_ciudad):
        occurreddate= mp.get(x, "datetime")["value"]
        avistamiento= datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
        om.put(mapa, avistamiento, x)
            
    max= om.maxKey(mapa)
    min= om.minKey(mapa)
    llaves= om.keys(mapa, min, max)
    respuestas= lt.newList(datastructure= "ARRAY_LIST")
    lt.addLast(respuestas, total_avistamientos)
    lt.addLast(respuestas, avistamientos_ciudad)
    lt.addLast(respuestas, mapa)
    lt.addLast(respuestas, llaves)
    return respuestas

def compare_time(time1, time2):

    if(time1 < time2):
        return 1
    elif(time2 == time1):
        return 0
    else: 
        return -1

def contar_avistamientos_hora(catalog, hora_inicial, hora_final):
    contador_rango= 0
    mapa_rango= om.newMap(comparefunction= compare_time)
    mapa_tarde= om.newMap(comparefunction= compare_time)
    for diccionarios in lt.iterator(mp.get(catalog, 'ufo_sightings')["value"]):

        hora= mp.get(diccionarios, "datetime")["value"]
        hora2= hora[11:]
        hora= hora[11:]       
        hora= datetime.datetime.strptime(hora, "%H:%M:%S")
            
        if om.contains(mapa_tarde, hora2):
            n= om.get(mapa_tarde, hora2)["value"]
            n+=1
            om.put(mapa_tarde, hora2, n)
        else:
            om.put(mapa_tarde, hora2, 1)

        if(hora >= hora_inicial) and (hora <= hora_final):
                
            om.put(mapa_rango, mp.get(diccionarios, "datetime")["value"], diccionarios)
            contador_rango+=1

    llaves1= om.keySet(mapa_tarde)
    llaves2= om.keySet(mapa_rango)
    respuestas= lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(respuestas, contador_rango)
    lt.addLast(respuestas, mapa_tarde)
    lt.addLast(respuestas, llaves1)
    lt.addLast(respuestas, mapa_rango)
    lt.addLast(respuestas, llaves2)
    return respuestas

