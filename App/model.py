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


from typing_extensions import Concatenate
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as m
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# ___________________________________________________
# Construccion de modelos
# ___________________________________________________
def newCatalog():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los registros
    Se crean indices (Maps) por los siguientes criterios:
    -Ciudad

    Retorna el analizador inicializado.
    """
    catalogo = {'registros': None,
                'indiceCiudad': None,
                'indiceDuracion': None,
                'indiceHoraMinuto':None,
                }

    catalogo['registros'] = lt.newList('ARRAY_LIST')
    catalogo['indiceCiudad'] =om.newMap(omaptype='RBT',
                                      comparefunction=cmpCiudades)
    catalogo['indiceDuracion'] = om.newMap(omaptype='RBT',
                                      comparefunction=cmpDuracion)
    return catalogo
# ___________________________________________________
# Funciones para agregar informacion al catalogo
# ___________________________________________________

def addRegistro(catalogo, registro):
    dicRegistro ={}
    datetimeRegistro=registro["datetime"]
    if datetimeRegistro=="":
        datetimeRegistro="0001-01-01 00:00:01"
    dicRegistro["fechahora"]= datetime.datetime.strptime(datetimeRegistro,'%Y-%m-%d %H:%M:%S')
    dicRegistro["ciudad"]= registro["city"]
    dicRegistro["estado"]= registro["state"]
    dicRegistro["pais"]= registro["country"]
    dicRegistro["pais-ciudad"]= (dicRegistro["pais"]) +"-"+ dicRegistro["ciudad"]
    dicRegistro["forma"]= registro["shape"]
    duracion= registro["duration (seconds)"]
    if duracion=="":
        duracion=0
    dicRegistro["duracionsegundos"]= float(duracion)
    dicRegistro["duracionvariable"]= registro["duration (hours/min)"]
    dicRegistro["date posted"]= datetime.datetime.strptime(registro["date posted"],'%Y-%m-%d %H:%M:%S')    
    dicRegistro["latitud"]= registro["latitude"]
    dicRegistro["longitud"]= registro["longitude"]

    lt.addLast(catalogo['registros'], dicRegistro)
    updateIndiceCiudad(catalogo['indiceCiudad'], dicRegistro)
    updateIndiceDuracion(catalogo["indiceDuracion"], dicRegistro)
    return catalogo


def updateIndiceCiudad(map, registro):
    """
    Se toma la ciudad del registro y se busca si ya existe en el arbol
    dicha  ciudad.  Si es asi, se adiciona el registro a su lista de registros.
    Si no se encuentra creado un nodo para esa ciudad en el arbol se crea
    """
    ciudad = registro['ciudad']
    addOrCreateListInMap(map,ciudad,registro)
    return map
def updateIndiceDuracion(map, registro):
    """
    Se toma la ciudad del registro y se busca si ya existe en el arbol
    dicha  ciudad.  Si es asi, se adiciona el registro a su lista de registros.
    Si no se encuentra creado un nodo para esa ciudad en el arbol se crea
    """
    duracion = registro["duracionsegundos"]
    addOrCreateListInMap(map,duracion,registro)

    return map
def addOrCreateListInMap(mapa, llave, elemento):
    if om.contains(mapa,llave)==False:
        lista_nueva=lt.newList("ARRAY_LIST")
        lt.addLast(lista_nueva,elemento)
        om.put(mapa,llave,lista_nueva)
    else:
        pareja=om.get(mapa,llave)
        lista_existente=me.getValue(pareja)
        lt.addLast(lista_existente,elemento)
        om.put(mapa,llave,lista_existente)

# ___________________________________________________
# Funciones para creacion de datos
# ___________________________________________________


# ___________________________________________________
# Funciones de consulta
# ___________________________________________________
#REQ 1#
def registrosPorCiudad(catalogo,nombreCiudad):
    par= om.get(catalogo['indiceCiudad'], nombreCiudad)
    if par== None:
        registros=None
    else:
        registros= me.getValue(par)
        for i in lt.iterator(registros):
            fecha=i["fechahora"]
            print(str(fecha))
        #TODO no esta ordenando bien los diccionarios#
        registros= m.sort(registros, cmpDatetime)
        print("after")
        for i in lt.iterator(registros):
            fecha=i["fechahora"]
            print(str(fecha))
    return(registros)
#REQ 2#
def registrosEnRangoDuracion(catalogo,limiteMaximo,limiteMinimo):
    """
    Retorna la lista de crimenes en un rango de duración.
    """
    listaEnRango= lt.newList("ARRAY_LIST")
    listaDeListas = om.values(catalogo['indiceDuracion'],limiteMaximo,limiteMinimo)
    for list in lt.iterator(listaDeListas):
        for registro in list:
            listaEnRango = lt.addLast(listaEnRango,registro)
    return listaEnRango
# ___________________________________________________
#Funciones para consultar info om#
# ___________________________________________________
def registrosSize(catalogo):
    """
    Número de crimenes
    """
    return lt.size(catalogo["registros"])

def indexHeight(catalogo, indice):
    """
    Altura del arbol
    """
    return om.height(catalogo[indice])

def indexSize(catalogo, indice):
    """
    Numero de elementos en el indice
    """
    return om.size(catalogo[indice])

def minKey(catalogo, indice):
    """
    Llave mas pequena
    """
    return om.minKey(catalogo[indice])

def maxKey(catalogo, indice):
    """
    Llave mas grande
    """
    return om.maxKey(catalogo[indice])
# ___________________________________________________
# Funciones utilizadas para comparar elementos dentro de una lista o mapa
# ___________________________________________________

def cmpCiudades(ciudad1,ciudad2):
    """
    Compara dos ciudades alfabeticamente
    """
    if (ciudad1 == ciudad2):
        return 0
    elif (ciudad1 > ciudad2):
        return 1
    else:
        return -1 

def cmpDuracion(duracion1,duracion2):
    """
    Compara dos fechas
    """
    if (duracion1 == duracion2):
        return 0
    elif (duracion1 > duracion2):
        return 1
    else:
        return -1 
def cmpDuracionSort(dic1,dic2):
    """
    Compara ascendentemente por su duración y en caso de múltiples 
    avistamientos de la misma duración,mostrarlos ordenados alfabéticamente 
    por su combinación ciudad y país (country-city).
    """
    duracion1=dic1["duracion"]
    duracion2=dic2["duracion"]
    if (duracion1 == duracion2):
        if dic1["pais-ciudad"] > dic2["pais-ciudad"]:
            return 1
        else:
            return-1
    elif (duracion1 > duracion2):
        return 1
    else:
        return -1
def cmpDatetime(dic1, dic2):
    """
    Compara dos diccionarios por sus fechas
    """
    date1=dic1["fechahora"]
    date2=dic2["fechahora"]
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

# Funciones de ordenamiento
