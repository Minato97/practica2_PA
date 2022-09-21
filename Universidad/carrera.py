from Universidad.alumno import Alumno
from Universidad.materia import Materia

lista_carreras = list()

class Carrera:

    def __init__(self,nombre="",materias=[]):
        self.nombre = nombre
        self.materias = materias

    def mostrar(self):
        for car in lista_carreras:
            print("Nombre: ", car.nombre, "\nlista de materias: ", car.materias)
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

    def agregar_Materia(self,materia):
        pass

    def eliminar_Materia(self, materia):
        pass

    def listar_Materias(self):
        for mat in self.materias:
            print("Nombre ", mat.nombre, "\nTitular: ", mat.titular, "\nAlumnos inscritos:\n")
            listar_alumnos().Materia()
            print("\n")

    def getNombre(self):
        return self.nombre

    def getMaterias(self):
        return self.materias

    def setNombre(self):
        return self.nombre

    def setMaterias(self):
        return self.materias

