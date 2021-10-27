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
from DISClib.ADT import orderedmap as omap
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def CreateCatalog(): #Se crea el catalogo 
    catalog = {"sightings":None,"dates":None} #Se crea el catalogo. Diccionario con dos parejas llave-valor
    catalog["dates"]=omap.newMap(omaptype="RBT") #Se crea un nuevo mapa dentro de la llave de dates
    return catalog

# Funciones para agregar informacion al catalogo
def AddDates(catalog, sighting): #Se crea al función, entra el catalogo y el avistamiento
    #breakpoint()
    sighting_date = datetime.datetime.strptime(sighting["datetime"], '%Y-%m-%d %H:%M:%S') #Se convierte el formato de la fecha
    if not omap.contains(catalog["dates"], sighting_date.date()): #Se observa si en el mapa está la fecha de lo contrario
        sighting_list = lt.newList("SINGLE_LINKED") #Se crea una lista vacía 
        lt.addFirst(sighting_list, sighting) #Se añade toda la información del avistamiento a la lista
        omap.put(catalog["dates"], sighting_date.date(), sighting_list) #Se agrega en el mapa
    else:
        sighting_list = me.getValue(omap.get(catalog["dates"], sighting_date.date())) #Se saca la lista que contiene la fecha de avistamiento
        lt.addFirst(sighting_list, sighting) #Se añade la información de dicho avistamiento
    catalog["sightings"] = sighting #Se añade el avistamiento en el mapa con la llave avistamientos 

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
