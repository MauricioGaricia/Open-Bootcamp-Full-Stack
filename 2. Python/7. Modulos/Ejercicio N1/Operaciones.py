def Sumar(Numero_1, Numero_2):
    return Numero_1 + Numero_2

def Restar(Numero_1, Numero_2):
    return Numero_1 - Numero_2

def Multiplicar(Numero_1, Numero_2):
    return Numero_1 * Numero_2

def Dividir(Numero_1, Numero_2):
    if Numero_2 == 0:
        print("No se puede dividir entre cero")
        return
    else:
        return Numero_1 / Numero_2
