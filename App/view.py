"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """



import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config
from DISClib.Algorithms.Graphs import scc
from DISClib.ADT.graph import gr
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import list as lt
from DISClib.ADT import map as m
from DISClib.Algorithms.Graphs import dfs
from DISClib.DataStructures import edge as e

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


initialStation = None
recursionLimit = 20000
servicefile = '201801-1-citibike-tripdata.csv'
#servicefile2 = '201801-2-citibike-tripdata.csv'
#servicefile3 = '201801-3-citibike-tripdata.csv'
#servicefile4 = '201801-4-citibike-tripdata.csv'

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("****************************************************")
    print("RETO No. 4 CitiBike")
    print("[ 1 ] Inicializar Analizador")
    print("[ 2 ] Cargar información de citibyke en newyork")
    print("[ 3 ] Req 1. Cantidad de clusters de viajes")
    print("[ 4 ] Req 2. Ruta turistica circular")
    print("[ 5 ] Req 3. Estaciones criticas ")
    print("[ 6 ] Req 4. Ruta turistisca por resistencia")
    print("[ 7 ] Req 5. Recomendador de Rutas")
    print("[ 8 ] Req 6. Ruta de interes turistico")
    print("[ 9 ] Req 7. Identificacion de estaciones para publicidad")
    print("[10 ] Req 8. Identificacion de bicicletas para mantenimiento")
    print("[ 0 ] Salir")
    print("****************************************************")


def optionTwo():
    print("\nCargando información ....")
    controller.loadServices(cont,servicefile,aux)



    #Aqui puedo imprimir todos los vertices
    print (gr.vertices(cont['connections']))
    numedges = controller.totalConnections(cont)
    numvertex = controller.totalStops(cont)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))
    sys.setrecursionlimit(recursionLimit)
    print('El limite de recursion se ajusta a: ' + str(recursionLimit))
    # Aqui puedo imprimir el numero de arcos
    #print (gr.numEdges(cont['connections']))
    #input ("Clic para como quedo cargado el Grafo .... continuar ......")
    # Aqui puedo imprimir el grafo con su informacion


    
    


def optionThree():
    sccA=controller.connectedComponents(cont)
    #print('El número de componentes conectados es: ' + str(controller.connectedComponents(cont)))
    print('El número de componentes conectados es: ' + str(sccA))
    input ("El argorimo de Kosaraju esta funcionando, esto es el scc.py")
    
    id1=input("Inserte Station ID_1: " )
    id2=input("Inserte Station ID_2: ")
    #TESTED WITH 
    #72 y 127, True
    #72 y 270
    scc2=(controller.connectedwithID(cont,id1,id2))
    print ("Estan ", id1, " y " , id2 , "fuertemente conectados: " , scc2) 
    input ("clic para continuar")



