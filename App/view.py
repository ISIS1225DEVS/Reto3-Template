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
    print("2- Caracterizar las reproducciones")
    print("3- Encontrar música para festejar")

def initAnalyzer():

    return controller.initAnalyzer()

def loadData(analyzer):
    return controller.loadData(analyzer)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        analyzer = initAnalyzer()

    elif int(inputs[0]) == 2:
        carac = input('Diga la característica que busca: ')
        val_min= float(input('Diga el valor mínimo que debe tener la característica: '))
        val_max= float(input('Diga el valor máximo que debe tener la característica: '))

        rta = controller.requerimiento1(analyzer, carac, val_min, val_max)

        print(carac, " está entre ", val_min, " y ", val_max)
        print("Total de reproducciones: ", rta[1], " Total de artistas únicos: ", rta[0])

    elif int(inputs[0]) == 3:
        min_e = float(input("Diga el valor mínimo de energy."))
        max_e = float(input("Diga el valor máximo de energy."))
        min_d = float(input("Diga el valor mínimo de danceability."))
        max_d = float(input("Diga el valor máximo de danceability."))

        rta = controller.requerimiento2(analyzer, min_e,max_e, min_d, max_d)
        total_tracks = rta[1]
        tracks = rta[0]
        track1 = tracks[0][0]
        track2 = tracks[1][0]
        track3 = tracks[2][0]
        track4 = tracks[3][0]
        track5 = tracks[4][0]

        energy1 = tracks[0][1]
        energy2 = tracks[1][1]
        energy3 = tracks[2][1]
        energy4 = tracks[3][1]
        energy5 = tracks[4][1]

        

        print("Energy está entre ", min_e, " y ", max_e)
        print("Danceability está entre ", min_d, " y ", max_d)
        print("Total unique tracks in events: ", total_tracks)
        print("-------------------- Unique track id --------------------")
        print("Track 1: ", track1, " con energy: ", energy1[0] ," y danceability: ", energy1[1] )
        print("Track 2: ", track2, " con energy: ", energy2[0] ," y danceability: ", energy2[1] )
        print("Track 3: ", track3, " con energy: ", energy3[0] ," y danceability: ", energy3[1] )
        print("Track 4: ", track4, " con energy: ", energy4[0] ," y danceability: ", energy4[1] )
        print("Track 5: ", track5, " con energy: ", energy5[0] ," y danceability: ", energy5[1] )
      


    else:
        sys.exit(0)
sys.exit(0)
