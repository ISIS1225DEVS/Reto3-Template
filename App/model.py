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

#•••••••••••••••••••••••••••••••••••••••••
#   Importaciones
#•••••••••••••••••••••••••••••••••••••••••

import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
assert cf
import datetime
from DISClib.ADT import map as m





#•••••••••••••••••••••••••••••••••••••••••
#   Inicializacion del catalogo
#•••••••••••••••••••••••••••••••••••••••••

def newAnalyzer():
    """ Inicializa el analizador
    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas
    Retorna el analizador inicializado.
    """
    
    #analyzer['dateIndex'] = om.newMap(omaptype='RBT',
     #                                 comparefunction=compareDates)
    
    analyzer = mp.newMap(
                        2,
                        maptype = "CHAINING",
                        loadfactor = 4.0,
                        comparefunction = None
                    )

    mp.put(
            analyzer,
            "cases",
            lt.newList('ARRAY_LIST')
            )

    mp.put(
            analyzer,
            "casesSize",
            lt.size(me.getValue(mp.get(analyzer, "cases"))) 
            )

    return analyzer




#•••••••••••••••••••••••••••••••••••••••••
#Funciones de consulta
#•••••••••••••••••••••••••••••••••••••••••

def getCasesByCity(analyzer, city):

    """
    
        Responde al requerimiento 1.

    """

    return None

#----------------------------------------

def getCasesBetweeenSeconds(analyzer, beginSeconds, endSeconds):

    """
    
        Responde al requerimiento 2.

    """

    return None

#----------------------------------------

def getCasesBetweeenHours(analyzer, beginHour, endHour):

    """
    
        Responde al requerimiento 3.

    """

    return None





#•••••••••••••••••••••••••••••••••••••••••
# Funciones para agregar informacion al catalogo
#•••••••••••••••••••••••••••••••••••••••••

def addCase(analyzer, case):
    """
    """
    lt.addLast(me.getValue(mp.get(analyzer, "cases")), case)
    return analyzer






#•••••••••••••••••••••••••••••••••••••••••
# Funciones para creacion de datos
#•••••••••••••••••••••••••••••••••••••••••





#•••••••••••••••••••••••••••••••••••••••••
# Funciones adicionales
#•••••••••••••••••••••••••••••••••••••••••

def getCasesSize(analyzer):
    return lt.size(me.getValue(mp.get(analyzer, "cases")))



#•••••••••••••••••••••••••••••••••••••••••
# Funciones de comparacion
#•••••••••••••••••••••••••••••••••••••••••

def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

#----------------------------------------





#•••••••••••••••••••••••••••••••••••••••••
# Funciones de ordenamiento
#•••••••••••••••••••••••••••••••••••••••••