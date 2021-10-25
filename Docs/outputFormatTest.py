# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:34:54 2021

@author: bbaruque
"""

def load_answer(file):
    
    in_file = open (file, "r")
    contentLines = in_file.readlines()
    in_file.close()

    rides = {}

    for v, line in enumerate(contentLines):
        vehic = line.split(' ')
        rides[v] = (list(map(int, vehic[1:])))
    
    return rides

if __name__ == "__main__":
    
    # Incluir aquí la ruta del fichero sobre el que se quiere probar
    # Include here the path to the file to test its format
    file_a = "./qualification_round_2018.out/example.out"
    
    rides = load_answer(file_a)
    
    print(rides)

    for v in rides:
        print('Vehiculo: '+str(v)+' Realiza los viajes: '+str(rides[v])+' en este orden')
        print('Vehicle: '+str(v)+' Completes the rides (in order): '+str(rides[v]))