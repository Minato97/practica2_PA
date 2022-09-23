import sys

from Universidad.carrera import Carrera
from Universidad.materia import Materia
from Universidad.profesor import Profesor
from Universidad.alumno import Alumno

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
        4.- Salir del programa
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
        sys.exit("\nGracias por usar software de calidad")
    else:
        os.system("cls")
        print("Ingrese una opción válida.")
        menu()
menu()