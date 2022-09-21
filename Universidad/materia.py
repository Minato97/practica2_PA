import Universidad.alumno as alumno

lista_materias = list()
numeros = [1, 2, 3]
lista_materias.append(numeros)

class Materia:

    def __init__(self,nombre,titular, lista_alumnos):
        self.nombre = nombre
        self.titular = titular
        self.lista_alumnos = lista_alumnos

    def agregarAlumno(self):
        print("\t\t---Agregar alumno ---\n\n")
        try:
            nuevo= alumno.Alumno.buscar_alumno(1)
            lista_materias.append(nuevo)
            print("nuevo alumno agregado a la materia")
            print(lista_materias)
        except:
            print("error, no se agregó el alumno")

    def eliminarAlumno(self):
        print("\t\t---Eliminar alumno ---\n\n")
        eliminar = alumno.Alumno.buscar_alumno(1)
        for alum in lista_materias:
            try:
                if eliminar == alum:
                    lista_materias.remove(alum)
                    print(f"Alumno con matricula: {alumno} ha sido eliminado.")
            except:
                print("No se encontró el alumno a eliminar")

    def listarAlumnos(self):
        print("\t\t---Listar alumnos ---\n\n")
        print(lista_materias)

    def prueba(self):
        print("instancia")


