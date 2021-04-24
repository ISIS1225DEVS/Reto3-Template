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
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo
def init():
    analyzer = model.newAnalyzer()
    return analyzer
# Funciones para la carga de datos
def loadData(analyzer, songsfile):
    songsfile = cf.data_dir + songsfile
    input_file = csv.DictReader(open(songsfile, encoding="utf-8"), delimiter=",")
    for song in input_file:
        model.add_song(analyzer, song)
    return analyzer
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def crimesSize(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.crimesSize(analyzer)


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


def Requerimiento1(analyzer, initialInstru, finalInstru, caract):
    return model.Requerimiento1(analyzer, initialInstru, finalInstru, caract)
def Requerimiento2(analyzer, menorEnergy, mayorEnergy, menorDance, mayorDance):
    return model.Requerimiento2(analyzer, menorEnergy, mayorEnergy, menorDance, mayorDance)