from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"#None

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, *lista):
        lista1=list(lista)
        lista1.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista1

    def __str__(self):
        return "Grupo de estudiantes: "+self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
