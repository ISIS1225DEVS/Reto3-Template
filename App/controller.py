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

import config as cf
import model
import datetime
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Analizador

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    analizer = model.newAnalyzer()
    return analizer

# Funciones para la carga de datos

def loadData(analizer, ufosfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    ufosfile = cf.data_dir + ufosfile
    input_file = csv.DictReader(open(ufosfile, encoding = "utf-8"), delimiter = ",")
    for ufo in  input_file:
        model.addUFO(analizer, ufo)
    return analizer

# Funciones para consultas

def sightingsByCity(analyzer, city):
   'Req 1'
   return model.sightingsByCity(analyzer, city)

def sightingsByDuration(analyzer, minTime, maxTime):
    'Req 2'
    return model.sightingsByDuration(analyzer, minTime, maxTime)

def ufosSize(analyzer):
    """
    Numero de UFOS leidos
    """
    return model.ufosSize(analyzer)

def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)

def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)

def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

