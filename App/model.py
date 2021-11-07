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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

#•••••••••••••••••••••••••••••••••••••••••
#   Importaciones
#•••••••••••••••••••••••••••••••••••••••••

import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
assert cf
from datetime import datetime, time
from DISClib.ADT import map as m
from prettytable import PrettyTable





#•••••••••••••••••••••••••••••••••••••••••
#   Inicializacion del catalogo
#•••••••••••••••••••••••••••••••••••••••••

def newAnalyzer():
    """ Inicializa el analizador
    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas
    Retorna el analizador inicializado.
    """
    
    analyzer = mp.newMap(
                        2,
                        maptype = "CHAINING",
                        loadfactor = 4.0,
                        comparefunction = None
                    )

    mp.put(
            analyzer,
            "cases",
            lt.newList('ARRAY_LIST')
            )

    mp.put(
            analyzer,
            "casesSize",
            lt.size(me.getValue(mp.get(analyzer, "cases"))) 
            )

    mp.put(
            analyzer,
            "casesByCity",
            om.newMap(  omaptype='RBT',
                        comparefunction=None)
            )

    mp.put(
            analyzer,
            "casesBySeconds",
            om.newMap(  omaptype='RBT',
                        comparefunction=None)
            )

    mp.put(
            analyzer,
            "casesByHour",
            om.newMap(  omaptype='RBT',
                        comparefunction=None)
            )

    return analyzer


#•••••••••••••••••••••••••••••••••••••••••
#Funciones de consulta
#•••••••••••••••••••••••••••••••••••••••••

