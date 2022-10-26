"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

Se define la estructura de un catálogo de libros.
El catálogo tendrá  una lista para los libros.

Los autores, los tags y los años se guardaran en
tablas de simbolos.
"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los gamenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {"games": None,
                "dateIndex": None,
                "areaIndex": None,
                }

    analyzer["games"] = lt.newList("SINGLE_LINKED", compareIds)
    analyzer["dateIndex"] = om.newMap(omaptype="RBT",
                                      comparefunction=compareDates)

    return analyzer


# Funciones para agregar informacion al catalogo


def addGame(analyzer, game):
    """
    adicionar un gamen a la lista de gamenes y en el arbol
    """
    lt.addLast(analyzer["games"], game)
    updateDateIndex(analyzer["dateIndex"], game)
    return analyzer





def updateDateIndex(map, game):
    """
    Se toma la fecha del gamen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de gamenes
    y se actualiza el indice de tipos de gamenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de gamenes
    """
    occurreddate = game["Release_Date"]
    gamedate = datetime.datetime.strptime(occurreddate, "%y-%m-%d")
    entry = om.get(map, gamedate.date())
    if entry is None:
        datentry = newDataEntry(game)
        om.put(map, gamedate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, game)
    return map


def addDateIndex(datentry, game):
    """
    Actualiza un indice de tipo de gamenes.  Este indice tiene una lista
    de gamenes y una tabla de hash cuya llave es el tipo de gamen y
    el valor es una lista con los gamenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry["lstgames"]
    lt.addLast(lst, game)
    categoryIndex = datentry["categoryIndex"]
    catentry = m.get(categoryIndex, game["Category"])
    if (catentry is None):
        entry = newcategoryEntry(game["Category"], game)
        lt.addLast(entry["lstcategorys"], game)
        m.put(categoryIndex, game["Category"], entry)
    else:
        entry = me.getValue(catentry)
        lt.addLast(entry["lstcategorys"], game)
    return datentry


def newDataEntry(game):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {"categoryIndex": None, "lstgames": None}
    entry["categoryIndex"] = m.newMap(numelements=30,
                                     maptype="PROBING",
                                     comparefunction=comparecategorys)
    entry["lstgames"] = lt.newList("SINGLE_LINKED", compareDates)
    lt.addLast(entry["lstgames"], game)
    return entry


def newcategoryEntry(categorygrp, game):
    """
    Crea una entrada en el indice por tipo de gamen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {"category": None, "lstcategorys": None}
    ofentry["category"] = categorygrp
    ofentry["lstcategorys"] = lt.newList("SINGLE_LINKED", comparecategorys)
    lt.addLast(ofentry["lstcategorys"], game)
    return ofentry


# ==============================
# Funciones de consulta
# ==============================


def gamesSize(analyzer):
    """
    Número de gamenes
    """
    return lt.size(analyzer["games"])


def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer["dateIndex"])


def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer["dateIndex"])


def minKey(analyzer):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer["dateIndex"])


def maxKey(analyzer):
    """
    Llave mas grande
    """
    return om.maxKey(analyzer["dateIndex"])


def indexHeightAreas(analyzer):
    """
    Altura del arbol por areas
    """
    return om.height(analyzer["areaIndex"])


def indexSizeAreas(analyzer):
    """
    Numero de elementos en el indice por areas
    """
    return om.size(analyzer["areaIndex"])
    


def minKeyAreas(analyzer):
    """
    Llave mas pequena por areas
    """
    return om.minKey(analyzer["areaIndex"])


def maxKeyAreas(analyzer):
    """
    Llave mas grande por areas
    """
    return om.maxKey(analyzer["areaIndex"])


def getgamesByRangeArea(analyzer, initialArea, FinalArea):
    """
    Retorna el numero de gamenes en un rango de areas
    """
    lst = om.values(analyzer["areaIndex"], initialArea, FinalArea)
    totalgames = 0
    for lstarea in lt.iterator(lst):
        totalgames += lt.size(lstarea["lstgames"])
    return totalgames


def getgamesByRange(analyzer, initialDate, finalDate):
    """
    Retorna el numero de gamenes en un rago de fechas.
    """
    lst = om.values(analyzer["dateIndex"], initialDate, finalDate)
    totalgames = 0
    for lstdate in lt.iterator(lst):
        totalgames += lt.size(lstdate["lstgames"])
    return totalgames


def getgamesByRangeCode(analyzer, initialDate, categorycode):
    """
    Para una fecha determinada, retorna el numero de gamenes
    de un tipo especifico.
    """
    gamedate = om.get(analyzer["dateIndex"], initialDate)
    if gamedate["key"] is not None:
        categorymap = me.getValue(gamedate)["categoryIndex"]
        numcategorys = m.get(categorymap, categorycode)
        if numcategorys is not None:
            return m.size(me.getValue(numcategorys)["lstcategorys"])
    return 0


# ==============================
# Funciones de Comparacion
# ==============================


def compareIds(id1, id2):
    """
    Compara dos gamenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


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


def compareAreas(area1, area2):
    """
    Compara dos areas
    """
    if (area1 == area2):
        return 0
    elif (area1 > area2):
        return 1
    else:
        return -1



def comparecategorys(category1, category2):
    """
    Compara dos tipos de gamenes
    """
    category = me.getKey(category2)
    if (category1 == category):
        return 0
    elif (category1 > category):
        return 1
    else:
        return -1
