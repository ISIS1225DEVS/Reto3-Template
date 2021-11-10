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
def casosPorHoras(catalog,rangoInferior,rangoSuperior):
    listR=controller.casosPorHoras(catalog,rangoInferior,rangoSuperior)
    return listR
def casosPorFechas(catalog,rangoInferior,rangoSuperior):
    listR=controller.casosPorFechas(catalog,rangoInferior,rangoSuperior)  
    return listR
def casosPorArea(catalog,longitudMin,longitudMax,latitudMin,latitudMax):
    listR=controller.casosPorArea(catalog,longitudMin,longitudMax,latitudMin,latitudMax)
    return listR    

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
        print("")
        print("")
        print("Los 5 primeros avistamientos cargados son: ")
        print("")
        casos=(list(lt.iterator(catalog["casos"])))
        for i in range(0,5): 
            print ("Fecha:"+ casos[i]["datetime"]+ "|Ciudad: "+ casos[i]["city"]+ "|Shape: "+ casos[i]["shape"]+ "|Duracion: "+ casos[i]["duration (seconds)"]+ "|Comentario: "+ casos[i]["comments"])
            print("")
        print("")    
        print("Los 5 ultimos avistamientos cargados son: ")
        print("")
        for i in range(len(casos)-5,len(casos)): 
            print ("Fecha:"+ casos[i]["datetime"]+ "|Ciudad: "+ casos[i]["city"]+ "|Shape: "+ casos[i]["shape"]+ "|Duracion: "+ casos[i]["duration (seconds)"]+ "|Comentario: "+ casos[i]["comments"])
            print("")
        

    elif int(inputs[0]) == 2:
          ciudad=input("Ingrese el nombre de la ciudad que desea consultar:")
          casosCiudad=casosPorCiudad(catalog,ciudad)
          print("El total de avistamientos en la ciudad de "+ ciudad+" son: "+str(lt.size(casosCiudad)))
          print("")
          print("Los 3 primeros avistamientos son: ")
          print("")
          listaCiudad=(list(lt.iterator(casosCiudad)))
          for i in range(0,3): 
            print ("Fecha:"+ listaCiudad[i]["datetime"]+ "|Ciudad: "+ listaCiudad[i]["city"]+"|Pais: "+ listaCiudad[i]["country"]+"|Duracion: " + listaCiudad[i]["duration (seconds)"] + "|Forma: "+ listaCiudad[i]["shape"])
            print("")
          print("")  
          print("Los 3 ultimos avistamientos son: ")
          print("")
          for i in range(lt.size(casosCiudad)-3,lt.size(casosCiudad)):  
             print ("Fecha:"+ listaCiudad[i]["datetime"]+ "|Ciudad: "+ listaCiudad[i]["city"]+"|Pais: "+ listaCiudad[i]["country"]+"|Duracion: " + listaCiudad[i]["duration (seconds)"] + "|Forma: "+ listaCiudad[i]["shape"])
             print("")

         
    elif int(inputs[0]) == 3:
         pass

    elif int(inputs[0]) == 4:
         rangoInferior=input("Ingrese la hora correspondiente al rango inferior que desea consultar, en formato HH:MM:SS   : ")
         rangoSuperior=input("Ingrese la hora correspondiente al rango superior que desea consultar, en formato HH:MM:SS   : ")
         listaHoras=casosPorHoras(catalog,rangoInferior,rangoSuperior)
         print("Entre las "+rangoInferior+" y las " +rangoSuperior+" se reportaron " +str(lt.size(listaHoras))+" avistamientos.")
         print("")
         print("Los 3 primeros avistamientos son: ")
         print("")
         horasMostrar=(list(lt.iterator(listaHoras)))
         for i in range(0,3): 
            print ("Fecha:"+ horasMostrar[i]["datetime"]+ "|Ciudad: "+ horasMostrar[i]["city"]+"|Pais: "+ horasMostrar[i]["country"]+"|Duracion: " + horasMostrar[i]["duration (seconds)"] + "|Forma: "+ horasMostrar[i]["shape"])
            print("")
         print("")  
         print("Los 3 ultimos avistamientos son: ")
         print("")
         for i in range(lt.size(listaHoras)-3,lt.size(listaHoras)):  
             print ("Fecha:"+ horasMostrar[i]["datetime"]+ "|Ciudad: "+ horasMostrar[i]["city"]+"|Pais: "+ horasMostrar[i]["country"]+"|Duracion: " + horasMostrar[i]["duration (seconds)"] + "|Forma: "+ horasMostrar[i]["shape"])
             print("")


    elif int(inputs[0]) == 5:
         rangoInferior=input("Ingrese la fecha correspondiente al rango inferior que desea consultar, en formato AAAA-MM-DD  : ")
         rangoSuperior=input("Ingrese la fecha correspondiente al rango superior que desea consultar, en formato AAAA-MM-DD  : ")   
         listaFechas=casosPorFechas(catalog,rangoInferior,rangoSuperior)     
         print("Entre la fecha "+rangoInferior+" y la fecha " +rangoSuperior+" se reportaron " +str(lt.size(listaFechas))+" avistamientos.")
         print("")
         print("Los 3 primeros avistamientos son: ")
         print("")
         fechasMostrar=(list(lt.iterator(listaFechas)))
         for i in range(0,3): 
            print ("Fecha:"+ fechasMostrar[i]["datetime"]+ "|Ciudad: "+ fechasMostrar[i]["city"]+"|Pais: "+ fechasMostrar[i]["country"]+"|Duracion: " + fechasMostrar[i]["duration (seconds)"] + "|Forma: "+ fechasMostrar[i]["shape"])
            print("")
         print("")  
         print("Los 3 ultimos avistamientos son: ")
         print("")
         for i in range(lt.size(listaFechas)-3,lt.size(listaFechas)):  
            print ("Fecha:"+ fechasMostrar[i]["datetime"]+ "|Ciudad: "+ fechasMostrar[i]["city"]+"|Pais: "+ fechasMostrar[i]["country"]+"|Duracion: " + fechasMostrar[i]["duration (seconds)"] + "|Forma: "+ fechasMostrar[i]["shape"])
            print("")      

    elif int(inputs[0]) == 6:
         longitudMin=input("Ingrese la coordenada que corresponda a la longitud minima a consultar :")
         longitudMax=input("Ingrese la coordenada que corresponda a la longitud maxima a consultar :")
         latitudMin=input("Ingrese la coordenada que corresponda a la latitud minima a consultar :")
         latitudMax=input("Ingrese la coordenada que corresponda a la latitud maxima a consultar :")
         listaCasos=casosPorArea(catalog,longitudMin,longitudMax,latitudMin,latitudMax)
         print("")
         print("Hay un total de " +str(lt.size(listaCasos))+ " avistamientos en el area especificada.")
         print("")
         print("Los 5 primeros avistamientos son: ")
         print("")
         casosMostrar=(list(lt.iterator(listaCasos)))
         if lt.size(listaCasos) >= 5:
            for i in range(0,5): 
                print ("Fecha:"+ casosMostrar[i]["datetime"]+ "|Ciudad: "+ casosMostrar[i]["city"]+"|Pais: "+ casosMostrar[i]["country"]+"|Duracion: " + casosMostrar[i]["duration (seconds)"] + "|Forma: "+ casosMostrar[i]["shape"]+ "|Longitud: "+ casosMostrar[i]["longitude"]+ "|Latitud: "+ casosMostrar[i]["latitude"])
                print("")
            print("")  
            print("Los 5 ultimos avistamientos son: ")
            print("")
            for i in range(lt.size(listaCasos)-5,lt.size(listaCasos)):  
                print ("Fecha:"+ casosMostrar[i]["datetime"]+ "|Ciudad: "+ casosMostrar[i]["city"]+"|Pais: "+ casosMostrar[i]["country"]+"|Duracion: " + casosMostrar[i]["duration (seconds)"] + "|Forma: "+ casosMostrar[i]["shape"]+ "|Longitud: "+ casosMostrar[i]["longitude"]+ "|Latitud: "+ casosMostrar[i]["latitude"])
                print("")      
         else: 
               for i in range(0,lt.size(listaCasos)): 
                   print ("Fecha:"+ casosMostrar[i]["datetime"]+ "|Ciudad: "+ casosMostrar[i]["city"]+"|Pais: "+ casosMostrar[i]["country"]+"|Duracion: " + casosMostrar[i]["duration (seconds)"] + "|Forma: "+ casosMostrar[i]["shape"]+ "|Longitud: "+ casosMostrar[i]["longitude"]+ "|Latitud: "+ casosMostrar[i]["latitude"])
                   print("")

    elif int(inputs[0]) == 7:
        
        pass

    else:
        sys.exit(0)
sys.exit(0)
