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
#-----------------------------------
#Funciones varias
#-----------------------------------
def detCaracteristica(numero):
    if(numero == 1):
        return 'instrumentalness'
    elif(numero == 2):
        return 'acousticness'
    elif(numero == 3):
        return 'liveness'
    elif(numero == 4):
        return 'speechiness'
    elif(numero == 5):
        return 'energy'
    elif(numero == 6):
        return 'danceability'
    else:
        return 'valence'
#-----------------------------------
#Ruta a los archivos
#-----------------------------------
#context_content_features-small.csv
songFile = 'context_content_features-small.csv'
cont = None
#-----------------------------------
#Menu
#-----------------------------------
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\nBienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Requerimiento 1")
    print("3- Informacion del arbol")
    print("4- Música para festejar")
    print("5- Música para estudiar")
    print("6- Canciones y artistas por géneros")
    print("7- Género más escuchado en un tiempo")
    print("Presione cualquier otra tecla para salir")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print('antes')
        cont = controller.init()
        print('despues')
        controller.loadData(cont, songFile)
        print("Cargando información de los archivos ....")

    elif int(inputs[0]) == 2:
        numero = int(input("Escoja entre alguna de las caracteristicas de contenido: \nInstrumentalness: '1'\nAcousticness: '2'\nLiveness: '3'\nSpeechiness: '4'\nEnergy: '5'\nDanceability: '6'\nValence: '7'"))
        Caract = detCaracteristica(numero)
        initialInstru = float(input("limite inferior: "))
        finalInstru = float(input("limite superior: "))
        retorno = controller.Requerimiento1(cont, initialInstru, finalInstru, Caract)
        print('numero de artistas: ', retorno[0], '   \nnumero de visualizaciones: ', retorno[1], '\nPistas unicas: ', retorno[2])
    elif int(inputs[0]) == 3:
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))  
    elif int (inputs[0]) == 4:
        menorEnergy = float(input("Ingrese el rango minimo de Energy: "))
        mayorEnergy = float(input("Ingrese el rango maximo de Energy: "))
        menorDanceability = float(input("Ingrese el rango minimo de Danceability: "))
        mayorDanceability = float(input("Ingrese el rango maximo de Danceability: "))
        print(controller.Requerimiento2(cont, menorEnergy, mayorEnergy, menorDanceability, mayorDanceability))
    else:
        sys.exit(0)
sys.exit(0)
