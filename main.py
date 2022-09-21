from Universidad.materia import Materia
from Universidad.carrera import Carrera
from Universidad.alumno import Alumno, lista_alumnos


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
    print("Este es el menú de materias")
    Materia.prueba(1)

menu_materias()