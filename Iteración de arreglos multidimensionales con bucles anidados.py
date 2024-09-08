### uea ###
### Juan Gabriel Zurita Manobanda ###

# se crea 2 matrices de dos ciudades 7 dias por dos semanas
temperatura = [
    [  # SACHA
        [32, 29, 28, 27, 34, 28, 30],  # Semana 1
        [30, 28, 29, 34, 33, 32, 31],  # Semana 2
    ],
    [  # COCA
        [28, 27, 29, 30, 32, 25, 25],  # Semana 1
        [28, 30, 27, 28, 29, 27, 29],  # Semana 2
    ]
]

ciudades = ["SACHA", "COCA"]
semanas = ["Semana 1", "Semana 2"]

# Se utulizara bucles  animados para calcular el promedio por ciudad y semana
for i, ciudad in enumerate(ciudades):
    for j, semana in enumerate(semanas):
        temperaturaI = 0    ## LA TEMPERATURA INICIAL LA MARCAMOS EN 0
        for dia in range(7):  # EL RANDO 7 días en una semana
            temperaturaI += temperatura [i][j][dia]

        promedio = temperaturaI / 7 ## SACAMOS EL PROMEDIO
        ## imprimimos los promedios
        print(f"Promedio de temperaturas para {ciudad} en {semana}: {promedio:.2f}°C")
