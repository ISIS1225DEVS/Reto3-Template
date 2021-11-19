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
from DISClib.Algorithms.Sorting import shellsort as sa
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

    catalog['casos'] = lt.newList('SINGLE_LINKED')

    catalog['dateIndex'] = om.newMap(omaptype='BST', comparefunction=compareDates)
    catalog["horaMin"]= om.newMap(omaptype="RBT")
    catalog["durations"]=om.newMap(omaptype="RBT")

    catalog['dateIndex'] = om.newMap(omaptype='BST',comparefunction=compareDateIndex)
                                      
    catalog['hoursIndex'] = om.newMap(omaptype='BST',
                                      comparefunction=compareHours)
    catalog['LongitudIndex'] = om.newMap(omaptype='BST',
                                      comparefunction=compareLongitud)                                                                       


    return catalog                                  

# Funciones para agregar informacion al catalogo

def addCasos(catalog,caso):
    lt.addLast(catalog["casos"],caso) 

def addDateIndex(catalog):
    casos=catalog["casos"] 
    casosPorFecha={}
    for caso in lt.iterator(casos):
        fecha=caso["datetime"]
        fechaSpl=fecha.split()
        fechaAMD=fechaSpl[0]
        casoDic={}
        casoDic['datetime']=caso['datetime']
        casoDic['city']=caso['city']
        casoDic['state']=caso['state']
        casoDic['country']=caso['country']
        casoDic['shape']=caso['shape']
        casoDic['duration (seconds)']=caso['duration (seconds)']
        casoDic['duration (hours/min)']=caso['duration (hours/min)']
        casoDic['comments']=caso['comments']
        casoDic['date posted']=caso['date posted']
        casoDic['latitude']=caso['latitude']
        casoDic['longitude']=caso['longitude']
        lista=[]
        if fechaAMD not in casosPorFecha:
            lista.append(casoDic)
            casosPorFecha[fechaAMD]=lista 
        else: 
             valor=casosPorFecha[fechaAMD]
             lista=[]
             lista.append(valor)
             lista.append(casoDic)  
             casosPorFecha[fechaAMD]=lista  
    fechas=list(casosPorFecha.keys())
    fechasLt=lt.newList("ARRAY_LIST",cmpfunction=compareDates) 
    for fechaL in fechas: 
        lt.addLast(fechasLt,fechaL)
    fechasSort=sa.sort(fechasLt,compareDates)  
    for fecha in lt.iterator(fechasSort): 
        casos=casosPorFecha[fecha]
        for caso in casos:          
            om.put(catalog["dateIndex"],fecha,caso)
        
             
            
def addHoursIndex(catalog):
    casos=catalog["casos"] 
    casosPorHora={}
    for caso in lt.iterator(casos):
        fecha=caso["datetime"]
        fechaSpl=fecha.split()
        hora=fechaSpl[1]
        lista=[]
        if hora not in casosPorHora: 
           lista.append(caso)   
           casosPorHora[hora]=lista
        else:  
             valor=casosPorHora[hora]
             valor.append(caso)      
             casosPorHora[hora]=valor                             
    horas=list(casosPorHora.keys())
    horas.sort()
    for hora in horas: 
        casos=casosPorHora[hora]       
        lista=lt.newList("ARRAY_LIST") 
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

            casoDic={}
            casoDic['datetime']=caso['datetime']
            casoDic['city']=caso['city']
            casoDic['state']=caso['state']
            casoDic['country']=caso['country']
            casoDic['shape']=caso['shape']
            casoDic['duration (seconds)']=caso['duration (seconds)']
            casoDic['duration (hours/min)']=caso['duration (hours/min)']
            casoDic['comments']=caso['comments']
            casoDic['date posted']=caso['date posted']
            casoDic['latitude']=caso['latitude']
            casoDic['longitude']=caso['longitude'] 
            lt.addLast(lista,casoDic)          
        om.put(catalog["hoursIndex"],hora,lista)  
           
