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
 """

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

#•••••••••••••••••••••••••••••••••••••••••
#   Importaciones
#•••••••••••••••••••••••••••••••••••••••••

import config as cf
import model
import csv
from datetime import datetime
from DISClib.ADT import map as mp





#•••••••••••••••••••••••••••••••••••••••••
#   Inicializacion del catalogo
#•••••••••••••••••••••••••••••••••••••••••

def init():

    analyzer = model.newAnalyzer()

    return analyzer





#•••••••••••••••••••••••••••••••••••••••••
# Funciones para la carga de datos
#•••••••••••••••••••••••••••••••••••••••••

def loadData(analyzer, ufosFile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    ufosFile = cf.data_dir + ufosFile
    input_file = csv.DictReader(open(ufosFile, encoding="utf-8"),
                                delimiter=",")
    for case in input_file:
        model.addCase(analyzer, case)

    sorted = model.sortByDate(analyzer)
    mp.put(analyzer, "cases", sorted)

    analyzer = model.firstAndLastFiveCases(analyzer)

    return analyzer





#•••••••••••••••••••••••••••••••••••••••••
#Funciones de consulta
#•••••••••••••••••••••••••••••••••••••••••

def getCasesByCity(analyzer, city):
    return model.getCasesByCity(analyzer, city)

#----------------------------------------

def getCasesBetweeenSeconds(analyzer, beginSeconds, endSeconds):
    return model.getCasesBetweeenSeconds(analyzer, beginSeconds, endSeconds)

#----------------------------------------

def getCasesBetweeenHours(analyzer, beginHour, endHour):
    return model.getCasesBetweeenHours(analyzer, beginHour, endHour)

#----------------------------------------



# Funciones de ordenamiento


#•••••••••••••••••••••••••••••••••••••••••
#Funciones de consulta
#•••••••••••••••••••••••••••••••••••••••••

def getCasesSize(analyzer):
    return model.getCasesSize(analyzer)