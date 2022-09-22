from Universidad.alumno import Alumno
from Universidad.materia import Materia

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

