from Universidad.carrera import Carrera
from Universidad.materia import Materia
from Universidad.profesor import Profesor
from Universidad.alumno import Alumno, lista_alumnos

def menu():
    carrera = Carrera()
    materia = Materia()
    #profesor = Profesor()
    alumno = Alumno()
    carrera.llenar_lista_carrera()
    alumno.llenar_lista_alumno()
    materia.llenar_lista_materia()
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
    elif opcion == 5:    
        #---MENÚ CARRERA---#
        carrera.menu_carrera()
    elif opcion == 6:    
        #---MENÚ MATERIA---#
        materia.menu_materias()
    elif opcion == 7:    
        #---MENÚ PROFESOR---#
        #profesor.menu_profesor()
        pass

menu()