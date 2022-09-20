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


