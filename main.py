from Universidad.materia import Materia
from Universidad.carrera import Carrera
from Universidad.alumno import Alumno, lista_alumnos
import os

def menu():
    alumno = Alumno()
    carrera = Carrera()
    carrera.llenar_lista_carrera()
    alumno.llenar_lista_alumno()
    opcion = int(input("\nIngrese una opción: "))
    if opcion == 1:
        alumno.registrar()
        menu()
    elif opcion == 2:
        for alum in lista_alumnos:
            alum.mostrar(alum)
            print("\n")
        menu()
    elif opcion == 3:
        carrera.mostrar()
        menu()
    elif opcion == 4:
        alumno.buscar_alumno()
        menu()
#menu()

#menú de materia-----------------------------------------------------------
def menu_materias():
    MT = Materia()
    print("""
    ---Este es el menú de materias---
    Ingrese alguna de las siguientes opciones:
    1.- Agregar alumno 
    2.- Eliminar alumno 
    3.- Listar alumnos:
    4.- Volver al menú principal
    """)
    try:
        opc = int(input())
    except ValueError:
        print("ingrese una opción válida")
        menu_materias()
    if opc == 1:
        os.system("cls")
        MT.agregarAlumno()
        menu_materias()
    elif opc == 2:
        os.system("cls")
        MT.eliminarAlumno()
        menu_materias()
    elif opc == 3:
        os.system("cls")
        MT.listarAlumnos()
        menu_materias()
    else:
        print("Ingrese una de las opciones indicadas anteriormente")
        menu_materias()

menu_materias()