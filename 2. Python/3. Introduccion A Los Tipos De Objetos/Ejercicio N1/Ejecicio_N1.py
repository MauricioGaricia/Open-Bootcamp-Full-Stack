print("Calcular Tu Indice De Masa Corporal ")
Nombre = input("Escribe tu Nombre : ")
Peso = int(input(f"{Nombre}, Cual Es Tu peso ? : "))
Estatura = float(input(f"{Nombre}, Cual Es Tu Estatura En Metros? : "))

def CalIMC(Peso, Estatura):
    IMC = Peso  /(Estatura**2)
    return IMC
print(f"{Nombre}, tu Índice de Masa Corporal es: {CalIMC(Peso, Estatura):.2f}")