def addLongitudIndex(catalog):
    casos=catalog["casos"] 
    casosPorLongitud={}
    for caso in lt.iterator(casos):
        longitudInt=round(float(caso["longitude"]),2)
        longitudStr=str(longitudInt)
        casoDic={}
        casoDic['datetime']=caso['datetime']
        casoDic['city']=caso['city']
        casoDic['state']=caso['state']
        casoDic['country']=caso['country']
        casoDic['shape']=caso['shape']
        casoDic['duration (seconds)']=caso['duration (seconds)']
        casoDic['duration (hours/min)']=caso['duration (hours/min)']
        casoDic['comments']=caso['comments']
        casoDic['date posted']=caso['date posted']
        casoDic['latitude']=caso['latitude']
        casoDic['longitude']=caso['longitude']
        lista=[]
        if longitudStr not in casosPorLongitud: 
           lista.append(casoDic)   
           casosPorLongitud[longitudStr]=lista
        else:  
             valor=casosPorLongitud[longitudStr]
             lista.append(valor)
             lista.append(casoDic)  
             casosPorLongitud[longitudStr]=lista       
    longitudes=list(casosPorLongitud.keys())
    longitudesLt=lt.newList("ARRAY_LIST",cmpfunction=compareLongitudes) 
    for longitudL in longitudes: 
        lt.addLast(longitudesLt,longitudL)
    longitudesSort=sa.sort(longitudesLt,compareLongitudes)  
    for longitud in lt.iterator(longitudesSort): 
        casos=casosPorLongitud[longitud]
        for caso in casos:          
            om.put(catalog['LongitudIndex'],longitud,caso)
    




# Funciones de consulta
def casosPorCiudad(catalog,ciudad):
    casosCiudad=lt.newList("ARRAY_LIST")
    casos=catalog["casos"]
    for caso in lt.iterator(casos):
        ciudadCaso=caso["city"]
        if ciudadCaso.strip() == ciudad.strip(): 
           lt.addLast(casosCiudad,caso)
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
          

def casosPorHoras(catalog,rangoInferior,rangoSuperior):
     inferiorFormat=datetime.datetime.strptime(rangoInferior, "%H:%M:%S") 
     superiorFormat=datetime.datetime.strptime(rangoSuperior, "%H:%M:%S") 
     casos=catalog["hoursIndex"]  
     casosEnRango=lt.newList("ARRAY_LIST")
     horas=om.keySet(casos)
     for hora in lt.iterator(horas):
         horaFormat=datetime.datetime.strptime(hora, "%H:%M:%S") 
         if horaFormat > inferiorFormat and horaFormat < superiorFormat:
             casosEnHora=om.get(casos,hora)
             casosEnHoraValue=(casosEnHora["value"])      
             for caso in lt.iterator(casosEnHoraValue):
                 lt.addLast(casosEnRango,caso)                    
     return casosEnRango

def casosPorFechas(catalog,rangoInferior,rangoSuperior):
     inferiorFormat=datetime.datetime.strptime(rangoInferior, "%Y-%m-%d") 
     superiorFormat=datetime.datetime.strptime(rangoSuperior, "%Y-%m-%d")    
     casos=catalog["dateIndex"]     
     casosEnRango=lt.newList("ARRAY_LIST")
     fechas=om.keySet(casos)
     for fecha in lt.iterator(fechas):
         fechaFormat=datetime.datetime.strptime(fecha, "%Y-%m-%d") 
         if fechaFormat > inferiorFormat and fechaFormat < superiorFormat:
             casosEnFecha=om.get(casos,fecha)
             casosEnFechaValue=casosEnFecha["value"]                 
             lt.addLast(casosEnRango,casosEnFechaValue) 
     return casosEnRango          

def casosPorLongitud (catalog,longitudMin,longitudMax):
    listaEnRango=lt.newList("ARRAY_LIST")
    casos=catalog['LongitudIndex']
    longitudes=om.keySet(casos)
    for longitud in lt.iterator(longitudes):
        if float(longitud) > float(longitudMin) and float(longitud) <float(longitudMax): 
           casosEnLongitud=om.get(casos,longitud)
           casosEnLongitudValue=casosEnLongitud["value"]
           lt.addLast(listaEnRango,casosEnLongitud)
    return listaEnRango     

def casosPorLatitud(listaOrdenadaPorLongitud,latitudMin,latitudMax):
    listaEnRangoLatitud=lt.newList("ARRAY_LIST") 
    for longitud in lt.iterator(listaOrdenadaPorLongitud): 
        key=longitud["key"]
        value=longitud["value"]
        latitud=round(float(value['latitude']),2)
        if latitud > float(latitudMin) and latitud < float(latitudMax): 
           lt.addLast(listaEnRangoLatitud,value) 

    return listaEnRangoLatitud


# Funciones utilizadas para comparar elementos dentro de una lista

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    date1Format=datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2Format=datetime.datetime.strptime(date2, "%Y-%m-%d")
    return date1Format < date2Format 

def compareLongitudes(longitud1,longitud2):
    return longitud1 < longitud2 

def compareDateIndex(date1, date2):
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
def compareHours(date1, date2):
    """
    Compara las horas de dos fechas
    """
    date1Format=datetime.datetime.strptime(date1, "%H:%M:%S")
    date2Format=datetime.datetime.strptime(date2, "%H:%M:%S")
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
def compareLongitud(longitud1,longitud2): 
    if (longitud1 == longitud2):
        return 0
    elif (longitud1 > longitud2):
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


