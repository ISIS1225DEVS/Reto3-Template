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
from datetime import datetime
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
    analyzer = {"games":m.newMap(numelements=40,maptype='PROBING'),
                "dateGame":om.newMap('RBT'),
                "tries":om.newMap('RBT'),
                "records":m.newMap(numelements=40,maptype='PROBING'),
                "dateRecord":om.newMap('RBT'),
                "playerRecord":om.newMap('RBT')
                }
    return analyzer

def addGame(analyzer,game):
    m.put(analyzer["games"],game['Game_Id'],game)
    updateDateGame(analyzer["dateGame"],game)
    return analyzer

def addRecord(analyzer,record):
    m.put(analyzer["records"],record['Game_Id'],record)
    updateRecordDate(analyzer["dateRecord"],record)
    return analyzer


def updateDateGame(map,game):
    gameDate = game["Release_Date"]
    
    if gameDate == "" or gameDate == " " or gameDate == None:
        gameDate="31-12-99"
    
    gameDate = datetime.strptime(gameDate,"%y-%m-%d")
    entry = om.get(map,gameDate)
    if entry is None:
        dateEntry = newDateGameEntry(game)
        om.put(map,gameDate,dateEntry)
    else:
        dateEntry = me.getValue(entry)

    addDateGameIndex(dateEntry,game)
    
    return map

def updateRecordDate(map,record):
    recordDate = record["Record_Date_0"]
    if recordDate == "" or recordDate == " " or recordDate == None:
        recordDate="9999-12-31T23:59:59Z"
    recordDate = datetime.strptime(recordDate,"%Y-%m-%dT%H:%M:%SZ")
    entry = om.get(map,recordDate)
    if entry is None:
        dateEntry = newDateRecordEntry(record)
        om.put(map,recordDate,dateEntry)
    else:
        dateEntry = me.getValue(entry)

    addDateRecordIndex(dateEntry,record)
    
    return map

def addDateGameIndex(dateEntry,game):
    lst = dateEntry["lstgames"]
    lt.addLast(lst,game)
    gamesIndex = dateEntry["gamesIndex"]
    
    gameEntry = m.get(gamesIndex, game["Game_Id"])
    if (gameEntry is None):
         entry = newGameEntry(game["Game_Id"], game)
         lt.addLast(entry["lstgames"], game)
         m.put(gamesIndex, game["Game_Id"], entry)
    else:
         entry = me.getValue(gameEntry)
         lt.addLast(entry["lstgames"], game)
    
    return gameEntry

def addDateRecordIndex(dateEntry,record):
    lst = dateEntry["lstrecords"]
    lt.addLast(lst,record)
    recordsIndex = dateEntry["recordsIndex"]
    
    recordEntry = m.get(recordsIndex, record["Game_Id"])
    if (recordEntry is None):
         entry = newRecordEntry(record["Game_Id"], record)
         lt.addLast(entry["lstrecords"], record)
         m.put(recordsIndex, record["Game_Id"], entry)
    else:
         entry = me.getValue(recordEntry)
         lt.addLast(entry["lstrecords"], record)
    
    return recordEntry


def newGameEntry(gameMap,game):
    entry = {"gamesIndex":gameMap,
            "lstgames":lt.newList('SINGLE_LINKED')   }
    lt.addLast(entry["lstgames"],game)
    return entry

def newRecordEntry(recordMap,record):
    entry = {"recordsIndex":recordMap,
            "lstrecords":lt.newList('SINGLE_LINKED')   }
    lt.addLast(entry["lstrecords"],record)
    return entry

def newDateGameEntry(game):
    entry = {"gamesIndex":m.newMap(numelements=5,maptype='PROBING'),
            "lstgames":lt.newList('SINGLE_LINKED')   }
    lt.addLast(entry["lstgames"],game)
    return entry

def newDateRecordEntry(record):
    entry = {"recordsIndex":m.newMap(numelements=5,maptype='PROBING'),
            "lstrecords":lt.newList('SINGLE_LINKED')   }
    lt.addLast(entry["lstrecords"],record)
    return entry

def pruebas(analyzer):
    cosas = (om.get(analyzer["dateGame"],datetime.strptime('15-12-01',"%y-%m-%d"))["value"]["lstgames"])
    for k in lt.iterator(cosas):
        print(k)