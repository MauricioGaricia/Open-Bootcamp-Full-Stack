Paises_Digitados = input("Introduce Una Lista De Países Separados Por Comas: ")
Paises_Digitados = Paises_Digitados.upper()
Paises = [Pais.strip() for Pais in Paises_Digitados.split(", ")]
Paises_Final = list(set(Paises))
Paises_Final.sort()
print(", ".join(Paises_Final))
