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
assert cf

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


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
