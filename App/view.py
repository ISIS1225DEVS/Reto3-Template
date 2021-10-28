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

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Contar los avistamientos en una ciudad") #FALTA POR PENSAR
    print("3- Contar los avistamientos por duración")#MAPA ORDENADO SEGÚN LA DURACIÓN DE LOS EVENTOS(LLAVE), DENTRO DE CADA LLAVE ESTARÁ UNA LISTA ORDENADA SEGÚN DISCORD (VER LA PREGUNTA)
    print("4- Contar avistamientos por Hora/Minutos del día") # MAPA ORDENADO SEGÚN DATATIME(LLAVE), DENTRO DE CADA LLAVE HABRÁ UNA LISTA QUE CONTENGA LOS EVENTOS EN ESA FECHA
    print("5- Contar los avistamientos en un rango de fechas") #USAR EL MAPA ORDENADO SEGÚN DATATIME Y LISTAR LOS DATOS REGISTRADOS SEGÚN UN RANGO DE FECHAS
    print("6- Contar los avistamientos de una Zona Geográfica") #ESPERAR RESPUESTA DE LINDSAY
    print("7- Visualizar los avistamientos de una zona geográfica") #MOSTRAR EN EL MAPA EL ÁREA EN EL QUE ENTRA EL RANGO 

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        catalog = controller.InitCatalog()
        print('Se ha inicializado el Catalog_UFOS...')
        ufofile = input("Escriba el nombre del archivo que desea cargar:\n1) small\n2) 5pct\n3) 10pct\n4) 20pct\n5) 30pct\n6) 50pct\n7) 80pct\n9) large\n")
        if ufofile == 'small' or ufofile == 'large':
            ufofile = 'UFOS-utf8-'+ufofile+'.csv'
        else:
            ufofile = 'UFOS-utf8-'+ufofile+'.csv'
        controller.loadData(catalog,ufofile)
        print('Se han cargado los datos...')
        info= controller.total_sightings(catalog)
        print("Total de avistamientos cargados: "+ str(info[0]))
        print("Los primeros 5 avistamientos son:")
        print(info[1])
        print("Los últimos 5 avistamientos son:")
        print(info[2])

    elif int(inputs[0]) == 2:
        ciudad= input("Ingrese el nombre de la ciudad a consultar: ")
        info= controller.sightings_by_city(catalog,ciudad)
        print("Hay "+ str(info[0])+ " diferentes ciudades con avistamientos de UFOs...")
        print("Hubo un total de " + str(info[1])+" avistamientos en la ciudad de "+ ciudad+ "...")
        print("Los primeros tres avistamientos en dicha ciudad son:")
        primeros= []
        for sighting in lt.iterator(info[2]):
            dict={}
            dict["datetime"]= sighting["datetime"]
            dict["location"]= sighting["city"] + ", "+ sighting["country"]
            dict["duration (secs.)"]= sighting["duration (seconds)"]
            dict["shape"]= sighting["shape"]
            primeros.append(dict)
        for dict in primeros:
            print(dict)
        print("Los últimos tres avistamientos en dicha ciudad son:")
        ultimos= []
        for sighting in lt.iterator(info[3]):
            dict={}
            dict["datetime"]= sighting["datetime"]
            dict["location"]= sighting["city"] + ", "+ sighting["country"]
            dict["duration (secs.)"]= sighting["duration (seconds)"]
            dict["shape"]= sighting["shape"]
            ultimos.append(dict)
        for dict in ultimos:
            print(dict)
        print("="*40)
        info= controller.size_city_tree(catalog)
        print("El número de elementos dentro del árbol implementado para este requerimiento es: "+ str(info[0]))
        print("La altura del árbol implementado para este requerimiento es: "+ str(info[1]))
        print("="*40)
        
    else:
        sys.exit(0)
sys.exit(0)
