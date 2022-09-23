from datetime import date
# from relativedelta import relativedelta


lista_alumnos = list()

class Alumno:

    def __init__(self,matricula="",nombre="",fecha_nacimiento="",fecha_ingreso="",genero="",ciudad=""):
        self.matricula = matricula
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.genero = genero
        self.ciudad = ciudad


    def registrar_alumno(self):
        print("\nFormulario de registro de alumnos\n")

        alumno = Alumno()
        alumno.matricula = int(input("Introduzca su número de matricula: "))
        alumno.nombre = input("\nIntruduzca su nombre")
        print("\nIngrese su fecha de nacimiento:")
        anio = int(input("\nIntroduzca el año"))
        mes = int(input("\nIntroduzca el mes"))
        dia = int(input("\nIntroduzca el dia"))
        alumno.fecha_nacimiento = date(anio, mes, dia)
        print("\nIngrese su fecha de ingreso:")
        anio = int(input("\nIntroduzca el año"))
        mes = int(input("\nIntroduzca el mes"))
        dia = int(input("\nIntroduzca el dia"))
        alumno.fecha_ingreso = date(anio, mes, dia)
        alumno.genero = input("\nIngrese su genero")
        alumno.ciudad = input("\nIngrese su ciudad de origen")

        lista_alumnos.append(alumno)

    def mostrar_alumno(self,alum):
        print("Matricula: ", alum.matricula, "\nNombre: ", alum.nombre, "\nfecha de nacimiento: ", alum.fecha_nacimiento, "\nFecha de ingreso: ", alum.fecha_ingreso, "\nCiudad de origen: ", alum.ciudad, "\nGenero: ", alum.genero)


    def buscar_alumno(self):
        buscar = int(input("\nIngrese la matricula del alumno: "))
        # print(buscar)
        for alum in lista_alumnos:
            if buscar == alum.matricula:
                # alum.mostrar()
                print("encontrado")
                return alum

        print("Usuario no encontrado, por favor intentelo de nuevo\n")
        self.buscar_alumno()


    # def calcularEdad(self, fecha_nacimiento):
    #     fecha_nacimiento = date.strptime(fecha_nacimiento, "%d/%m/%Y")
    #     edad = relativedelta(date.now(), fecha_nacimiento)
    #     return (f"{edad.years} años")

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


# Alumno.llenar_lista_alumno(lista_alumnos)