def getCasesByCity(analyzer, ciity):

    """
    
        Responde al requerimiento 1.

    """

    # Se extrae el mapa de avistamientos
    cases = me.getValue(mp.get(analyzer, "cases"))

    # Se guarda en una lista todas las ciudades
    cityKeys = lt.newList("ARRAY_LIST")
    
    # Se revisan las ciudades de cada avistamiento, si no se ha agregado la ciudad al mapa que indica
    # los avistamientos por ciudad, se grega la ciudad con una lista vacia como valor
    for i in lt.iterator(cases):
        if om.contains(me.getValue(mp.get(analyzer, "casesByCity")), i["city"]) == False:
            lt.addLast(cityKeys, i["city"])
            om.put(me.getValue(mp.get(analyzer, "casesByCity")), i["city"], lt.newList("ARRAY_LIST"))

    # Se añade cada caso de avistamiento a lista que corresponde a los casos de avistamientos de cada
    # ciudadas anteriormente
    for i in lt.iterator(cases):
        lt.addLast(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByCity")), i["city"])), i)

    # Se eliminan los avistamientos duplicados en cada ciudad
    for i in lt.iterator(cityKeys):
        pos = 2
        while pos <= lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByCity")), i))):
            lt.deleteElement(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByCity")), i)), pos)
            pos += 2
            pos -=1
        om.put(me.getValue(mp.get(analyzer, "casesByCity")), i, me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByCity")), i)))

    # Se incializa un nuevo mapa
    outMap = mp.newMap(
           2,
           maptype = "CHAINING",
           loadfactor = 4.0,
           comparefunction = None
       )

    mp.put( outMap,
            "totalCities",
            None)

    mp.put( outMap,
            "casesByCity",
            None
            )
    
    mp.put( outMap,
            "top5NCases",
            None
            )

    mp.put( outMap,
            "nCasesByCity",
            None
            )

    mp.put( outMap,
            "recentAndOlderCasesByCity",
            None
            )


    # Se cargan los datos al mapa

    # Se carga la cantidad de ciudades en donde se presentaron avistamientos.
    mp.put( outMap,
            "totalCities",
            lt.size(cityKeys))

    # Se cargan los avistamientos por ciudad
    mp.put( outMap,
            "casesByCity",
            me.getValue(mp.get(analyzer, "casesByCity"))
            )

    # Se crea una nueva lista para almacenar las ciudades y cantidades de avistamientos
    # en esta ciudad
    citiesAndNCases = lt.newList("ARRAY_LIST")

    # Se cargan los datos a la lista creada
    for i in lt.iterator(cityKeys):
        city = {"city": None,
                "nCases": None
                }

        city["city"] = i
        city["nCases"] = lt.size(me.getValue(om.get(me.getValue(mp.get(outMap, "casesByCity")), i)))
        lt.addLast(citiesAndNCases, city)

    # Se ordenan los datos de la lista creada de mayor a menos segun el numero de avistamientos
    # en cada ciudad
    sortByNCases(citiesAndNCases)

    #Se crea una nueva lista para almacenar las 5 ciudades con mayor numero de avistamientos
    topCitiesAndNCases = lt.newList("ARRAY_LIST")
    lt.addLast(topCitiesAndNCases, lt.getElement(citiesAndNCases, 1))
    lt.addLast(topCitiesAndNCases, lt.getElement(citiesAndNCases, 2))
    lt.addLast(topCitiesAndNCases, lt.getElement(citiesAndNCases, 3))
    lt.addLast(topCitiesAndNCases, lt.getElement(citiesAndNCases, 4))
    lt.addLast(topCitiesAndNCases, lt.getElement(citiesAndNCases, 5))

    # Se carga la lista creada anteriormente
    mp.put( outMap,
            "top5NCases",
            topCitiesAndNCases
            )

    # Se guarda el numero de avistamientos en una ciudad especifica dada por el usuario.
    mp.put( outMap,
            "nCasesByCity",
            lt.size(me.getValue(om.get(me.getValue(mp.get(outMap, "casesByCity")), ciity)))
            )

    # Se crea una nueva lista para guardar los tres avistamientos mas antiguos y mas recientes de
    # ciudad dada por el usuario.        
    recentAndOlderCasesByCity = lt.newList("ARRAY_LIST")
    lt.addLast(recentAndOlderCasesByCity, lt.getElement(me.getValue(om.get(me.getValue(mp.get(outMap, "casesByCity")), ciity)), 1))
    lt.addLast(recentAndOlderCasesByCity, lt.getElement(me.getValue(om.get(me.getValue(mp.get(outMap, "casesByCity")), ciity)), 2))
    lt.addLast(recentAndOlderCasesByCity, lt.getElement(me.getValue(om.get(me.getValue(mp.get(outMap, "casesByCity")), ciity)), 3))
    lt.addLast(recentAndOlderCasesByCity, lt.getElement(me.getValue(om.get(me.getValue(mp.get(outMap, "casesByCity")), ciity)), lt.size(me.getValue(om.get(me.getValue(mp.get(outMap, "casesByCity")), ciity)))-2))
    lt.addLast(recentAndOlderCasesByCity, lt.getElement(me.getValue(om.get(me.getValue(mp.get(outMap, "casesByCity")), ciity)), lt.size(me.getValue(om.get(me.getValue(mp.get(outMap, "casesByCity")), ciity)))-1))
    lt.addLast(recentAndOlderCasesByCity, lt.getElement(me.getValue(om.get(me.getValue(mp.get(outMap, "casesByCity")), ciity)), lt.size(me.getValue(om.get(me.getValue(mp.get(outMap, "casesByCity")), ciity)))))

    mp.put( outMap,
            "recentAndOlderCasesByCity",
            recentAndOlderCasesByCity
            )

    topFive = PrettyTable([   "City",
                            "Count"
                        ])
                        
    topFive.add_row([
                        lt.getElement(me.getValue(mp.get(outMap, "top5NCases")), 1)["city"],
                        lt.getElement(me.getValue(mp.get(outMap, "top5NCases")), 1)["nCases"]
                    ])

    topFive.add_row([
                        lt.getElement(me.getValue(mp.get(outMap, "top5NCases")), 2)["city"],
                        lt.getElement(me.getValue(mp.get(outMap, "top5NCases")), 2)["nCases"]
                    ])

    topFive.add_row([
                        lt.getElement(me.getValue(mp.get(outMap, "top5NCases")), 3)["city"],
                        lt.getElement(me.getValue(mp.get(outMap, "top5NCases")), 3)["nCases"]
                    ])

    topFive.add_row([
                        lt.getElement(me.getValue(mp.get(outMap, "top5NCases")), 4)["city"],
                        lt.getElement(me.getValue(mp.get(outMap, "top5NCases")), 4)["nCases"]
                    ])

    topFive.add_row([
                        lt.getElement(me.getValue(mp.get(outMap, "top5NCases")), 5)["city"],
                        lt.getElement(me.getValue(mp.get(outMap, "top5NCases")), 5)["nCases"]
                    ])

    firstAndLastThree = PrettyTable([   "Datetime",
                                        "City",
                                        "State",
                                        "Country",
                                        "Shape",
                                        "Duration (seconds)"
                                    ])

    firstAndLastThree.add_row([
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 1)["datetime"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 1)["city"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 1)["state"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 1)["country"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 1)["shape"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 1)["duration (seconds)"],
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 2)["datetime"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 2)["city"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 2)["state"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 2)["country"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 2)["shape"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 2)["duration (seconds)"],
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 3)["datetime"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 3)["city"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 3)["state"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 3)["country"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 3)["shape"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 3)["duration (seconds)"],
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 4)["datetime"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 4)["city"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 4)["state"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 4)["country"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 4)["shape"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 4)["duration (seconds)"],
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 5)["datetime"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 5)["city"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 5)["state"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 5)["country"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 5)["shape"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 5)["duration (seconds)"],
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 6)["datetime"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 6)["city"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 6)["state"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 6)["country"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 6)["shape"],
                        lt.getElement(me.getValue(mp.get(outMap, "recentAndOlderCasesByCity")), 6)["duration (seconds)"],
                    ])

    answer = f"\n================ Req No. 1 Inputs ================\n\nUFO Sightings in the city of: {ciity}.\n\n================ Req No. 1 answer ================\n\nThere are {me.getValue(mp.get(outMap, 'totalCities'))} different cities with UFO sightings.\n\n{topFive}\n\n There are {me.getValue(mp.get(outMap, 'nCasesByCity'))} sightings at the: {ciity} city.\n\nThe first 3 and last 3 UFO sightings are:\n\n{firstAndLastThree}\n"

    return answer

