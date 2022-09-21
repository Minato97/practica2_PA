import alumno

lista_materias = list()

class Materia:

    def __init__(self,nombre,titular, lista_alumnos):
        self.nombre = nombre
        self.titular = titular
        self.lista_alumnos = lista_alumnos

    def agregarAlumno(self):
        try:
            nuevo= alumno.Alumno.buscar_alumno(1)
            lista_materias.append(nuevo)
            print("nuevo alumno agregado a la materia")
        except:
            print("error, no se agregó el alumno")

    def eliminarAlumno(self):
        eliminar = alumno.Alumno.buscar_alumno(1)
        for alum in lista_materias:
            try:
                if eliminar == alum:
                    lista_materias.remove(alum)
                    print(f"Alumno con matricula: {alumno} ha sido eliminado.")
            except:
                print("No se encontró el alumno a eliminar")

    def listarAlumnos(self):
        print(lista_materias)

    def prueba(self):
        print("instancia")


