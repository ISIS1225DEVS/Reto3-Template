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

# Inicialización del Catálogo de libros
def initAnalyzer():
    return model.newAnalyzer

# Funciones para la carga de datos
def loadData(analyzer):
    loadTracks(analyzer)
    loadCaracterisiticas(analyzer)

def loadTracks(analyzer):
    tracks_file = cf.data_dir + "context_content_features-small.csv"
    input_file = csv.DictReader(open(tracks_file, encoding='utf-8'),delimiter='\t')
    for categoria in input_file:
        model.addCanciones(analyzer,categoria)

def loadCaracterisiticas(analyzer):
    caracteristics_file = cf.data_dir + "context_content_features-small.csv"
    input_file = csv.DictReader(open( caracteristics_file, encoding='utf-8'),delimiter='\t')
    for categoria in input_file:
        model.addCaracterisitica(analyzer,categoria)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def requerimiento1(analyzer, caracteristica, valor_min, valor_max):

    return model.requerimiento1(analyzer, caracteristica, valor_min, valor_max)

def requerimiento2(analyzer, min_energy, max_energy, min_danceability, max_danceability):

    return model.requerimiento2(analyzer, min_energy, max_energy, min_danceability, max_danceability)