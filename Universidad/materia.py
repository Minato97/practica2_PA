from Universidad.alumno import Alumno
import os
# import main
# from main import menu
lista_materias = list()

alumno = Alumno()

class Materia:

    def __init__(self,nombre="",titular="", lista_alumnos=[]):
        self.nombre = nombre
        self.titular = titular
        self.lista_alumnos = lista_alumnos

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
            nuevo = alumno.buscar_alumno()
            print(nuevo)
            materia.lista_alumnos.append(nuevo)
            print("\nNuevo alumno inscrito a la materia")
            # print(materia.lista_alumnos)
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
        buscar = input("\nIngrese el nombre de la materia: ")
        for mat in lista_materias:
            if buscar == mat.nombre:
                # print("encontrado")
                return mat
        print("Materia no encontrada, por favor intentelo de nuevo\n")
        self.buscar_materia()

    def mostrar_materias(self,mat):
        print("Nombre: ", mat.nombre, "\nProfesor: ", mat.titular,"\n")
            # self.mostrar_alumnos_inscritos(mat)

    def mostrar_alumnos_inscritos(self,materia):
        print("\nLos alumnos inscritos a la materia son:\n")
        for alum in materia.lista_alumnos:
            alum.mostrar_alumno(alum)


    def menu_materias(self):
        print("""
        ---Este es el menú de materias---
        Ingrese alguna de las siguientes opciones:
        1.- Agregar alumno a una materia
        2.- Eliminar alumno de una materia 
        3.- Listar alumnos los alumnos inscritos a una materia
        4.- Listar todas la materias
        5.- Volver al menú principal
        """)
        try:
            opc = int(input())
        except ValueError:
            print("Ingrese una opción válida")
            self.menu_materias()
        if opc == 1:
            os.system("cls")
            materia = self.buscar_materia()
            print(materia)
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
            for mat in lista_materias:
                self.mostrar_materias(mat)
            self.menu_materias()
        elif opc == 5:

            pass
        else:
            print("Ingrese una de las opciones indicadas anteriormente")
            self.menu_materias()


