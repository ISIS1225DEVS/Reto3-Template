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
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import listiterator as it
assert cf
default_limit = 1000
sys.setrecursionlimit(default_limit*1000)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(" Bienvenido")
    print(" 1 - Iniciar el catalogo. ")
    print(" 2 - Cargar información en el catálogo")
    print(' 3 - Req.1 --> Reproducciones basadas en una caracteristica dentro de un rango especifico.')
    print(' 4 - Req.2 --> Pistas recomendadas para usar en una fiesta.')
    print(' 5 - Req.3 --> Pistas recomendadas para usar mientras se estudia.')
    print(' 6 - Req.4 --> Estudiar los generos muiscales segun su Tempo.')
    print(' 7 - Req.5 --> Conocer el genero musical mas escuchado en un rango de tiempo.')
    print(" 0 - Salir.")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


database = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        database = controller.init()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        database = controller.loadevent(database)

    # Requerimiento 1.
    elif int(inputs[0]) == 3:
        print("\n")
        print('Caracteristicas Disponibles: ')
        print("\n")
        print(" --> Instrumentalness")
        print(" --> Acousticness")
        print(" --> Liveness")
        print(" --> Speechiness")
        print(" --> Energy")
        print(" --> Danceability")
        print(" --> Valence")
        print("\n")
        characteristic = input(' ---> Caracteristica del contenido: ')
        minvalue = input(' ---> Valor minimo de la caracteristica del contenido: ')
        maxvalue = input(' ---> Valor maximo de la caracteristica del contenido : ')
        sol = controller.Requerimiento1(database, characteristic.lower().strip(), minvalue, maxvalue)
        print("\n")
        print('++++++ Req No. 1 results... ++++++')
        #print(' >>> Altura del arbol: ' + str(controller.indexHeight(database)))
        #print(' >>> Elementos en el arbol: ' + str(controller.indexSize(database)))
        print(characteristic, 'is between ', minvalue, 'and' , maxvalue, 'is:')
        print('Total of reproductions: ', sol[0])
        print('Total of unique artists: ', sol[1])
        
    
    # Requerimiento 2.
    elif int(inputs[0]) == 4:
        print("\n")
        minvalue_energy = input('  --> Valor mínimo de la característica Energy: ')
        maxvalue_energy = input('  --> Valor máximo de la característica Energy: ')
        minvalue_dance = input('  --> Valor mínimo de la característica Danceability: ')
        maxvalue_dance = input('  --> Valor máximo de la característica Danceability: ')
        pass

    # Requerimiento 3.
    elif int(inputs[0]) == 5:
        print("\n")
        minvalue_instru = input('  --> El valor mínimo del rango para Instrumentalness: ')
        maxvalue_instru = input('  --> El valor máximo del rango para Instrumentalness: ')
        minvalue_tempo = input('  --> El valor mínimo del rango para el Tempo: ')
        maxvalue_tempo = input('  --> El valor máximo del rango para el Tempo: ')
        sol = controller.Requerimiento3(database, minvalue_instru, maxvalue_instru, minvalue_tempo, maxvalue_tempo)
        print("\n")
        print('++++++ Req No. 3 results... ++++++')
        print('Instrumentalness is between', minvalue_instru, 'and', maxvalue_instru)
        print('Tempo is between', minvalue_tempo, 'and', maxvalue_tempo)
        print('--> Total of unique tracks in events: ',sol[0])
        iterator = it.newIterator(sol[1])
        number= 1
        while (it.hasNext(iterator)) and number<6:
            event = it.next(iterator)
            print('Track',number,': ',event['track_id'], 'with instrumentalness of',
                event['instrumentalness'],'and tempo of', event['tempo'])
            number+=1

    # Requerimiento 4.
    elif int(inputs[0]) == 6:
        print("\n")
        print('Generos disponibles: ')
        print('Reggae, Down-tempo, Chill-out, Hip-hop, Jazz-and-Funk, Pop, R&B, Rock, Metal')
        print("\n")
        listg = input('Ingrese la lista de generos a buscar separados por coma: ')
        condition  = input("(Si / No ) Desea agregar un nuevo Genero a la busqueda: ")
        if (condition.lower().strip() == 'si'):
            nameg = input('  --> Nombre para el nuevo genero musical: ')
            minT = input('  --> El valor mínimo del rango para el Tempo(60-160): ')
            maxT = input('  --> El valor máximo del rango para el Tempo(60-160): ')
        else:
            nameg = 'None'
            minT = 0
            maxT = 0
            
        listg = listg.replace(',','').lower()
        listg = listg.split()
        sol = controller.Requerimiento4(database, listg, nameg.lower().strip(), minT, maxT)
        print("\n")
        print('++++++ Req No. 4 results... ++++++')
        print('Total of reproductions: ', sol[0])
        for event in lt.iterator(sol[1]):
            genre = event['genre'].upper()
            range = event['range']
            lstartist = mp.keySet(event['Uartist'])
            print("                                             ")
            print('========' ,genre, '========')
            print('for',genre, 'the tempo is between',range[0],'and',range[1],'BPM')
            print(genre,'reproductions:',event['rep'],'with',lt.size(lstartist),'different artists')
            print('----- Some artists for',genre, '-----')
            iterator = it.newIterator(lstartist)
            number= 1
            while (it.hasNext(iterator)) and number<11:
                event = it.next(iterator)
                print('Artist',number,':',event)
                number+=1
            




        
    
    # Requerimiento 5.
    elif int(inputs[0]) == 7:
        print("\n")
        minvalue_hour = input(' --> valor mínimo de la hora del día: ')
        maxvalue_hour = input(' --> valor máximo de la hora del día: ')
        pass

    else:
        sys.exit(0)
sys.exit(0)


