#Entrada
fabricaNorte = [120, 135, 140, 128, 150]
fabricaSur = [110, 125, 130, 120, 145]

#Funcion para calcular la Mayor Producción Registrada
def mayor_produccion(arreglo):
    mayor = arreglo[0]
    
    for valor in arreglo:
        if valor > mayor:
            mayor = valor
    return mayor


#Función que devuelve la producción promedio
def promedio_produccion(arreglo):
    suma = 0
    
    for valor in arreglo:
        suma += valor
        
    promedio = suma / len(arreglo)
    return promedio


#Funcion para detectar diferencias de produccion entre fabricas
def diferencia_produccion(norte, sur):
    diferencias = []
    
    for i in range(len(norte)):
        diferencias.append(norte[i] - sur[i])
        
    return diferencias


#Salida
print("Mayor producción Norte:", mayor_produccion(fabricaNorte))
print("Mayor producción Sur:", mayor_produccion(fabricaSur))

print("Promedio Norte:", promedio_produccion(fabricaNorte))
print("Promedio Sur:", promedio_produccion(fabricaSur))

print("Diferencias:", diferencia_produccion(fabricaNorte, fabricaSur))