#----------------------------------------

def getCasesBetweeenSeconds(analyzer, beginSeconds, endSeconds):

    """
    
        Responde al requerimiento 2.

    """

    # Se extrae el mapa de avistamientos
    cases = me.getValue(mp.get(analyzer, "cases"))

    # Se guarda en una lista todas las ciudades
    secondsKeys = lt.newList("ARRAY_LIST")
    
    # Se revisan las ciudades de cada avistamiento, si no se ha agregado la ciudad al mapa que indica
    # los avistamientos por ciudad, se grega la ciudad con una lista vacia como valor
    for i in lt.iterator(cases):
        if om.contains(me.getValue(mp.get(analyzer, "casesBySeconds")), i["duration (seconds)"]) == False:
            lt.addLast(secondsKeys, i["duration (seconds)"])
            om.put(me.getValue(mp.get(analyzer, "casesBySeconds")), i["duration (seconds)"], lt.newList("ARRAY_LIST"))

    secondsKeys = sortSeconds(secondsKeys)

    secondsKeysInRange = lt.newList("ARRAY_LIST")
    
    for i in lt.iterator(secondsKeys):
        if float(i) >= float(beginSeconds) and float(i) <= float(endSeconds):
            lt.addLast(secondsKeysInRange, i)

    # Se añade cada caso de avistamiento a lista que corresponde a los casos de avistamientos de cada
    # ciudadas anteriormente
    for i in lt.iterator(cases):
        lt.addLast(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), i["duration (seconds)"])), i)

    # Se eliminan los avistamientos duplicados en cada ciudad
    for i in lt.iterator(secondsKeys):
        pos = 2
        while pos <= lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), i))):
            lt.deleteElement(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), i)), pos)
            pos += 2
            pos -=1
        om.put(me.getValue(mp.get(analyzer, "casesBySeconds")), i, me.getValue(om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), i)))

    casesInRange = lt.newList("ARRAY_LIST")

    for i in lt.iterator(secondsKeysInRange):
        lt.addLast(casesInRange, om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), i))

    topFiveDurations = PrettyTable([   "Duration (seconds)",
                            "Count"
                        ])
                        
    topFiveDurations.add_row([
                        lt.getElement(secondsKeys, lt.size(secondsKeys)),
                        lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), lt.getElement(secondsKeys, lt.size(secondsKeys)))))
                    ])

    topFiveDurations.add_row([
                        lt.getElement(secondsKeys, lt.size(secondsKeys)-1),
                        lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), lt.getElement(secondsKeys, lt.size(secondsKeys)-1))))
                    ])

    topFiveDurations.add_row([
                        lt.getElement(secondsKeys, lt.size(secondsKeys)-2),
                        lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), lt.getElement(secondsKeys, lt.size(secondsKeys)-2))))
                    ])

    topFiveDurations.add_row([
                        lt.getElement(secondsKeys, lt.size(secondsKeys)-3),
                        lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), lt.getElement(secondsKeys, lt.size(secondsKeys)-3))))
                    ])

    topFiveDurations.add_row([
                        lt.getElement(secondsKeys, lt.size(secondsKeys)-4),
                        lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), lt.getElement(secondsKeys, lt.size(secondsKeys)-4))))
                    ])

    nCases = 0
    onlyCasesInRange = lt.newList("ARRAY_LIST")

    for i in lt.iterator(secondsKeysInRange):
        nCases += lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), i)))
        for j in lt.iterator(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), i))):
            lt.addLast(onlyCasesInRange, j)

    onlyCasesInRange = sortDates(onlyCasesInRange)

    firstAndLastThree = PrettyTable([   "Datetime",
                                        "City",
                                        "State",
                                        "Country",
                                        "Shape",
                                        "Duration (seconds)"
                                    ])

    firstAndLastThree.add_row([
                        lt.getElement(onlyCasesInRange, 1)["datetime"],
                        lt.getElement(onlyCasesInRange, 1)["city"],
                        lt.getElement(onlyCasesInRange, 1)["state"],
                        lt.getElement(onlyCasesInRange, 1)["country"],
                        lt.getElement(onlyCasesInRange, 1)["shape"],
                        lt.getElement(onlyCasesInRange, 1)["duration (seconds)"]
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(onlyCasesInRange, 2)["datetime"],
                        lt.getElement(onlyCasesInRange, 2)["city"],
                        lt.getElement(onlyCasesInRange, 2)["state"],
                        lt.getElement(onlyCasesInRange, 2)["country"],
                        lt.getElement(onlyCasesInRange, 2)["shape"],
                        lt.getElement(onlyCasesInRange, 2)["duration (seconds)"]
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(onlyCasesInRange, 3)["datetime"],
                        lt.getElement(onlyCasesInRange, 3)["city"],
                        lt.getElement(onlyCasesInRange, 3)["state"],
                        lt.getElement(onlyCasesInRange, 3)["country"],
                        lt.getElement(onlyCasesInRange, 3)["shape"],
                        lt.getElement(onlyCasesInRange, 3)["duration (seconds)"]
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-2)["datetime"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-2)["city"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-2)["state"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-2)["country"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-2)["shape"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-2)["duration (seconds)"]
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-1)["datetime"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-1)["city"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-1)["state"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-1)["country"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-1)["shape"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-1)["duration (seconds)"]
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange))["datetime"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange))["city"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange))["state"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange))["country"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange))["shape"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange))["duration (seconds)"]
                    ])

    answer = f"\n================ Req No. 2 Inputs ================\n\nUFO Sightings between {beginSeconds} and {endSeconds} seconds.\n\n================ Req No. 2 answer ================\n\nThere are {lt.size(secondsKeys)} different UFO sightings durations.\n\nThe TOP 5 durations with UFO sightings are:\n\n{topFiveDurations}\n\nThere are {nCases} sightings between: {beginSeconds} and {endSeconds} duration.\n\nThe first 3 and last 3 UFO sightings in the duration time are:\n\n{firstAndLastThree}\n"

    #x = om.get(me.getValue(mp.get(analyzer, "casesBySeconds")), "90.0")

    return answer

