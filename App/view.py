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
from DISClib.ADT import orderedmap as om
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("  1- Inicializar Catálogo")
    print("  2- Cargar información en el catálogo")
    print("  3- Cargar requerimiento 1.")
    print("  4- Cargar requerimiento 2.")
    print("  5- Cargar requerimiento 3.")
    print("  6- Cargar requerimiento 4.")
    print("  7- Cargar requerimiento 5.")


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        contr = controller.initCatalog()
        print("Catálogo Inicializado\n")

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....\n")
        controller.loadData(contr)
        print("Avistamientos:", str(controller.AvistamientosSize(contr)), "\n")
        print("Altura:", str(controller.height(contr)), "\n")
        print("Elementos:", str(controller.size(contr)), "\n")
        
    
    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass
    else:
        sys.exit(0)


      
sys.exit(0)


