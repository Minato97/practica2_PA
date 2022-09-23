from Universidad.alumno import Alumno
from Universidad.materia import Materia
#import main
import os

lista_carreras = list()
materia = Materia()
class Carrera:

    def __init__(self,nombre="",materias=[]):
        self.nombre = nombre
        self.lista_materias_carrera = materias

    def registrar_profesor(self):
        print("\t\n--->Formulario de registro de carreras\n")

        prof = Profesor()
        prof.no_empleado = int(input("Introduzca su número de trabajador: "))
        prof.nombre = input("\nIntruduzca su nombre: ")
        print("\nIngrese su fecha de ingreso:")
        try:
            dia = int(input("\nIntroduzca el dia: "))
            mes = int(input("\nIntroduzca el mes: "))
            anio = int(input("\nIntroduzca el año: "))
            dia = str(dia)
            mes = str(mes)
            anio = str(anio)
            prof.fecha_ingreso = dia + "/" + mes + "/" + anio
        except TypeError:
            print("ingrese solo valores numericos")
        lista_profesores.append(prof)

    def agregarMateria(self,carrera):
        print("\t\t---Agregar Materia ---\n")
        try:
            nuevo = materia.buscar_materia()
            carrera.lista_materias_carrera.append(nuevo)
            print("\nNueva materia agregada a la carrera correctamente")
            # print(self.lista_materias)
        except:
            print("\nError, no se agregó la materia")

    def eliminarMateria(self,carrera):
        print("\t\t---Eliminar materia ---\n\n")
        eliminar = materia.buscar_materia()
        for mat in carrera.lista_materias_carrera:
            try:
                if eliminar == mat:
                    carrera.lista_materias_carrera.remove(mat)
                    print(f"La materia con nombre: {mat.nombre} ha sido eliminada de la carera: {carrera.nombre}.")
            except:
                print("No se encontró la materia a eliminar")

    def mostrar_carreras(self):
        for car in lista_carreras:
            print("Nombre: ", car.nombre, "\n")

    def mostrar_materias_carrera(self,carrera):
        print("\nLas materias registradas en la carrera:\n")
        for mat in carrera.lista_materias_carrera:
            mat.mostrar_materias(mat)



    def llenar_lista_carrera(self):
        carrera = Carrera("Electrónica y computación")
        lista_carreras.append(carrera)
        carrera = Carrera("Psicología")
        lista_carreras.append(carrera)
        carrera = Carrera("Contabilidad")
        lista_carreras.append(carrera)
        carrera = Carrera("Administración")
        lista_carreras.append(carrera)
        carrera = Carrera("Tecnologías")
        lista_carreras.append(carrera)
        carrera = Carrera("Gerontología")
        lista_carreras.append(carrera)

    def buscar_carrera(self):
        buscar = input("\nIngrese el nombre de la carrera: ")
        for car in lista_carreras:
            if buscar == car.nombre:
                # print("encontrado")
                return car

        print("Materia no encontrada, por favor intentelo de nuevo\n")
        self.buscar_carrera()
    
    def getNombre(self):
        return self.nombre

    def getMaterias(self):
        return self.lista_materias_carrera

    def setNombre(self):
        return self.nombre

    def setMaterias(self):
        return self.lista_materias_carrera

    def menu_carrera(self):
        print("""
        ---Este es el menú de carreras---
        Ingrese alguna de las siguientes opciones:
        1.- Agregar materia a una carrera
        2.- Eliminar materia de una carrera 
        3.- Listar materias de una carrera
        4.- Listar todas las carreras
        5.- Volver al menú principal
        """)
        try:
            opc = int(input("\n"))
        except ValueError:
            print("Ingrese una opción válida")
            self.menu_carrera()
        if opc == 1:
            os.system("cls")
            carrera = self.buscar_carrera()
            self.agregarMateria(carrera)
            self.menu_carrera()
        elif opc == 2:
            os.system("cls")
            carrera = self.buscar_carrera()
            self.eliminarMateria(carrera)
            self.menu_carrera()
        elif opc == 3:
            os.system("cls")
            carrera = self.buscar_carrera()
            self.mostrar_materias_carrera(carrera)
            self.menu_carrera()
        elif opc == 4:
            os.system("cls")
            self.mostrar_carreras()
            self.menu_carrera()
        elif opc == 5:

            pass
        else:
            print("Ingrese una de las opciones indicadas anteriormente")
            self.menu_materias()