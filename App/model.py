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
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def crearCatalogo(): 
    catalog = {'casos': None,
                'dateIndex': None,

                }

    catalog['casos'] = lt.newList('SINGLE_LINKED'),
    catalog['dateIndex'] = om.newMap(omaptype='BST', comparefunction=compareDates),
    catalog["horaMin"]= om.newMap(omaptype="RBT"),
    catalog["durations"]=om.newMap(omaptype="RBT")

    return catalog                                  

# Funciones para agregar informacion al catalogo

def addCasos(catalog,caso):
    lt.addLast(catalog["casos"],caso) 

def addDateIndex(catalog):
    casos=catalog["casos"] 
    casosPorFecha={}
    for caso in lt.iterator(casos):
        fecha=caso["datetime"]
        lista=[]
        if fecha not in casosPorFecha:
            lista.append(caso)
            casosPorFecha[fecha]=lista 
        else: 
             valor=casosPorFecha[fecha]
             lista=[]
             lista.append(valor)
             lista.append(caso)  
             casosPorFecha[fecha]=lista  
    fechas=casosPorFecha.keys()
    for fecha in fechas: 
        casos=casosPorFecha[fecha]
        for caso in casos: 
            om.put(catalog["dateIndex"],fecha,caso)          


def addHoraMin(catalog, sights):

    sig= sights["datetime"]
    date=(datetime.datetime.strptime(sig, '%Y-%m-%d %H:%M:%S')).time()
    if not om.contains(catalog["horaMin"],date):
        avista=lt.newList("SINGLE_LINKED")
        lt.addLast(avista,sights)
        om.put(catalog["horaMin"],date,avista)
    else:
        avista=me.getValue(om.get(catalog["horaMin"],date))
        lt.addLast(avista,sights)

def addDuration(catalog, sights):
    duration =float(sights["duration (seconds)"])
    if not om.contains(catalog["durations"], duration):
        avists=lt.newList("SINGLE_LINKED")
        lt.addLast(avists,sights)
        om.put(catalog["durations"], duration,avists)

    else:

        avists=me.getValue(om.get(catalog["durations"], duration))
        lt.addLast(avists,sights)


# Funciones para creacion de datos

# Funciones de consulta
def casosPorCiudad(catalog,ciudad):
    casosCiudad=[]
    casos=catalog["casos"]
    for caso in lt.iterator(casos):
        ciudadCaso=caso["city"]
        if ciudadCaso.strip() == ciudad.strip():
           casosCiudad.append(caso) 
    return casosCiudad 

def sight_by_duration(catalog,duraMin,duraMax):
    key = "horaMin"

    duraMin=(datetime.datetime.strptime(duraMin, '%H:%M:%S')).time()
    duraMax=(datetime.datetime.strptime(duraMax, '%H:%M:%S')).time()

    maxDura=om.maxKey(catalog[key])
    numSightsMaxK=lt.size(me.getValue(om.get(catalog[key],maxDura)))
    avisRange=om.keys(catalog[key],duraMin,duraMax)
    listSights=lt.newList("SINGLE_LINKED")
    for x in lt.iterator(avisRange):
        duracion=me.getValue(om.get(catalog[key],x))
        for avis in lt.iterator(duracion):
            lt.addLast(listSights,avis)
    if key== "duraciones" :
        listSights= ms.sort(listSights,compareDuration)
    else:
        listSights= ms.sort(listSights,compareHoraMin)

    return maxDura,numSightsMaxK,listSights
          
# Funciones utilizadas para comparar elementos dentro de una lista

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    date1Format=datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2Format=datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareHoraMin(sig1 , sig2):
    hora1 = sig1["datetime"]
    date1 = sig1["datetime"]

    hora1 = (datetime.datetime.strptime(hora1, '%Y-%m-%d %H:%M:%S')).time()
    hora2 = sig2["datetime"]
    date2 = sig2["datetime"]

    hora2 = (datetime.datetime.strptime(hora2, '%Y-%m-%d %H:%M:%S')).time()
    date1 = (datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')).date()
    date2 = (datetime.datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')).date()

    if hora1 != hora2:
        return hora1 < hora2
    else:
        return date1 < date2

def compareDuration(sig1, sig2):

    d1 = float(sig1["duration (seconds)"])
    d2 = float(sig2["duration (seconds)"])
    CC1 = sig1["city"] + " " + sig1["country"]
    CC2 = sig2["city"] + " " + sig2["country"]

    if d1 != d2:
        return d1 < d2
    else:
        return CC1 < CC2


# Funciones de ordenamiento
