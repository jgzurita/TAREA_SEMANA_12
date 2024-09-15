### uea ###
### Juan Gabriel Zurita Manobanda ###

# Se aumenta una ciudad nueva y 2 semanas extras que se monitoriaran

temperatura = [
    [  # SACHA
        [32, 29, 28, 27, 34, 28, 30],  # Semana 1
        [30, 28, 29, 34, 33, 32, 31],  # Semana 2
        [31, 29, 30, 32, 33, 34, 28],  # Semana 3
        [32, 30, 31, 28, 35, 28, 27],  # Semana 4
    ],
    [  # COCA
        [28, 27, 29, 30, 32, 25, 25],  # Semana 1
        [28, 30, 27, 28, 29, 27, 29],  # Semana 2
        [27, 29, 30, 31, 28, 26, 25],  # Semana 3
        [29, 31, 32, 30, 33, 28, 27],  # Semana 4
    ],
    [  # TENA
        [20, 18, 19, 21, 22, 20, 19],  # Semana 1
        [21, 19, 20, 22, 23, 21, 20],  # Semana 2
        [22, 20, 21, 23, 24, 22, 21],  # Semana 3
        [23, 21, 22, 24, 25, 23, 22],  # Semana 4
    ]
]

ciudades = ["SACHA", "COCA", "TENA"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]

# Utilizamos bucles para calcular el promedio por ciudad y semana
for i, ciudad in enumerate(ciudades):
    for j, semana in enumerate(semanas):
        temperaturaI = 0  # Temperatura inicial en 0
        for dia in range(7):  # Rango de 7 días en una semana
            temperaturaI += temperatura[i][j][dia]

        promedio = temperaturaI / 7  # Calculamos el promedio
        # Imprimimos los promedios
        print(f"Promedio de temperaturas para {ciudad} en {semana}: {promedio:.2f}°C")
