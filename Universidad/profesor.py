from datetime import date
# from dateutil.relativedelta import relativedelta




lista_profesores = list()

class profesor:

    def __init__(self,no_empleado,nombre,fecha_ingreso):
        self.no_empleado = no_empleado
        self.nombre = nombre
        self.fecha_ingreso = fecha_ingreso

    def getNoempleado(self):
        return self.no_empleado

    def getNombre(self):
        return self.nombre

    # def calcularEdad(self, fecha_ingreso):
    #     fecha_ingreso = date.strptime(fecha_ingreso, "%d/%m/%Y")
    #     antiguedad = relativedelta(date.now(), fecha_ingreso)
    #     return (f"{antiguedad.years} años")