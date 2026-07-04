"""
Una empresa registró la producción diaria de dos fábricas durante 5 días:



fabricaNorte = [120, 135, 140, 128, 150]

fabricaSur = [110, 125, 130, 120, 145]



Se solicita lo siguiente:



a. Dado un arreglo de producción, desarrollar una función que devuelva la mayor producción registrada. (4 puntos)

b. Dado un arreglo de producción, desarrollar una función que devuelva la producción promedio. (3 puntos)

c. Dado los dos arreglos de producción, desarrollar una función que devuelva un arreglo con las diferencias de producción entre la fábrica Norte y la fábrica Sur por cada día. (3 puntos)
"""


fabricaNorte = [120, 135, 140, 128, 150]

def pregunta_a():
    produccionNorte = max(fabricaNorte)
    produccionSur = max(fabricaSur)
    if produccionNorte > produccionSur:
        print(f"La mayor producción fue en la fábrica del Norte con {produccionNorte}")
    else:
        print(f"hola mundo {produccionSur}")
def pregunta_b():
    acumuladoNorte = 0
    for i in fabricaNorte:
        acumuladoNorte += i
        i++
    
    
    acumuladoSur = 0
    for i in fabricaSur:
        acumuladoSur += i
    promedioProduccionSur = acumuladoSur / len(fabricaSur)
    
    print(f"El promedio del Norte es {promedioProduccionNorte}")
    print(f"El promedio del Sur es {promedioProduccionSur}")

def pregunta_c():
    diferencia = []
    for i in range(len(fabricaNorte)):
        diferencia.append(fabricaNorte[i] - fabricaSur[i])
    resultado = sum(diferencia) / len(diferencia)
    print(f"Promedio de diferencias: {resultado}")
    print(f"Diferencias día a día: {diferencia}")

pregunta_a()
pregunta_b()
pregunta_c()
