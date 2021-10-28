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
from App.model import OrderedArtist
import config as cf
import model
import csv



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def initCatalog():
    ana = model.initCatalog()
    return ana

def loadData(ana):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    UFOf = cf.data_dir + 'UFOS-utf8-small.csv'
    inputfile = csv.DictReader(open(UFOf, encoding="utf-8"),delimiter=",")
    for avist in inputfile:
        model.addAvist(ana, avist)
    return ana
# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo


def getcityadvis(catalog, City):
    cityLt = model.addAvist(catalog, City)
    return cityLt

def getltDates(cityLt):
    ltDates= model.ltDates(cityLt)
    return ltDates

def getOrderedlt(ltDates):
    Orderedlt = model.Orderedlt(ltDates)
    return Orderedlt

def getOrderedArtist(Orderedlt, cityLt ):
    ordered= model.OrderedArtist(Orderedlt, cityLt)
    return OrderedArtist

def gettop3fi(ordered):
    firsts = model.top3fi(ordered)
    return firsts
def gettop3la(ordered):
    latests= model.top3la(ordered)
    return ordered