def optionFour():
    tiempoDisponible=int(input(" Cuanto minutos tienes disponible para la visita? " ))
    initialStation=input("Inserte el punto de partida Station ID, Ejemplo 72, 79, 82, 83, 119, 120: " )
    #controller.minimumCostPaths(cont, initialStation)
    scc3=controller.connectedwithID_1(cont,initialStation)
    contador=0
    listaReverse= lt.newList()
    listaReverse=scc3['reversePost']
    print (listaReverse)
    input ("&&&&&&&&&&&&&&&&&& Clic para correr DFS   sobre modos del Stack Reverse    &&&&&&&&&&&&&&&&&&")
    dfsAns=dfs.DepthFirstSearch(cont['connections'], initialStation)
    
    #print (dfsAns)

    j=0
    listaDSF= lt.newList()
    """
    for i in element:
        if element['value']['marked']==True:
            listaDSF[j]=element['value']['edgeTo']
            j=j+1
    for i in listaDSF:
        print (listaDSF[i])
    """
   
    print ("********************************** Voy a imprimir el Path uno ****************************************")
    print ("")
    #tam=lt.size(listaReverse)
    tam=len(listaReverse)
    verX=listaReverse[tam-6]
    verY=listaReverse[0]
    #print ("tamano del stack:" , tam, " verx a buscar: ", verX)
    dfsAnsPathVerX=dfs.pathTo(dfsAns, verX)
    print (dfsAnsPathVerX)    
    print (" ")
    print ("Acabo de imprimir el path desde ", verX, " a ",  initialStation)
    print (" ")
    print ("********************************** Voy a imprimir el Path dos ****************************************")
    print (" ")
    dfsAnsPathVerY=dfs.pathTo(dfsAns, verY)
    print (dfsAnsPathVerY)    
    print (" ")
    print ("Acabo de imprimir el path desde ", verY, " a ",  initialStation)
   
    input ("Clic para encontrar las rutas circuales")
    stackTam=stack.size(dfsAnsPathVerX)
    #print ("Tamano dle stack: ", stackTam)
    #input("clic para cotinuar")
    ruta1=lt.newList()
 
    for i in range (0,stackTam):
        punto=stack.pop(dfsAnsPathVerX)
       # print (punto)
        ruta1[i]=punto
    
    tiempoRuta1=0   
    #print ("Punto 1: ", ruta1[0], " y Punto 2: ", ruta1[1])
    #print (stackTam)
    print("")
    print ("Ruta lineal")
    print("")
    for i in range (0,stackTam-1):
        nodo = gr.getEdge(cont['connections'], ruta1[i], ruta1[i+1])
        tiempoRuta1= tiempoRuta1+ nodo['weight'] +10
        print ("Sale de: ", ruta1[i], " a ", ruta1[i+1], " tiempo de recorrido incluye visita: ", round(tiempoRuta1,0))

    print("")
    print ("Ruta Circular")
    print("")
    tiempoRuta1=0
    pos=0
    peso=0
    i=0
    j=0
    for i in range (0,stackTam-1):
        if  (tiempoRuta1<=(tiempoDisponible/3)):
            nodo = gr.getEdge(cont['connections'], ruta1[i], ruta1[i+1])
            tiempoRuta1= tiempoRuta1+ nodo['weight'] +10
            peso=nodo['weight']
            print ("Sale de: ", ruta1[i], " a ", ruta1[i+1], " tiempo de recorrido incluye visita: ", round(tiempoRuta1,0))
            pos=i
            #print ("i: ",i, " pos: ", pos)
        else:    
            i=stackTam-1

    #print ("Posicion: ", pos)
    #nodo = gr.getEdge(cont['connections'], ruta1[pos+1], ruta1[pos])
    tiempoRuta1= tiempoRuta1+ peso +10
    print ("Sale de: ", ruta1[pos+1], " a ", ruta1[pos], " tiempo de recorrido incluye visita: ", tiempoRuta1)
    for k in range (pos,1,-1):
            nodo = gr.getEdge(cont['connections'], ruta1[k], ruta1[k-1])
            peso=nodo['weight']
            tiempoRuta1= tiempoRuta1+ peso +10
            print ("Sale de: ", ruta1[k], " a ", ruta1[k-1], " tiempo de recorrido incluye visita: ", round(tiempoRuta1,0))
  
    nodo = gr.getEdge(cont['connections'], ruta1[1], ruta1[0])
    peso=nodo['weight']
    tiempoRuta1= tiempoRuta1+ peso +10
    print ("Sale de: ", ruta1[1], " a ", ruta1[0], " tiempo de recorrido incluye visita: ", round(tiempoRuta1,0))


    """ 
    #De aqui en adelante Ruta 2
    stackTamY=stack.size(dfsAnsPathVery)
    ruta2=lt.newList()

    for i in range (0,stackTam):
        punto=stack.pop(dfsAnsPathVerY)
        # print (punto)
        ruta2[i]=punto

    tiempoRuta2=0   
    #print ("Punto 1: ", ruta1[0], " y Punto 2: ", ruta1[1])
    #print (stackTam)
    print("")
    print ("Ruta lineal")
    print("")
    for i in range (0,stackTamY-1):
        nodo = gr.getEdge(cont['connections'], ruta2[i], ruta2[i+1])
        tiempoRuta2= tiempoRuta2+ nodo['weight'] +10
        print ("Sale de: ", ruta2[i], " a ", ruta2[i+1], " tiempo de recorrido incluye visita: ", round(tiempoRuta2,0))
    print("")
    print ("Ruta Circular")
    print("")
    tiempoRuta2=0
    pos=0
    peso=0
    i=0
    j=0
    for i in range (0,stackTamY-1):
        if  (tiempoRuta2<=(tiempoDisponible/3)):
            nodo = gr.getEdge(cont['connections'], ruta2[i], ruta2[i+1])
            tiempoRuta2= tiempoRuta2+ nodo['weight'] +10
            peso=nodo['weight']
            print ("Sale de: ", ruta2[i], " a ", ruta2[i+1], " tiempo de recorrido incluye visita: ", round(tiempoRuta2,0))
            pos=i
            #print ("i: ",i, " pos: ", pos)
        else:    
            i=stackTamY-1

    #print ("Posicion: ", pos)
    #nodo = gr.getEdge(cont['connections'], ruta1[pos+1], ruta1[pos])
    tiempoRuta2= tiempoRuta2+ peso +10
    print ("Sale de: ", ruta2[pos+1], " a ", ruta2[pos], " tiempo de recorrido incluye visita: ", tiempoRuta2)
    for k in range (pos,1,-1):
            nodo = gr.getEdge(cont['connections'], ruta2[k], ruta2[k-1])
            peso=nodo['weight']
            tiempoRuta2= tiempoRuta2+ peso +10
            print ("Sale de: ", ruta2[k], " a ", ruta2[k-1], " tiempo de recorrido incluye visita: ", round(tiempoRuta2,0))

    nodo = gr.getEdge(cont['connections'], ruta2[1], ruta2[0])
    peso=nodo['weight']
    tiempoRuta2= tiempoRuta2+ peso +10
    print ("Sale de: ", ruta2[1], " a ", ruta2[0], " tiempo de recorrido incluye visita: ", round(tiempoRuta2,0))

    """

