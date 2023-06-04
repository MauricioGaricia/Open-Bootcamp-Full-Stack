import pickle

class Vehiculo:
    def __init__(self, marca, modelo, anyo, color):
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo
        self.color = color
    
    def __str__(self):
        return f"Vehiculo {self.marca} {self.modelo} del año {self.anyo} y color {self.color}"
    
mi_coche = Vehiculo("Toyota", "Prado", 2023, "Negra")


with open("mi_coche.pickle", "wb") as archivo:
    pickle.dump(mi_coche, archivo)


with open("mi_coche.pickle", "rb") as archivo:
    mi_coche_cargado = pickle.load(archivo)

print(mi_coche_cargado)
