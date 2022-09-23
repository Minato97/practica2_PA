import sys
import time
from Universidad.carrera import Carrera
from Universidad.materia import Materia
from Universidad.profesor import Profesor
from Universidad.alumno import Alumno
import os

def menu():
    carrera = Carrera()
    materia = Materia()
    profesor = Profesor()
    alumno = Alumno()
    carrera.llenar_lista_carrera()
    alumno.llenar_lista_alumno()
    materia.llenar_lista_materia()
    profesor.llenar_lista_profesor()
    print("""
        ---Este es el menú principal---
        Ingrese alguna de las siguientes opciones:
        1.- Menú carrera
        2.- Menú materia 
        3.- Menú profesor
        4.- Menú alumno
        5.- Salir del programa
        
        """)
    opcion = int(input("\nIngrese una opción: "))
    if opcion == 1:
        #---MENÚ CARRERA---#
        carrera.menu_carrera()
        menu()
    elif opcion == 2:
        #---MENÚ MATERIA---#
        materia.menu_materias()
        menu()
    elif opcion == 3:
        #---MENÚ PROFESOR---#
        profesor.menu_profesor()
        menu()
    elif opcion == 4:
        #---MENÚ Alumno---#
        alumno.menu_alumno()
        menu()
    elif opcion == 5:
        cadena = "Gracias por usar software de calidad"

        for i in range(0,len(cadena)):
            print(cadena[i], end="")
            time.sleep(0.1)
        sys.exit()
    else:
        os.system("cls")
        print("Ingrese una opción válida.")
        menu()
menu()