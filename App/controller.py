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
csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newAnalyzer()
    return catalog


# Funciones para la carga de datos
def loadData(catalog,gamesfile,categoryfile):
    """
    Carga los datos de los archivos CSV en la
    estructura de datos
    """
    gamesfile = cf.data_dir + gamesfile
    categoryfile = cf.data_dir + categoryfile
    
    input_games_file = csv.DictReader(open(gamesfile, encoding="utf-8"),
                                delimiter=",")
    input_category_file = csv.DictReader(open(categoryfile, encoding="utf-8"),delimiter=",")

    for game in input_games_file:
        model.addGame(catalog, game)

    for record in input_category_file:
        model.addRecord(catalog,record)
        
    
    return catalog

def req1(catalog,floor,ceiling):
    return model.req1(catalog,floor,ceiling)

def req2(catalog,player):
    return model.req2(catalog,player)

def req3(catalog,floor,ceiling):
    return model.req3(catalog,int(floor),int(ceiling))

def bono(catalog,release_year):
    return model.bono(catalog,release_year)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def pruebas(analyzer):
    model.pruebas(analyzer)