class Alumno:
    def __init__(self):
        self.Nombre = input("Digita El Nombre Del Alumno : ")
        self.Nota = float(input("Digita La Nota Del Alumno: "))

    def evaluacion(self):
        if self.Nota >= 70:
            print(f"{self.Nombre}, Has aprobado, Felicidades!")
        else:
            print(f"{self.Nombre}, Has Reprobado, Repite el curso.")

alumno = Alumno()
print(f"El Nombre Del Estudiante : {alumno.Nombre}")
print(f"La Nota Del Estudiante : {alumno.Nota}")
alumno.evaluacion()