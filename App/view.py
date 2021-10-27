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
from DISClib.ADT import orderedmap as omap
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Cargar información en el catálogo") #Se cargan los datos del catálogo
    #print("2- Contar los avistamientos en una ciudad")
    print("3- Contar los avistamientos por duración") #Desplegar datos para la opción 3
    #print("4- Contar los avistamientos por Hora/Minutos del día")
    #print("5- Contar los avistamientos en un rango de fechas")
    #print("6- Contar los avistamientos de una Zona Geográfica")
    print("0- Salir")
    print("*******************************************")

catalog = None

def CreateCatalog():
    return controller.CreateCatalog()

def AddDates(catalog):
    return controller.AddDates(catalog)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = CreateCatalog()
        AddDates(catalog)
        #print(catalog)

    elif int(inputs[0]) == 2:
        pass

    elif int(inputs[0]) == 3:
        print("La altura del árbol es: "+str(omap.height(catalog["dates"])))
        print("El número de elementos en el árbol es: "+str(omap.size(catalog["dates"])))

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass
    else:
        sys.exit(0)
sys.exit(0)