#----------------------------------------

def getCasesBetweeenHours(analyzer, beginHour, endHour):

    """
    
        Responde al requerimiento 3.

    """

    # Se extrae el mapa de avistamientos
    cases = me.getValue(mp.get(analyzer, "cases"))

    # Se guarda en una lista todas las ciudades
    hoursKeys = lt.newList("ARRAY_LIST")
    
    # Se revisan las ciudades de cada avistamiento, si no se ha agregado la ciudad al mapa que indica
    # los avistamientos por ciudad, se grega la ciudad con una lista vacia como valor
    for i in lt.iterator(cases):
        if om.contains(me.getValue(mp.get(analyzer, "casesByHour")), str(dateToHour(i["datetime"]))) == False:
            om.put(me.getValue(mp.get(analyzer, "casesByHour")), str(dateToHour(i["datetime"])), lt.newList("ARRAY_LIST"))
            if lt.isPresent(hoursKeys, str(dateToHour(i["datetime"]))) == 0:
                lt.addLast(hoursKeys, str(dateToHour(i["datetime"])))

    hoursKeys = sortHours(hoursKeys)

    # Se añade cada caso de avistamiento a lista que corresponde a los casos de avistamientos de cada
    # ciudadas anteriormente
    for i in lt.iterator(cases):
        lt.addLast(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByHour")), str(dateToHour(i["datetime"])))), i)

    # Se eliminan los avistamientos duplicados en cada ciudad
    for i in lt.iterator(hoursKeys):
        pos = 2
        while pos <= lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByHour")), i))):
            lt.deleteElement(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByHour")), i)), pos)
            pos += 2
            pos -=1
        om.put(me.getValue(mp.get(analyzer, "casesByHour")), i, me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByHour")), i)))

    #a = me.getValue(mp.get(analyzer, "casesByHour"))

    hourKeysInRange = lt.newList("ARRAY_LIST")
    
    for i in lt.iterator(hoursKeys):
        if toHour(i) >= toHour(beginHour) and toHour(i) <= toHour(endHour):
            lt.addLast(hourKeysInRange, i)

    nCases = 0
    onlyCasesInRange = lt.newList("ARRAY_LIST")

    for i in lt.iterator(hourKeysInRange):
        nCases += lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByHour")), i)))
        for j in lt.iterator(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByHour")), i))):
            lt.addLast(onlyCasesInRange, j)

    onlyCasesInRange = sortDates(onlyCasesInRange)

    latestTimes = PrettyTable([   "Time",
                            "Count"
                        ])
                        
    latestTimes.add_row([
                        lt.getElement(hoursKeys, lt.size(hoursKeys)),
                        lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByHour")), lt.getElement(hoursKeys, lt.size(hoursKeys)))))
                    ])

    latestTimes.add_row([
                        lt.getElement(hoursKeys, lt.size(hoursKeys)-1),
                        lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByHour")), lt.getElement(hoursKeys, lt.size(hoursKeys)-1))))
                    ])

    latestTimes.add_row([
                        lt.getElement(hoursKeys, lt.size(hoursKeys)-2),
                        lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByHour")), lt.getElement(hoursKeys, lt.size(hoursKeys)-2))))
                    ])

    latestTimes.add_row([
                        lt.getElement(hoursKeys, lt.size(hoursKeys)-3),
                        lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByHour")), lt.getElement(hoursKeys, lt.size(hoursKeys)-3))))
                    ])

    latestTimes.add_row([
                        lt.getElement(hoursKeys, lt.size(hoursKeys)-4),
                        lt.size(me.getValue(om.get(me.getValue(mp.get(analyzer, "casesByHour")), lt.getElement(hoursKeys, lt.size(hoursKeys)-4))))
                    ])

    firstAndLastThree = PrettyTable([   "Datetime",
                                        "City",
                                        "State",
                                        "Country",
                                        "Shape",
                                        "Duration (seconds)"
                                    ])

    firstAndLastThree.add_row([
                        lt.getElement(onlyCasesInRange, 1)["datetime"],
                        lt.getElement(onlyCasesInRange, 1)["city"],
                        lt.getElement(onlyCasesInRange, 1)["state"],
                        lt.getElement(onlyCasesInRange, 1)["country"],
                        lt.getElement(onlyCasesInRange, 1)["shape"],
                        lt.getElement(onlyCasesInRange, 1)["duration (seconds)"]
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(onlyCasesInRange, 2)["datetime"],
                        lt.getElement(onlyCasesInRange, 2)["city"],
                        lt.getElement(onlyCasesInRange, 2)["state"],
                        lt.getElement(onlyCasesInRange, 2)["country"],
                        lt.getElement(onlyCasesInRange, 2)["shape"],
                        lt.getElement(onlyCasesInRange, 2)["duration (seconds)"]
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(onlyCasesInRange, 3)["datetime"],
                        lt.getElement(onlyCasesInRange, 3)["city"],
                        lt.getElement(onlyCasesInRange, 3)["state"],
                        lt.getElement(onlyCasesInRange, 3)["country"],
                        lt.getElement(onlyCasesInRange, 3)["shape"],
                        lt.getElement(onlyCasesInRange, 3)["duration (seconds)"]
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-2)["datetime"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-2)["city"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-2)["state"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-2)["country"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-2)["shape"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-2)["duration (seconds)"]
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-1)["datetime"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-1)["city"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-1)["state"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-1)["country"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-1)["shape"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange)-1)["duration (seconds)"]
                    ])

    firstAndLastThree.add_row([
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange))["datetime"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange))["city"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange))["state"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange))["country"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange))["shape"],
                        lt.getElement(onlyCasesInRange, lt.size(onlyCasesInRange))["duration (seconds)"]
                    ])

    answer = f"\n================ Req No. 3 Inputs ================\n\nUFO Sightings between {beginHour} and {endHour} seconds.\n\n================ Req No. 3 answer ================\n\nThere are {lt.size(hoursKeys)} different UFO sightings times [HH:MM:SS].\n\nThe 5 latest times for UFO sightings are:\n\n{latestTimes}\n\nThere are {nCases} sightings between: {beginHour} and {endHour}.\n\nThe first 3 and last 3 UFO sightings in this time are:\n\n{firstAndLastThree}\n"

    return answer





