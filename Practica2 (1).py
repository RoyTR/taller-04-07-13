def Obtener_Promedio_Puntanjes(puntajes):
    Calculo_Promedio = 0
    Suma_Montos = 0
    
    for puntaje in range(0, len(puntajes), 1):
        Suma_Montos += int(puntajes[puntaje])
        
    Calculo_Promedio = Suma_Montos / len(puntajes)
    return Calculo_Promedio

def Obtener_Posicion_Puntanje_Alto(puntajes):
    Calculo_Puntaje = 0
    Posicion = 0

    for puntaje in range(0, len(puntajes), 1):
        if int(puntajes[puntaje]) > Calculo_Puntaje:
            Calculo_Puntaje = int(puntajes[puntaje])
            Posicion = puntaje
        
    return Posicion

def Obtener_Numero_Trabajadores_Superior_Promedio(puntajes):
    Promedio = Obtener_Promedio_Puntanjes(puntajes)
    Numero_Trabajadores = 0

    for puntaje in range(0, len(puntajes), 1):
        if int(puntajes[puntaje]) > Promedio:
            Numero_Trabajadores += 1

    return Numero_Trabajadores


# Arreglos
trabajadores = ["Ana Torres", "Luis Ramos", "Carmen Díaz", "Pedro Flores", "Rosa Medina"]
puntajes = [78, 85, 90, 70, 88]

# Pregunta A
Promedio = Obtener_Promedio_Puntanjes(puntajes)
print("El promedio de los puntajes es:", Promedio)

# Pregunta B
Posicion = Obtener_Posicion_Puntanje_Alto(puntajes)
print("El puntaje más alto fue obtenido por:", trabajadores[Posicion], "que hizo", puntajes[Posicion], "puntos.")

# Pregunta C
Numero_Trabajadores_Mayor_Promedio = Obtener_Numero_Trabajadores_Superior_Promedio(puntajes)
print("El número de trabajadores que obtuvo puntajes superiores al promedio es:", Numero_Trabajadores_Mayor_Promedio)