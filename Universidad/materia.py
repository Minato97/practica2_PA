from Universidad.alumno import Alumno
import os

lista_materias = list()

alumno = Alumno()

class Materia:

    def __init__(self,nombre="",titular="", lista_alumnos=[]):
        self.nombre = nombre
        self.titular = titular
        self.lista_alumnos = lista_alumnos

    def llenar_lista_materia(self):
        materia = Materia('Multimedia', "Carlos Verdín")
        lista_materias.append(materia)
        materia = Materia('Programación avanzada', "José Cervantes")
        lista_materias.append(materia)
        materia = Materia('Cálculo de varias variables', "Janet Torrealba")
        lista_materias.append(materia)
        materia = Materia('Ecuaciones Diferenciales', "Eric Martínez")
        lista_materias.append(materia)
        materia = Materia('Diseño Electrónico Analógico', "Julio Rodriguez")
        lista_materias.append(materia)
        materia = Materia('Redes Inalambricas y Móviles', "José Luis Fausto")
        lista_materias.append(materia)

    def agregarAlumno(self):
        print("\t\t---Agregar alumno ---\n\n")
        try:
            nuevo = alumno.buscar_alumno()
            self.lista_alumnos.append(nuevo)
            print("nuevo alumno inscrito a la materia")
            print(self.lista_alumnos)
        except:
            print("error, no se pudo inscribir el alumno a la materia")

    def eliminarAlumno(self):
        print("\t\t---Eliminar alumno ---\n\n")
        eliminar = alumno.buscar_alumno()
        for alum in self.lista_alumnos:
            try:
                if eliminar == alum:
                    self.lista_alumnos.remove(alum)
                    print(f"Alumno con matricula: {alum.matricula} ha sido eliminado.")
            except:
                print("No se encontró el alumno a eliminar")

    def listarAlumnos(self):
        print("\t\t---Listar alumnos ---\n\n")
        for alum in self.lista_alumnos:
            alumno.mostrar(alum)
            # print("Matricula: ", alum.matricula, "\nNombre: ", alum.nombre, "\nfecha de nacimiento: ",
            #       alum.fecha_nacimiento, "\nFecha de ingreso: ", alum.fecha_ingreso, "\nCiudad de origen: ",
            #       alum.ciudad, "\nGenero: ", alum.genero)

    def buscar_materia(self):
        buscar = input("\nIngrese el nombre de la materia a buscar: ")
        for mat in lista_materias:
            if buscar == mat.nombre:

                # print("encontrado")
                return mat
            else:
                print("Materia no encontrada, por favor intentelo de nuevo\n")
                self.buscar_materia()

    def mostrar(self,materia):
        print("Nombre: ", materia.nombre, "\nProfesor: ", materia.titular,"\n")


    def listarMaterias(self):
        print("Lista de materias\n")
        print(lista_materias)

    def menu_materias(self):
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
            self.menu_materias()
        if opc == 1:
            os.system("cls")
            self.agregarAlumno()
            self.menu_materias()
        elif opc == 2:
            os.system("cls")
            self.eliminarAlumno()
            self.menu_materias()
        elif opc == 3:
            os.system("cls")
            self.listarAlumnos()
            self.menu_materias()
        else:
            print("Ingrese una de las opciones indicadas anteriormente")
            self.menu_materias()


