from Universidad.alumno import Alumno
from Universidad.materia import Materia
#import main
import os

lista_carreras = list()
materia = Materia()
class Carrera:

    def __init__(self,nombre="",materias=[]):
        self.nombre = nombre
        self.lista_materias = materias

    def agregarMateria(self):
        print("\t\t---Agregar Materia ---\n\n")
        try:
            nuevo = materia.buscar_alumno()
            self.lista_alumnos.append(nuevo)
            print("nuevo alumno agregado a la materia")
            print(self.lista_alumnos)
        except:
            print("error, no se agregó el alumno")

    def eliminarMateria(self):
        print("\t\t---Eliminar alumno ---\n\n")
        eliminar = alumno.buscar_alumno()
        for alum in self.lista_alumnos:
            try:
                if eliminar == alum:
                    self.lista_alumnos.remove(alum)
                    print(f"Alumno con matricula: {alumno} ha sido eliminado.")
            except:
                print("No se encontró el alumno a eliminar")

    def listarMaterias(self):
        print("\t\t---Listar alumnos ---\n\n")
        for alum in self.lista_alumnos:
            print("Matricula: ", alum.matricula, "\nNombre: ", alum.nombre, "\nfecha de nacimiento: ",
                  alum.fecha_nacimiento, "\nFecha de ingreso: ", alum.fecha_ingreso, "\nCiudad de origen: ",
                  alum.ciudad, "\nGenero: ", alum.genero)

    def mostrar(self):
        cont = 0
        for car in lista_carreras:
            cont += 1
            print(f"{cont}: ", car.nombre, "\nlista de materias: ", car.materias)
            print("\n")

    def llenar_lista_carrera(self):
        carrera = Carrera("Electrónica y computación")
        lista_carreras.append(carrera)
        carrera = Carrera("Psicología")
        lista_carreras.append(carrera)
        carrera = Carrera("Contabilidad")
        lista_carreras.append(carrera)
        carrera = Carrera("Administración")
        lista_carreras.append(carrera)
        carrera = Carrera("Tecnológias")
        lista_carreras.append(carrera)
        carrera = Carrera("Gerontología")
        lista_carreras.append(carrera)

    def agregar_Materia(self, materia):
        pass 

    def eliminar_Materia(self, materia):
        pass

    def listar_Materias(self, carrera):
        print(f"\t\t\t\t\t\t\t\t---Carrera de {carrera}---\nLista de Materias: \n")
        for mat in self.materias:
            print("Nombre: ", mat.nombre, "\nTitular: ", mat.titular, "\nAlumnos inscritos:\n")
            #listar_alumnos().Materia()
        print("\n1.- Registrar nueva materia a la carrera\n2.- Salir\n")
        try: 
            opc = int(input())
            if opc == 1:
                self.agregar_Materia()
            elif opc == 2:
                os.system("cls")
                self.menu_carrera()
            else:
                os.system("cls")
                self.listar_Materias("Electrónica y Computación")
        except ValueError:
            print("ingrese un dato válido")
            os.system("cls")
            self.listar_Materias("Electrónica y Computación")

    def menu_carrera(self):
        print("\t\t\t\t\t\t\t\t---Este es el menú de carreras---\nCarreras actuales:\n")
        self.mostrar()
        print("Presione en número de la carrera para ver más opciones\nPresione 7 para salir al menú principal.")
        try:
            opc =int(input())
        except ValueError:
            print("Ingrese una opcion válida")
            self.menu_carrera()
        if opc == 1:
            os.system("cls")
            self.listar_Materias("Electrónica y computación")
        elif opc == 2:
            os.system("cls")
            self.listar_Materias("Psicología")
        elif opc == 3:
            os.system("cls")
            self.listar_Materias("Contabilidad")
        elif opc == 4:
            os.system("cls")
            self.listar_Materias("Administración")
        elif opc == 5:
            os.system("cls")
            self.listar_Materias("Tecnológias")
        elif opc == 6:
            os.system("cls")
            self.listar_Materias("Gerontología")
        elif opc == 7:
            #salir
            pass
        else: 
            print("Ingrese alguna de las opciones anteriormente mencionadas")
            os.system("cls")
            self.menu_carrera()
    
    def getNombre(self):
        return self.nombre

    def getMaterias(self):
        return self.materias

    def setNombre(self):
        return self.nombre

    def setMaterias(self):
        return self.materias
