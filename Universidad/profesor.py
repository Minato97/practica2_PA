from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
# from Universidad.materia import Materia

lista_profesores = list()

# materia = Materia()
class Profesor:

    def __init__(self, no_empleado=int, nombre=str, fecha_ingreso=str):
        self.no_empleado = no_empleado
        self.nombre = nombre
        self.fecha_ingreso = fecha_ingreso

    def llenar_lista_profesor(self):
        profesor = Profesor(11, "Carlos Verdín", "12/12/2000")
        lista_profesores.append(profesor)
        profesor = Profesor(12, "José Cervantes", "12/12/2004")
        lista_profesores.append(profesor)
        profesor = Profesor(13, "Janet Torrealba", "12/12/2006")
        lista_profesores.append(profesor)
        profesor = Profesor(13, "Eric Martínez", "12/12/2008")
        lista_profesores.append(profesor)
        profesor = Profesor(14, "Julio Rodriguez", "12/12/2010")
        lista_profesores.append(profesor)

    def menu_profesor(self):
        print("""                 <---Este es el menú de Profesores--->

        1.- Registrar a un nuevo profesor
        2.- Mostrar los profesores registrados
        3.- Calcular la antiguedad de un profesor

        """)
        try:
            opc = int(input())
        except ValueError:
            print("Ingrese una de las opciones")

        if opc == 1:
            self.registrar_profesor()
            self.menu_profesor()
        elif opc == 2:
            self.mostrar()
            self.menu_profesor()
        elif opc == 3:
            prof = input("Ingrese el nombre completo del profesor a calcular su edad: ")
            self.calcular_antiguedad(prof)
            print(prof)
        elif opc == 4:
            pass
        else:
            os.system("cls")
            print("Ingrese una opción válida.")
            self.menu_profesor()

    def registrar_profesor(self):
        print("\t\n--->Formulario de registro de profesores\n")

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

    def mostrar(self):
        print("\t>---\nProfesores registrados:\n")
        for prof in lista_profesores:
            print("No.Empleado:", prof.no_empleado, "\nNombre:", prof.nombre, "\nFecha de ingreso:", prof.fecha_ingreso,
                  "\n")
    def buscar_profesor(self):
        buscar = int(input("\nIngrese el número de empleado: "))
        # print(buscar)
        for prof in lista_profesores:
            if buscar == prof.no_empleado:
                # alum.mostrar()
                print("encontrado")
                return prof

        print("Profesor no encontrado\n")
        # materia.menu_materias()

    def calcular_antiguedad(self, nombre_profesor):
        for prof in lista_profesores:
            if prof.nombre == nombre_profesor:
                fecha_ingreso = prof.fecha_ingreso
                fecha_ingreso = datetime.strptime(fecha_ingreso, "%d/%m/%Y")
                edad = relativedelta(datetime.now(), fecha_ingreso)
                print(f"{edad.years} años, {edad.months} meses y {edad.days} días")
                os.system("pause")
                self.menu_profesor()
        os.system("cls")
        print("No se pudo encontrar al PROFESOR, favor de verificar sus datos")
        self.menu_profesor()


# prof = Profesor()
# prof.llenar_lista_profesor()
# prof.menu_profesor()