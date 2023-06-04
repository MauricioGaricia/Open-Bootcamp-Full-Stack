class Vehiculo(): 
    Color = ''
    Ruedas = 0
    Puertas = 0
    def __init__(self, Color, Ruedas, Puertas):
        self.color = Color
        self.ruedas = Ruedas
        self.puertas = Puertas


class Coche(Vehiculo):
    Velocidad = 0
    Cilindrada = 0
    def __init__(self, Velocidad, Cilindrada, Color, Ruedas, Puertas ):
        super().__init__(Color, Ruedas, Puertas)
        self.velocidad = Velocidad
        self.cilindrada = Cilindrada

c = Coche(474.8, 12200, 'Negro Mate', 4, 3)
print(
    "Color Es : ", c.color, '\n',
    "Velocidad Máxima: Es", c.velocidad, '\n',
    "Cilindrada Del Vehiculo Es : ", c.cilindrada, '\n',
    "Cantidad De Ruedas Del Vehiculo Es : ", c.ruedas, '\n',
    "Cantidad De Puertas Del Vehiculo Es : ", c.puertas
    )