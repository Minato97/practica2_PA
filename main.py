from Universidad.carrera import Carrera
from Universidad.alumno import Alumno


def menu():
    alumno = Alumno()
    opcion = int(input("\nIngrese una opción: "))
    if opcion == 1:
        alumno.registrar()
        menu()
    elif opcion == 2:
        alumno.mostrar()
        menu()

menu()