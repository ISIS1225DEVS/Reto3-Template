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
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def InitCatalog():
    catalog = {'lst_UFO': None,
                'duration_UFO': None,
                'datetime_UFO': None,
                'Citys': None}
    catalog['lst_UFO'] = lt.newList(datastructure='SINGLE_LINKED')
    catalog['duration_UFO'] = om.newMap(omaptype='RBT')
    catalog['datetime_UFO'] = om.newMap(omaptype='RBT')
    #TOCA CAMBIAR EL CITYS POR UN MAPA ORDENADO
    catalog['Citys'] = mp.newMap(maptype='PROBING',
                                loadfactor=0.4)
    return catalog
# Funciones para agregar informacion al catalogo
def addUFO(catalog, ufo_event):
    #CADA VEZ QUE SE ITERA EL CSV, VA A ENTRAR A LAS SIGUIENTES FUNCIONES
    lt.addLast(catalog['lst_UFO'], ufo_event)
    addCity(catalog['Citys'], ufo_event)
    UpdateDuration(catalog['duration_UFO'], ufo_event)
    UpdateDatatime(catalog['datetime_UFO'], ufo_event)

def UpdateDuration(orderedmap, ufo_event):
    #ESTA ES LA ESTRUCTURA PARA LAS SIGUIENTES FUNCIONES TAMBIÉN
    #EN ESTA FUNCIÓN LA VARIABLE DURATION_EVENT TOMA LA DURACIÓN EN SEGUNDOS
    duration_event = ufo_event['duration (seconds)']
    #PREGUNTA SI ESA DURACIÓN SE ENCUENTRA COMO LLAVE EN EL MAPA ORDENADO
    duration_entry = om.get(orderedmap, duration_event)
    #AQUÍ PREGUNTA SI ES NONE, Y SÍ LO ES, QUE CREE UNA LISTA Y AÑADA EL EVENTO EN ESA LISTA.
    if duration_entry is None:
        duration_list = lt.newList()
        lt.addLast(duration_list, ufo_event)
    #PARA FINALMENTE AÑADIR LA LLAVE DURATIONEVENT CON EL VALOR DE LA LISTA        
        om.put(orderedmap, duration_event, duration_list)
    else: 
    #AQUÍ MIRA SI YA SE ENCUENTRA LA LLAVE, Y SÍ ES ASÍ, ENTONCES OBTIENE EL VALOR (QUE ES UNA LSTA) Y AÑADE EL EVENTO QUE SE ESTÁ ITERANDO
        value_entry = me.getValue(duration_entry)
        lt.addLast(value_entry, ufo_event)
    return orderedmap


def UpdateDatatime(orderedmap, ufo_event):
    occurreddate = ufo_event['datetime']
    ufodate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    time_entry = om.get(orderedmap, ufodate.date())
    if time_entry is None:
        ufodate_list = lt.newList()
        lt.addLast(ufodate_list, ufo_event)
        om.put(orderedmap,ufodate.date(),ufodate_list)
    else:
        value_entry = me.getValue(time_entry)
        lt.addLast(value_entry, ufo_event)
    return orderedmap

def addCity(map, ufo_event):
    city = ufo_event['city']
    city_entry = mp.get(map, city)
    if (city_entry is None):
        city_list = lt.newList()
        lt.addLast(city_list,ufo_event)
        mp.put(map, city, city_list)
    else:
        value_entry = me.getValue(city_entry)
        lt.addLast(value_entry,ufo_event)
    return map

def datatimesize(catalog):
    return om.size(catalog['datetime_UFO'])

def durationsize(catalog):
    return om.size(catalog['duration_UFO'])
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
