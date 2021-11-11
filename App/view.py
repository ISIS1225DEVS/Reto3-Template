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

from datetime import datetime
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
    print("2- Contar los avistamientos en una ciudad")
    print("3- Contar los avistamientos por duración")
    print("4- Contar avistamientos por Hora/Minutos del día") 
    print("5- Contar los avistamientos en un rango de fechas") 
    print("6- Contar los avistamientos de una Zona Geográfica")
    print("7- Visualizar los avistamientos de una zona geográfica") 

def cargarDatosCat(): 
    catalog=controller.cargarDatos() 
    return catalog
def casosPorCiudad(catalog,ciudad):
    listR=controller.casosPorCiudad(catalog,ciudad)
    return listR    

def sight_by_duration(catalog,duraMin,duraMax):
    return controller.sight_by_durationc(catalog,duraMin,duraMax)


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=cargarDatosCat()
        tamaño=lt.size(catalog["casos"])
        print("El total de avistamientos cargados es: " +str(tamaño))
        print("Los 5 primeros avistamientos son: ")

        casos=(list(lt.iterator(catalog["casos"])))
        for i in range(0,5): 
            print ("Fecha:"+ casos[i]["datetime"]+ "|Ciudad: "+ casos[i]["city"]+ "|Shape: "+ casos[i]["shape"]+ "|Duracion: "+ casos[i]["duration (seconds)"]+ "|Comentario: "+ casos[i]["comments"])

    elif int(inputs[0]) == 2:
          ciudad=input("Ingrese el nombre de la ciudad que desea consultar:")
          listaCiudad=casosPorCiudad(catalog,ciudad)
          print("El total de avistamientos en la ciudad de "+ ciudad+" son: "+str(len(listaCiudad)))
          print("Los 3 primeros avistamientos son: ")
          for i in range(0,3): 
            print ("Fecha:"+ listaCiudad[i]["datetime"]+ "|Ciudad: "+ listaCiudad[i]["city"]+"|Pais: "+ listaCiudad[i]["country"]+"|Duracion: " + listaCiudad[i]["duration (seconds)"] + "|Forma: "+ listaCiudad[i]["shape"])
          
          print("Los 3 ultimos avistamientos son: ")
          for i in range(len(listaCiudad)-3,len(listaCiudad)):  
             print ("Fecha:"+ listaCiudad[i]["datetime"]+ "|Ciudad: "+ listaCiudad[i]["city"]+"|Pais: "+ listaCiudad[i]["country"]+"|Duracion: " + listaCiudad[i]["duration (seconds)"] + "|Forma: "+ listaCiudad[i]["shape"])
 
    elif int(inputs[0]) == 3:

        horaMin = input("Ingrese el tiempo minimo (en formato HH:MM:SS) para la busqueda en formato:\n ")
        horaMax = input("Ingrese el tiempo maximo (en formato HH:MM:SS) para la busqueda en formato:\n ")

        sights = sight_by_duration(catalog,horaMin,horaMax)
        
        print("\nLa mayor duracion registrada es de "+str(sights[0])+" segundos con "+str(sights[1])+" avistamiento(s)")
        print("\nLos avistamientos totales ocurridos entre " + horaMin + " y " + horaMax + " son " + str(lt.size(sights[2])))
        if lt.size(sights[2])>=6:
            
            print("\nLos tres avistamientos más recientes y los tres avistamientos más antiguos registrados en este intervalo de tiempo son: ")

            x = lt.size(sights[2]) - 2
            y = True
            z = 1

            while y:
                if z != 4:
                    AS = lt.getElement(sights[2], z)
                    z += 1
                else: 
                    AS = lt.getElement(sights[2], x)
                    x += 1
                    if x == lt.size(sights[2])+1:
                        y = False
                print ("Fecha:"+ AS["datetime"]+ "|Ciudad: "+ AS["city"]+ "|Forma: "+ AS["shape"]+ "|Duracion: "+ AS["duration (seconds)"]+ "|Comentario: "+ AS["comments"])
                
        pass
    
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass               
    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        
        pass

    else:
        sys.exit(0)
sys.exit(0)
