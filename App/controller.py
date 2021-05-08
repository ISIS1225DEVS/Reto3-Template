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

from DISClib.ADT import list as lt
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def init():
    database = model.newdatabase()
    return database

# Funciones para la carga de datos

def loadevent(database):
    videosfile = cf.data_dir + 'context_content_features-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for event in input_file:
        model.addevent(database, event)
    return database

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def indexHeight(database):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(database)

def indexSize(database):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(database)

def Requerimiento1(database, characteristic, minvalue, maxvalue):
    sol = model.Requerimiento1(database, characteristic, minvalue, maxvalue)
    return sol 

def Requerimiento3(database, minvalue_instru, maxvalue_instru, minvalue_tempo, maxvalue_tempo):
    sol = model.Requerimiento3(database, minvalue_instru, maxvalue_instru, minvalue_tempo, maxvalue_tempo)
    return sol 
