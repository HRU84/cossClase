import os
import time
import csv


def unpartido(equipo1,Marcador1,Equipo2):
    print('1 partido',equipo1,Marcador1,Equipo2, end= ' : ')
    goles1 = int(Marcador1[0])
    goles2 = (Marcador1[2])
    if goles1 > goles2:
        print(equipo1, 'Es el ganador')
    else :
        if goles2 > goles1 :
            print(Equipo2, 'Es el ganador')
        else:
            print('empate')
#fin def

def dospartidos(equipo1,Marcador1,Marcador2,Equipo2):
    print('2 partidos',equipo1,Marcador1,Marcador2,Equipo2)
#fin def

def trespartidos(equipo1,Marcador1,Marcador2,Marcador3,Equipo2):
    print('2 partidos',equipo1,Marcador1,Marcador2,Marcador3,Equipo2)
#fin def
    
#limpia la pantalla
os.system("cls")
#tiempo antes de mostrar lo siguiente
#time.sleep(.5)


with open ('C:\\Users\\CETECOM\\Desktop\\FinalesLibertadores.csv', 'r', encoding= 'utf-8') as entrada:
    print ('abrimos el archivo')
    contenido = csv.DictReader(entrada)
    for linea in contenido :
        #print (linea)
        
        año = int(linea['Año'])
        equipo1 =  linea['Equipo1'],
        Pais1 =  linea['Pais1'],
        Marcador1 =  linea['Marcador1'],
        Marcador2 = linea['Marcador2'],
        Marcador3 =  linea['Marcador3'],
        Equipo2 =  linea['Equipo2'],
        Pais2 =  linea['Pais2']
        
        print (año,end = ': ')
        if año < 1988 :
            #print('son 3 partidos')
            trespartidos(equipo1,Marcador1,Marcador2,Marcador3,Equipo2)
        else :
            if año < 2019:
                #print('Son 2 partidos')
                dospartidos(equipo1,Marcador1,Marcador2,Equipo2)
            else :
                #print ('Es 1 partido')
                unpartido(equipo1, Equipo2,Marcador1)
            #fin if
        #fin if
        
        #print(año)
        time.sleep(2)
    #fin for 
#fin with
print ('cerramos el archivo')