#•••••••••••••••••••••••••••••••••••••••••
# Funciones para agregar informacion al catalogo
#•••••••••••••••••••••••••••••••••••••••••

def addCase(analyzer, case):
    """
    """
    lt.addLast(me.getValue(mp.get(analyzer, "cases")), case)
    return analyzer






#•••••••••••••••••••••••••••••••••••••••••
# Funciones para creacion de datos
#•••••••••••••••••••••••••••••••••••••••••





#•••••••••••••••••••••••••••••••••••••••••
# Funciones adicionales
#•••••••••••••••••••••••••••••••••••••••••

def getCasesSize(analyzer):
    return lt.size(me.getValue(mp.get(analyzer, "cases")))

def toDate(date:str):
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%f')

def firstAndLastFiveCases(analyzer):

    list = me.getValue(mp.get(analyzer, "cases"))

    elemnt1 = lt.getElement(list, 1)
    elemnt2 = lt.getElement(list, 2)
    elemnt3 = lt.getElement(list, 3)
    elemnt4 = lt.getElement(list, 4)
    elemnt5 = lt.getElement(list, 5)

    nPosition = lt.size(list)

    elemntn_4 = lt.getElement(list, nPosition-4)
    elemntn_3 = lt.getElement(list, nPosition-3)
    elemntn_2 = lt.getElement(list, nPosition-2)
    elemntn_1 = lt.getElement(list, nPosition-1)
    elemntn = lt.getElement(list, nPosition)



    table = PrettyTable([   "Datetime",
                            "City",
                            "State",
                            "Country",
                            "Shape",
                            "Duration (Seconds)"
                        ])
                        
    table.add_row([
                    elemnt1["datetime"],
                    elemnt1["city"],
                    elemnt1["state"],
                    elemnt1["country"],
                    elemnt1["shape"],
                    elemnt1["duration (seconds)"]
                    ])

    table.add_row([
                    elemnt2["datetime"],
                    elemnt2["city"],
                    elemnt2["state"],
                    elemnt2["country"],
                    elemnt2["shape"],
                    elemnt2["duration (seconds)"]
                    ])

    table.add_row([
                    elemnt3["datetime"],
                    elemnt3["city"],
                    elemnt3["state"],
                    elemnt3["country"],
                    elemnt3["shape"],
                    elemnt3["duration (seconds)"]
                    ])

    table.add_row([
                    elemnt4["datetime"],
                    elemnt4["city"],
                    elemnt4["state"],
                    elemnt4["country"],
                    elemnt4["shape"],
                    elemnt4["duration (seconds)"]
                    ])

    table.add_row([
                    elemnt5["datetime"],
                    elemnt5["city"],
                    elemnt5["state"],
                    elemnt5["country"],
                    elemnt5["shape"],
                    elemnt5["duration (seconds)"]
                    ])

    table.add_row([
                    elemntn_4["datetime"],
                    elemntn_4["city"],
                    elemntn_4["state"],
                    elemntn_4["country"],
                    elemntn_4["shape"],
                    elemntn_4["duration (seconds)"]
                    ])

    table.add_row([
                    elemntn_3["datetime"],
                    elemntn_3["city"],
                    elemntn_3["state"],
                    elemntn_3["country"],
                    elemntn_3["shape"],
                    elemntn_3["duration (seconds)"]
                    ])

    table.add_row([
                    elemntn_2["datetime"],
                    elemntn_2["city"],
                    elemntn_2["state"],
                    elemntn_2["country"],
                    elemntn_2["shape"],
                    elemntn_2["duration (seconds)"]
                    ])

    table.add_row([
                    elemntn_1["datetime"],
                    elemntn_1["city"],
                    elemntn_1["state"],
                    elemntn_1["country"],
                    elemntn_1["shape"],
                    elemntn_1["duration (seconds)"]
                    ])

    table.add_row([
                    elemntn["datetime"],
                    elemntn["city"],
                    elemntn["state"],
                    elemntn["country"],
                    elemntn["shape"],
                    elemntn["duration (seconds)"]
                    ])

    return table

