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
import time
import sys
import controller
from prettytable import PrettyTable
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

UFOfile = 'UFOS-utf8-small.csv'
# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Consultar el número de avistamientos en una ciudad")
    print("2- Consultar el número de avistamientos por duración")
    print("3- Consultar el número de avistamientos por hora y minuto del día")
    print("4- Consultar el número de avistamientos en un rango de fechas")
    print("5- Consultar el número de avistamientos de una zona geográfica")
    print("10-Salir ")

#Funciones para imprimir#
def printRegistro(lista):
    x = PrettyTable() 
    x.field_names = ["Fecha y hora","Ciudad", "Estado", "Pais", "Forma","Duracion (segundos)"]
    for i in lt.iterator(lista):
        x.add_row([str(i["fechahora"]),str(i["ciudad"]),str(i["estado"]),str(i["pais"]),
            str(i["forma"]),str(i["duracionsegundos"])])
        x.max_width = 20
    print(x)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        start_time = time.process_time()
        print("Cargando información de los archivos ....")
        catalogo = controller.init()
        controller.loadData(catalogo, UFOfile)
        print("El total de avistamientos cargados:"+ str(controller.registrosSize(catalogo)))
        primeras= lt.subList(catalogo["registros"],1,5)
        ultimas= lt.subList(catalogo["registros"],lt.size(catalogo["registros"])-4,5)
        print("Los primeros 5 registros cargados son:")  
        printRegistro(primeras)
        print("Los ultimos 5 registros cargados son:") 
        printRegistro(ultimas)
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))
    elif int(inputs[0]) == 1:
        print("información Arbol con indice=ciudad")
        print('Altura del arbol: ' + str(controller.indexHeight(catalogo,"indiceCiudad")))
        print('Elementos en el arbol: ' + str(controller.indexSize(catalogo,"indiceCiudad")))
        print('Menor Llave: ' + str(controller.minKey(catalogo,"indiceCiudad")))
        print('Mayor Llave: ' + str(controller.maxKey(catalogo,"indiceCiudad")))
        nombreCiudad = input('Nombre de la ciudad a consultar\n')
        registrosCiudad= controller.registrosPorCiudad(catalogo,nombreCiudad)
        if registrosCiudad==None:
            print("Ciudad no encontrada")
        else:
            print("El total de avistamientos en "+ nombreCiudad+ " es: "+ str(lt.size(registrosCiudad)))
            
            if lt.size(registrosCiudad) <= 3:
                print("Hay 3 o menos registros, estos son:")
                printRegistro(registrosCiudad)
            elif lt.size(registrosCiudad) > 3:
                primeras= lt.subList(registrosCiudad,1,3)
                ultimas= lt.subList(registrosCiudad,lt.size(registrosCiudad)-2,3)
                print("Los primeros 3 registros son:")  
                printRegistro(primeras)
                print("Los ultimos 3 registros son:") 
                printRegistro(ultimas)
    elif int(inputs[0]) == 2:
        print("información Arbol con indice=duracion")
        print('Altura del arbol: ' + str(controller.indexHeight(catalogo,"indiceDuracion")))
        print('Elementos en el arbol: ' + str(controller.indexSize(catalogo,"indiceDuracion")))
        print('Menor Llave: ' + str(controller.minKey(catalogo,"indiceDuracion")))
        print('Mayor Llave: ' + str(controller.maxKey(catalogo,"indiceDuracion")))
        limiteMaximo = float(input('Ingrese el límite inferior en segundos (máximo):  '))
        limiteMinimo = float(input('Ingrese el límite superior en segundos (mínimo):  '))
        registrosEnRango= controller.registrosEnRangoDuracion(catalogo,limiteMaximo,limiteMinimo)
        if registrosEnRango==None or lt.size(registrosEnRango)==0:
            print("No se encontraron avistaamientos, en este rango. Revise el orden de entrada")
        else:
            print("El total de avistamientos entre "+ str(limiteMinimo)+ " y "+
                     str(limiteMaximo)+" es: "+ str(lt.size(registrosEnRango)))
            if lt.size(registrosEnRango) <= 3:
                print("Hay 3 o menos registros, estos son:")
                printRegistro(registrosEnRango)
            elif lt.size(registrosEnRango) > 3:
                primeras= lt.subList(registrosEnRango,1,3)
                ultimas= lt.subList(registrosEnRango,lt.size(registrosEnRango)-2,3)
                print("Los primeros 3 registros son:")  
                printRegistro(primeras)
                print("Los ultimos 3 registros son:") 
                printRegistro(ultimas)
    elif int(inputs[0]) > 1:
        print("No disponible")
        pass
    else:
        sys.exit(0)

