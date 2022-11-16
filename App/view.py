"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

gamefile = "Speedruns//game_data_utf-8-small.csv"
categoryfile = "Speedruns//category_data_urf-8-small.csv"

catalog = None

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Req 1")
    print("3- Req 2")
    print("4- Req 3")
    print("5- Req 4")
    print("6- Req 5")
    print("7- Req 6")
    print("8- Req 7")
    print("9- Req 8 (Bono)")

"""
Menu principal
"""
print("\nInicializando Catálogo ....")
catalog = controller.initCatalog()
    
while True:
    printMenu()
    inputs = input('Selecciona una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        controller.loadData(catalog,gamefile,categoryfile)
        print("\nInformacion cargada exitosamente\n")

    elif int(inputs[0]) == 2:
        print("Ejecutando requerimiento 1")
        floor = input("Escriba la fecha inicial: ")
        ceiling = input("Escriba la fecha final: ")
        controller.req1(catalog,floor,ceiling)
    elif int(inputs[0]) == 3:
        print("Ejecutando requerimiento 2")
        player = input("Escriba el nombre del jugador: ")
        controller.req2(catalog,player)
    elif int(inputs[0]) == 4:
        print("Ejecutando requerimiento 3")
        floor = input("Escriba el numero menor de intentos: ")
        ceiling = input("Escriba el numero mayor de intentos: ")
        controller.req3(catalog,floor,ceiling)
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass
    elif int(inputs[0]) == 7:
        pass
    elif int(inputs[0]) == 8:
        pass
    elif int(inputs[0]) == 9:
        print("Ejecutando requerimiento 8 - bono")
        release_year = input("Ingresa el anio a buscar: ")
        controller.bono(catalog,release_year)
    elif int(inputs[0])==0:
        controller.pruebas(catalog)
    else:
        sys.exit(0)
sys.exit(0)
