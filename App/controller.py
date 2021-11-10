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
def cargarDatos(): 
    catalogo=model.crearCatalogo()
    cargarCasos(catalogo)
    cargarDatesIndex(catalogo) 
    cargarHoursIndex(catalogo)
    cargarLongitudesIndex(catalogo)
    return catalogo 

# Funciones para la carga de datos
def cargarCasos(catalog):
    ufofile = cf.data_dir + "UFOS/UFOS-utf8-small.csv" 
    input_file = csv.DictReader(open(ufofile, encoding="utf-8"),
                                delimiter=",")
    for caso in input_file:
        model.addCasos(catalog, caso)

def cargarDatesIndex(catalog): 
    model.addDateIndex(catalog) 

def cargarHoursIndex(catalog):
    model.addHoursIndex(catalog)

def cargarLongitudesIndex(catalog):
    model.addLongitudIndex(catalog)  
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def casosPorCiudad(catalog,ciudad):
    listR=model.casosPorCiudad(catalog,ciudad) 
    return listR 

def casosPorHoras(catalog,rangoInferior,rangoSuperior):
    listR=model.casosPorHoras(catalog,rangoInferior,rangoSuperior)
    return listR     

def casosPorFechas(catalog,rangoInferior,rangoSuperior):
    listR=model.casosPorFechas(catalog,rangoInferior,rangoSuperior)          
    return listR

def casosPorArea(catalog,longitudMin,longitudMax,latitudMin,latitudMax):
    listaOrdenadaPorLongitud=model.casosPorLongitud(catalog,longitudMin,longitudMax)
    listaOrdenadaPorLatitud=model.casosPorLatitud(listaOrdenadaPorLongitud,latitudMin,latitudMax)
    
    return listaOrdenadaPorLatitud