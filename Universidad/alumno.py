from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import os



lista_alumnos = list()

class Alumno:

    def _init_(self,matricula="",nombre="",fecha_nacimiento="",fecha_ingreso="",genero="",ciudad=""):
        self.matricula = matricula
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.genero = genero
        self.ciudad = ciudad

    def menu_alumno(self):
        print("""                 <---Este es el menú de Alumnos--->

        1.- Registrar a un nuevo alumno
        2.- Mostrar los alumnos registrados
        3.- Buscar Alumno
        4.- Calcular la edad de un alumno
        5.- Regresar al menú principal

        """)
        try:
            opc = int(input())
        except ValueError:
            print("Ingrese una de las opciones")

        if opc == 1:
            self.registrar_alumno()
            self.menu_alumno()
        elif opc == 2:
            for alum in lista_alumnos:
                self.mostrar_alumno(alum)
            self.menu_alumno()
        elif opc == 3:
            alum = self.buscar_alumno()
            self.mostrar_alumno(alum)
            self.menu_alumno()
        elif opc == 4:
            alum = input("ingrese el nombre completo del alumno a calcular su edad: ")
            self.calcular_edad(alum)
        elif opc == 5:
            pass
        else:
            os.system("cls")
            print("-->Ingrese una opción válida.\n")
            self.menu_alumno()

    def registrar_alumno(self):
        os.system("cls")
        print("\t\t\t\n<---Formulario de registro de alumnos--->\n")
        alumno = Alumno()
        alumno.matricula = int(input("Introduzca su número de matricula: "))
        alumno.nombre = input("\nIntruduzca su nombre: ")
        print("\nIngrese su fecha de nacimiento:")
        anio = int(input("\nIntroduzca el año: "))
        mes = int(input("\nIntroduzca el mes: "))
        dia = int(input("\nIntroduzca el dia: "))
        alumno.fecha_nacimiento = date(anio, mes, dia)
        print("\nIngrese su fecha de ingreso:")
        anio = int(input("\nIntroduzca el año: "))
        mes = int(input("\nIntroduzca el mes: "))
        dia = int(input("\nIntroduzca el dia: "))
        alumno.fecha_ingreso = date(anio, mes, dia)
        alumno.genero = input("\nIngrese su genero (M/F): ")
        alumno.ciudad = input("\nIngrese su ciudad de origen: ")

        lista_alumnos.append(alumno)

    def mostrar_alumno(self,alum):
        print("Matricula: ", alum.matricula, "\nNombre: ", alum.nombre, "\nfecha de nacimiento: ", alum.fecha_nacimiento, "\nFecha de ingreso: ", alum.fecha_ingreso, "\nCiudad de origen: ", alum.ciudad, "\nGenero: ", alum.genero, "\n")

    def buscar_alumno(self):
        os.system("cls")
        buscar = int(input("\nIngrese la matricula del alumno: "))
        for alum in lista_alumnos:
            if buscar == alum.matricula:
                print("encontrado")
                return alum

        print("Usuario no encontrado, por favor intentelo de nuevo\n")
        self.buscar_alumno()


    def calcular_edad(self, nombre_alumno):
        for alumn in lista_alumnos:
            if alumn.nombre == nombre_alumno:
                edad = relativedelta(datetime.now(), alumn.fecha_ingreso)
                print(f"{edad.years} años, {edad.months} meses y {edad.days} días\n\n")
                self.menu_alumno()

        os.system("cls")
        print("No se pudo encontrar el alumno, favor de verificar sus datos")
        self.menu_alumno()

    def llenar_lista_alumno(self):
        alumno = Alumno(123, "Jose Antonio Fausto Guerrero", date(1996, 2, 24), date(1997, 1, 15), "Masculino", "Tala")
        lista_alumnos.append(alumno)
        alumno = Alumno(124, "Julio Cesar Preciado Hernandez", date(1995, 12, 4), date(1997, 1, 15), "Masculino", "Magdalena")
        lista_alumnos.append(alumno)
        alumno = Alumno(125, "Brenda Gutierrez Ramirez", date(1995, 11, 7), date(1997, 1, 15), "Femenino", "Magdalena")
        lista_alumnos.append(alumno)
        alumno = Alumno(126, "Luis Antonio Lopez Camacho", date(1997, 5, 16), date(1997, 1, 15), "Masculino", "Ameca")
        lista_alumnos.append(alumno)
        alumno = Alumno(127, "Roxana Uribe Robles", date(1995, 12, 4), date(1997, 1, 15), "Masculino", "Guadalajara")
        lista_alumnos.append(alumno)


# alum = Alumno()
# alum.llenar_lista_alumno()
# alum.menu_alumno()