def optionFive():

    id_mayores_salida=[0,0,0]
    mayores_salida=[0,0,0]

    id_mayores_llegada=[0,0,0]
    mayores_llegada=[0,0,0]

    id_menores=[0,0,0]
    menores=[1000000000000000,10000000000000000,1000000000000000]

# Loop para determinar top salida

    for x in aux:
        if aux[x][0] > mayores_salida[0]:

            mayores_salida[2]=mayores_salida[1]
            mayores_salida[1]=mayores_salida[0]
            mayores_salida[0]= aux[x][0]

            id_mayores_salida[2]=id_mayores_salida[1]
            id_mayores_salida[1]=id_mayores_salida[0]
            id_mayores_salida[0]= x

        elif aux[x][0] > mayores_salida[1]: 

            mayores_salida[2]=mayores_salida[1]
            mayores_salida[1]=aux[x][0]

            id_mayores_salida[2]=id_mayores_salida[1]
            id_mayores_salida[1]= x

        elif aux[x][0] > mayores_salida[2]:

            mayores_salida[2]=aux[x][0]
            id_mayores_salida[2]= x

# Loop para determinar top salida

    for x in aux:

        if aux[x][1] > mayores_llegada[0]:

            mayores_llegada[2]=mayores_llegada[1]
            mayores_llegada[1]=mayores_llegada[0]
            mayores_llegada[0]= aux[x][1]

            id_mayores_llegada[2]=id_mayores_llegada[1]
            id_mayores_llegada[1]=id_mayores_llegada[0]
            id_mayores_llegada[0]= x

        elif aux[x][1] > mayores_llegada[1]: 

            mayores_llegada[2]=mayores_llegada[1]
            mayores_llegada[1]=aux[x][1]

            id_mayores_llegada[2]=id_mayores_llegada[1]
            id_mayores_llegada[1]= x

        elif aux[x][0] > mayores_llegada[2]:

            mayores_llegada[2]=aux[x][1]
            id_mayores_llegada[2]= x

# Loop para determinar top menor utilizado

    for x in aux:
        if aux[x][2] < menores[0]:

            menores[2]=menores[1]
            menores[1]=menores[0]
            menores[0]= aux[x][2]

            id_menores[2]=id_menores[1]
            id_menores[1]=id_menores[0]
            id_menores[0]= x

        elif aux[x][2] < menores[1]: 

            menores[2]=menores[1]
            menores[1]=aux[x][2]

            id_menores[2]=id_menores[1]
            id_menores[1]= x

        elif aux[x][2] < menores[2]:

            menores[2]=aux[x][2]
            id_menores[2]= x

    
    print("El Id del top de estaciones de salida (consecutivamente) son: ", id_mayores_salida, ", Los respectivos valores de cada uno (consecutivamente) son: ", mayores_salida)
    print("El Id del top de estaciones de llegada (consecutivamente) son: ", id_mayores_llegada, ", Los respectivos valores de cada uno (consecutivamente) son: ", mayores_llegada)
    print("El Id del top de estaciones menos utilizadas (consecutivamente) son: ", id_menores, ", Los respectivos valores de cada uno (consecutivamente) son: ", menores)
    





















