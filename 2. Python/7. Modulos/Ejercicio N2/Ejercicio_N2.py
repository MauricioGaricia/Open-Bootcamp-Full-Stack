import time as T

Hora_Actual = T.localtime().tm_hour

if Hora_Actual >= 19:  
    print("¡Hora de irse a casa!")
else:
    Hora_Salida = 19   
    Minutos_Restantes = (Hora_Salida - Hora_Actual) * 60 - T.localtime().tm_min
    Horas_Restantes = Minutos_Restantes / 60
    print(f"Aún quedan {Horas_Restantes:.1f} horas de trabajo.")
