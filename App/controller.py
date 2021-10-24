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
def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalogo = model.newCatalog()
    return catalogo
# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento de datos en EL modelo
# ___________________________________________________
def loadData(catalogo, UFOfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    UFOfile = cf.data_dir + UFOfile
    input_file = csv.DictReader(open(UFOfile, encoding="utf-8"),
                                delimiter=",")
    for registro in input_file:
        model.addRegistro(catalogo, registro)
    return catalogo

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
#REQ1#
def registrosPorCiudad(catalogo,nombreCiudad):
    registros=model.registrosPorCiudad(catalogo,nombreCiudad)
    return registros
#REQ2#
def registrosEnRangoDuracion(catalogo,limiteMaximo,limiteMinimo):
    registros=model.registrosEnRangoDuracion(catalogo,limiteMaximo,limiteMinimo)
    return registros
#REQ3
def NumAvistamientosPorHoraMinuto (catalogo,inferior,superior):
    rta=model.NumAvistamientosPorHoraMinuto(catalogo,inferior,superior)
    return(rta)
#funciones de consulta om#
def registrosSize(analyzer):
    """
    Numero de registros leidos
    """
    return model.registrosSize(analyzer)

def indexHeight(analyzer,indice):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer,indice)


def indexSize(analyzer,indice):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer,indice)


def minKey(analyzer,indice):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer,indice)


def maxKey(analyzer,indice):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer,indice)