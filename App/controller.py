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
def CreateCatalog():
    return model.CreateCatalog() #Se llama a la función que crea el catalogo

# Funciones para la carga de datos
def AddData(catalog):
    UFOS_file = cf.data_dir + "UFOS-utf8-small.csv" #Se coloca la ruta del archivo
    data = csv.DictReader(open(UFOS_file, encoding="utf-8"),delimiter=",") #Se lee todo el .csv
    for sighting in data: #Por cada fila del .csv
        model.AddDates(catalog, sighting) #Se añade las fechas
        model.addCity(catalog, sighting) # Se añade la ciudad

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
