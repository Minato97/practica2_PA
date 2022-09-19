import datetime



lista_alumnos = list()



class Alumno:

    def __init__(self,matricula="",nombre="",fecha_nacimiento="",fecha_ingreso="",genero="",ciudad=""):
        self.matricula = matricula
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.genero = genero
        self.ciudad = ciudad

    def registrar(self):
        print("\nMenú de registro\n")

        alumno = Alumno()
        alumno.matricula = int(input("Introduzca su número de matricula: "))
        alumno.nombre = input("\nIntruduzca su nombre")
        print("\nIngrese su fecha de nacimiento:")
        anio = int(input("\nIntroduzca el año"))
        mes = int(input("\nIntroduzca el mes"))
        dia = int(input("\nIntroduzca el dia"))
        alumno.fecha_nacimiento = datetime.date(anio, mes, dia)
        print("\nIngrese su fecha de ingreso:")
        anio = int(input("\nIntroduzca el año"))
        mes = int(input("\nIntroduzca el mes"))
        dia = int(input("\nIntroduzca el dia"))
        alumno.fecha_ingreso = datetime.date(anio, mes, dia)
        alumno.genero = input("\nIngrese su genero")
        alumno.ciudad = input("\nIngrese su ciudad de origen")

        lista_alumnos.append(alumno)

    def mostrar(self):
        for alum in lista_alumnos:
            print("Matricula: ", alum.matricula, "\nNombre: ", alum.nombre, "\nfecha de nacimiento: ", alum.fecha_nacimiento, "\nFecha de ingreso: ", alum.fecha_ingreso, "\nCiudad de origen: ", alum.ciudad, "\nGenero: ", alum.genero)
            print("\n")







