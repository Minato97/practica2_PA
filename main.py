from Universidad.carrera import Carrera
from Universidad.alumno import Alumno


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
        alumno.mostrar()
        menu()
    elif opcion == 3:
        carrera.mostrar()
        menu()


menu()