def dateToHour(date):
    return datetime.strptime(date[11:len(date)+1], "%H:%M:%f").time()

def toHour(hour):
    return datetime.strptime(hour, "%H:%M:%f").time()

#•••••••••••••••••••••••••••••••••••••••••
# Funciones de comparacion
#•••••••••••••••••••••••••••••••••••••••••

def compareDates(case1, case2):
    return(toDate(case1["datetime"]) < toDate(case2["datetime"]))

def compareNumbers(case1, case2):
    return(case1["nCases"] > case2["nCases"])

def compareSeconds(time1, time2):
    return(float(time1) < float(time2))

def compareHours(time1, time2):
    return (datetime.strptime(time1, "%H:%M:%f").time() < datetime.strptime(time2, "%H:%M:%f").time())

#----------------------------------------





#•••••••••••••••••••••••••••••••••••••••••
# Funciones de ordenamiento
#•••••••••••••••••••••••••••••••••••••••••

def sortByDate(analyzer):

    list = me.getValue(mp.get(analyzer, "cases"))
    list = sa.sort(list, compareDates)

    return list

def sortByNCases(data):
    return sa.sort(data, compareNumbers)

def sortSeconds(data):
    data = sa.sort(data, compareSeconds)
    return data

def sortDates(data):
    return sa.sort(data, compareDates)

def sortHours(data):
    return sa.sort(data, compareHours)