#input:tiempo max resistencia (minutos)
#input: id estacion inicial
#output:rutas desde estacion salida
#output: nombre estacion inicio
#output: nombre estacion final
#output: duracion estimada
def optionSix():
    
    #time = input("ingrese tiempo maximo de resistencia")
    #unformattedtime =int(5)

    #tiempoDisponible=int(input(" Tiempo de resistencia " ))
    #initialStation=input("Inserte el punto de partida Station ID, Ejemplo 72, 79, 82, 83, 119, 120: " )


    tiempoDisponible =int(120)
    initialStation=str(72)


    #controller.minimumCostPaths(cont, initialStation)
    scc3=controller.connectedwithID_1(cont,initialStation)
    contador=0
    listaReverse= lt.newList()
    listaReverse=scc3['reversePost']
    print (listaReverse)
    dfsAns=dfs.DepthFirstSearch(cont['connections'], initialStation)
    


    j=0
    listaDSF= lt.newList()
    tam=len(listaReverse)
    verX=listaReverse[tam-6]
    verY=listaReverse[0]
    dfsAnsPathVerX=dfs.pathTo(dfsAns, verX)
    print (dfsAnsPathVerX)    
    print (" ")
    print ("path desde ", verX, " a ",  initialStation)
    dfsAnsPathVerY=dfs.pathTo(dfsAns, verY)
    print (dfsAnsPathVerY)    
    print (" ")
    print ("path desde ", verY, " a ",  initialStation)
    stackTam=stack.size(dfsAnsPathVerX)
    ruta1=lt.newList()
    for i in range (0,stackTam):
        punto=stack.pop(dfsAnsPathVerX)
        ruta1[i]=punto
    
    tiempoRuta1=0   
    print("")
    print ("Ruta lineal")
    print("")
    for i in range (0,stackTam-1):
        nodo = gr.getEdge(cont['connections'], ruta1[i], ruta1[i+1])
        tiempoRuta1= tiempoRuta1+ nodo['weight'] +10
        print ("Sale de: ", ruta1[i], " a ", ruta1[i+1], " tiempo de resistencia: ", round(tiempoRuta1,0))





def optionSeven():
    pass


    controller.loadServices_REQ5(cont,servicefile,aux, edades)
    
    #establecer_rango_de_edad:

    edad_min=None
    edad_max=None


    print("\n")
    print("****************************************************")
    print("¿En que rango de edad se encuentra usted?")
    print("[ 1 ] 0-10")
    print("[ 2 ] 11-20")
    print("[ 3 ] 21-30")
    print("[ 4 ] 31-40")
    print("[ 5 ] 41-50")
    print("[ 6 ] 51-60")
    print("[ 7 ] +60")
    print("****************************************************")

    rango_edad=input("escriba su respuesta: ")

    if rango_edad == "1":
        edad_min=0
        edad_max=10

    elif rango_edad == "2":
        edad_min=11
        edad_max=20

    elif rango_edad == "3":
        edad_min=21
        edad_max=30

    elif rango_edad == "4":
        edad_min=31
        edad_max=40

    elif rango_edad == "5":
        edad_min=41
        edad_max=50

    elif rango_edad == "6":
        edad_min=51
        edad_max=60

    elif rango_edad == "7":
        edad_min=61
        edad_max=135
    

    #Desarrollo del requerimiento


    r_inicio={}
    r_final={}
    
    inicial=""
    final=""

    i=0
    j=0

    for estacion in edades:
        y=0
        z=0
        for x in range(edad_min,edad_max):

            y += edades[estacion][0][x]
            z += edades[estacion][1][x]  

        r_inicio[estacion]=y
        r_final[estacion]=z


    for id_est in r_inicio:

        if r_inicio[id_est] > i:
            inicial=id_est
            i=r_inicio[id_est]

    for id_est in r_final:

        if r_final[id_est] > j:
            final=id_est
            j=r_final[id_est]

    
    print("La estacion en donde las personas de su rango de edad inician mas viajes es: ", inicial)
    print("La estacion en donde las personas de su rango de edad terminan mas viajes es: ", final)

    """

    camino=controller.minimumCostPaths(cont, inicial)
    print(camino)
    camino_final=controller.minimumCostPath(camino, final)
    print(camino_final)

    """



















def optionEight():
    pass

def optionNine():
    pass

def optionTen():
    pass



"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()
        aux={}

    elif int(inputs) == 2:
        executiontime = timeit.timeit(optionTwo, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs) == 3:
        executiontime = timeit.timeit(optionThree, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs) == 4:
        #msg = "Estación Base (Ej: 72): "
        #initialStation = input(msg)
        executiontime = timeit.timeit(optionFour, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs) == 5:
        executiontime = timeit.timeit(optionFive, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs) == 6:
        #destStation = input("Estación destino (Ej: 15151-10): ")
        #destStation = 72
        executiontime = timeit.timeit(optionSix, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs) == 7:
        edades = {}
        executiontime = timeit.timeit(optionSeven, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    
    elif int(inputs) == 8:
        executiontime = timeit.timeit(optionEight, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    
    elif int(inputs) == 9:
        executiontime = timeit.timeit(optionNine, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    
    elif int(inputs) == 10:
        executiontime = timeit.timeit(optionTen, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    else:
        sys.exit(0)
sys.exit(0)