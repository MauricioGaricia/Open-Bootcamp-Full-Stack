from functools import reduce

def Suma_Lista_Pasada(lst):
    Lista_Pasada = filter(lambda x: x % 2 != 0, lst)
    Suma_Pasada = reduce(lambda x, y: x + y, Lista_Pasada)
    return Suma_Pasada

Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Resultado = Suma_Lista_Pasada(Lista)

print("La Lista Predeterminada Es : ", Lista)
print("El Resultado De La Suma Es : ", Resultado)
