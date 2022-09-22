from Universidad.alumno import Alumno


lista_materias = list()
materias = ['Multimedia', 'Programación avanzada', 'Cálculo de varias variables', 'Ecuaciones Diferenciales', 
'Diseño Electrónico Analógico', 'Redes Inalambricas y Móviles', 'Electricidad y Magnetismo']
lista_materias.append(materias)

alumno = Alumno()
class Materia:

    def __init__(self,nombre="",titular="", lista_alumnos=[]):
        self.nombre = nombre
        self.titular = titular
        self.lista_alumnos = lista_alumnos

    def agregarAlumno(self):
        print("\t\t---Agregar alumno ---\n\n")
        try:
            nuevo = alumno.buscar_alumno()
            self.lista_alumnos.append(nuevo)
            print("nuevo alumno agregado a la materia")
            print(self.lista_alumnos)
        except:
            print("error, no se agregó el alumno")

    def eliminarAlumno(self):
        print("\t\t---Eliminar alumno ---\n\n")
        eliminar = alumno.buscar_alumno()
        for alum in self.lista_alumnos:
            try:
                if eliminar == alum:
                    self.lista_alumnos.remove(alum)
                    print(f"Alumno con matricula: {alum.matricula} ha sido eliminado.")
            except:
                print("No se encontró el alumno a eliminar")

    def listarAlumnos(self):
        print("\t\t---Listar alumnos ---\n\n")
        for alum in self.lista_alumnos:
            print("Matricula: ", alum.matricula, "\nNombre: ", alum.nombre, "\nfecha de nacimiento: ",
                  alum.fecha_nacimiento, "\nFecha de ingreso: ", alum.fecha_ingreso, "\nCiudad de origen: ",
                  alum.ciudad, "\nGenero: ", alum.genero)



