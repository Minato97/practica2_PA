from Universidad.alumno import Alumno
import os
from Universidad.profesor import Profesor

lista_materias = list()
alumno = Alumno()
profesor = Profesor()

class Materia:

    def __init__(self,nombre="",titular="", lista_alumnos=[]):
        self.nombre = nombre
        self.titular = titular
        self.lista_alumnos = lista_alumnos

    def registrar_materia(self):
        print("\t\n--->Formulario de registro de materias\n")

        materia = Materia()
        materia.nombre = input("\nIntruduzca el nombre de la materia: ")
        lista_materias.append(materia)

    def asignar_titular(self,materia):
        if materia.titular == "":
            profe = profesor.buscar_profesor()
            materia.titular = profe.nombre

    def llenar_lista_materia(self):
        materia = Materia("Multimedia", "Carlos Verdín")
        lista_materias.append(materia)
        materia = Materia("Programación avanzada", "José Cervantes")
        lista_materias.append(materia)
        materia = Materia("Cálculo de varias variables", "Janet Torrealba")
        lista_materias.append(materia)
        materia = Materia("Ecuaciones Diferenciales", "Eric Martínez")
        lista_materias.append(materia)
        materia = Materia("Diseño Electrónico Analógico", "Julio Rodriguez")
        lista_materias.append(materia)
        materia = Materia("Redes Inalambricas y Móviles", "José Luis Fausto")
        lista_materias.append(materia)

    def agregarAlumno(self,materia):
        print("\t\t---Agregar alumno ---\n\n")
        try:
            print("--> Alumnos registrados: \n")
            alumno.listar_alumnos_registrados()
            nuevo = alumno.buscar_alumno()
            materia.lista_alumnos.append(nuevo)
            print(f"\nNuevo alumno inscrito a {materia.nombre}")
        except:
            print("\nError, no se pudo inscribir el alumno a la materia")

    def eliminarAlumno(self,materia):
        print("\t\t---Eliminar alumno ---\n\n")
        eliminar = alumno.buscar_alumno()
        for alum in materia.lista_alumnos:
            try:
                if eliminar == alum:
                    materia.lista_alumnos.remove(alum)
                    print(f"Alumno con matricula: {alum.matricula} ha sido eliminado de la materia: {materia.nombre}.")
            except:
                print("No se encontró el alumno a eliminar")


    def buscar_materia(self):
        self.mostrar_materias_totales()
        buscar = input("\nIngrese el nombre de la materia: ")
        for mat in lista_materias:
            if buscar == mat.nombre:
                return mat
        print("Materia no encontrada\n")

    def mostrar_materias(self,mat):
        print("Nombre: ", mat.nombre, "\nProfesor: ", mat.titular, "\nAlumnos Registrados: ","\n")
        for alum in mat.lista_alumnos:
            alum.mostrar_alumno(alum)

    def mostrar_materias_totales(self):
        for mat in lista_materias:
            print("\nNombre:", mat.nombre, "\nTitular:", mat.titular,  "\n")

    def mostrar_alumnos_inscritos(self,materia):
        for alum in materia.lista_alumnos:
            alum.mostrar_alumno(alum)


    def menu_materias(self):
        print("""
                    <---Este es el menú de materias--->

        Ingrese alguna de las siguientes opciones:

        1.- Agregar alumno a una materia
        2.- Eliminar alumno de una materia 
        3.- Listar alumnos inscritos a una materia
        4.- Listar todas la materias
        5.- Registrar una nueva materia en el sistema
        6.- Asignar profesor a la materia
        7.- Volver al menú principal
        """)
        try:
            opc = int(input())
        except ValueError:
            print("Ingrese una opción válida")
            self.menu_materias()
        if opc == 1:
            os.system("cls")
            materia = self.buscar_materia()
            self.agregarAlumno(materia)
            self.menu_materias()
        elif opc == 2:
            os.system("cls")
            materia = self.buscar_materia()
            self.eliminarAlumno(materia)
            self.menu_materias()
        elif opc == 3:
            os.system("cls")
            materia = self.buscar_materia()
            self.mostrar_alumnos_inscritos(materia)
            self.menu_materias()
        elif opc == 4:
            os.system("cls")
            self.mostrar_materias_totales()
            self.menu_materias()
        elif opc == 5:
            os.system("cls")
            self.registrar_materia()
            self.menu_materias()
        elif opc == 6:
            os.system("cls")
            materia = self.buscar_materia()
            self.asignar_titular(materia)
        elif opc == 7:
            pass
        else:
            print("Ingrese una de las opciones indicadas anteriormente")
            self.menu_materias()


