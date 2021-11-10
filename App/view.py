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
from DISClib.ADT import map as mp
assert cf
import datetime
import time
default_limit=1000
sys.setrecursionlimit(default_limit*10)


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
        # print("Total de avistamientos cargados: "+ str(info[0]))
        # print("Los primeros 5 avistamientos son:")
        # print(info[1])
        # print("Los últimos 5 avistamientos son:")
        # print(info[2])

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
    elif int(inputs[0]) == 4:
        lowhour = input('Hora Inicial (HH:MM): ')
        highhour = input('Hora Final (HH:MM): ')
        older_hour = controller.older_hour(catalog)
        hours_in_range = controller.hours_in_range(catalog, lowhour, highhour)
        size_range = controller.size_in_range(hours_in_range)
        primeros = []
        ultimos = []
        Primeros = lt.subList(hours_in_range,1,3)
        Ultimos = lt.subList(hours_in_range,-2,3)
        lst_olders = []
        j = 0
        while j < 1:
            last = lt.removeLast(older_hour)
            k = last['first']['info']
            date = datetime.datetime.strptime(k['datetime'], '%Y-%m-%d %H:%M:%S')
            date2 = date.time()
            size_older = last['size']
            j += 1
            lst_olders.append((str(date2),size_older))
        for actual in lt.iterator(Primeros):
            dict = {}
            dict["datetime"]= actual["datetime"]
            dict["location"]= actual["city"] + ", "+ actual["country"]
            dict["duration (secs.)"]= actual["duration (seconds)"]
            dict["shape"]= actual["shape"]
            primeros.append(dict)
        for actual in lt.iterator(Ultimos):
            dict = {}
            dict["datetime"]= actual["datetime"]
            dict["location"]= actual["city"] + ", "+ actual["country"]
            dict["duration (secs.)"]= actual["duration (seconds)"]
            dict["shape"]= actual["shape"]
            ultimos.append(dict)

        print('')
        print('Ejecutando...')
        print('')
        print('El avistamiento más tardío es: ', lst_olders)
        print('Los números de avistamientos dentro del rango de fechas son: ', size_range)
        print('Los primeros 3 avistamientos en el rango son: ', )
        for a in primeros:
            print(a)
        print('Los últimos 3 avistamientos en el rango son: ', )
        for a in ultimos:
            print(a)

    elif int(inputs[0]) == 5:
        lowdate = input('Fecha Inicial (YYYY-MM-DD): ')
        highdate = input('Fecha Final (YYYY-MM-DD): ')
        older_date = controller.older_sightings(catalog)
        dates_in_range = controller.dates_in_range(catalog,lowdate,highdate)
        size_range = controller.size_in_range(dates_in_range[0])
        primeros = []
        ultimos = []
        lst_olders = []
        j = 0
        for i in lt.iterator(older_date):
            k = i['first']['info']
            if j < 1:
                date = datetime.datetime.strptime(k['datetime'], '%Y-%m-%d %H:%M:%S')
                date2 = date.date()
                size_older = i['size']
                j += 1
                lst_olders.append((str(date2),size_older))
        for i in lt.iterator(dates_in_range[1]):
            for j in lt.iterator(i):
                dict = {}
                dict["datetime"]= j["datetime"]
                dict["location"]= j["city"] + ", "+ j["country"]
                dict["duration (secs.)"]= j["duration (seconds)"]
                dict["shape"]= j["shape"]
                primeros.append(dict)
        for i in lt.iterator(dates_in_range[2]):
            for j in lt.iterator(i):
                dict = {}
                dict["datetime"]= j["datetime"]
                dict["location"]= j["city"] + ", "+ j["country"]
                dict["duration (secs.)"]= j["duration (seconds)"]
                dict["shape"]= j["shape"]
                ultimos.append(dict)
        print('')
        print('Ejecutando...')
        print('')
        print('La fecha más antiguas es: ', lst_olders)
        print('Los números de avistamientos dentro del rango de fechas son: ', size_range)
        print('Los primeros 3 avistamientos en el rango son: ', )
        for a in primeros:
            print(a)
        print('Los últimos 3 avistamientos en el rango son: ', )
        for a in ultimos:
            print(a)
    else:
        sys.exit(0)
sys.exit(0)
