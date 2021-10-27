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
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def crearCatalogo(): 
    catalog = {'casos': None,
                'dateIndex': None
                }

    catalog['casos'] = lt.newList('SINGLE_LINKED')
    catalog['dateIndex'] = om.newMap(omaptype='BST',
                                      comparefunction=compareDates)

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

# Funciones de ordenamiento
