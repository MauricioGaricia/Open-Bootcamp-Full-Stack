def Es_Bisiesto(año):
    if (año % 4 == 0) and (año % 100 != 0 or año % 400 == 0):
        return "Es Un Año Bisiesto"
    else:
        return "Este NO Es Un Año Bisiesto"

while True:
    Menu = ('''  
            Menu 
        1. Saber Si El Año es Bisiesto 
        2. Salir 
        Selecciona Una Opcion Entre : ''')
    
    opcion = input(Menu)
    
    match opcion:
        case "1":
            año = int(input("Digite El Año Que Desea Saber, Si Es Bisiesto o NO: "))
            print(Es_Bisiesto(año))
            
        case "2":
            print("Saliendo... ")
            break

        case _:
            print("Opción inválida. Por favor, intenta de nuevo.")
