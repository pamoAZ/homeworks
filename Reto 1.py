#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

# Generar el conjunto de datos de temperaturas para el año completo (365 días)
temperatura_min = -5
temperatura_max = 30
dias_medicion = 360
temperaturas = np.random.uniform(temperatura_min, temperatura_max, dias_medicion)

# 1. Calcular la temperatura media, mínima y máxima en la ciudad durante el año.
temperatura_media = np.mean(temperaturas)
temperatura_minima = np.min(temperaturas)
temperatura_maxima = np.max(temperaturas)

# 2. Encontrar el día más caliente y el día más frío del año.
dia_mas_caliente = np.argmax(temperaturas) + 1 # se le suma uno para que de con el dia 
dia_mas_frio = np.argmin(temperaturas) + 1

# 3. Calcular la temperatura media de cada mes (suponiendo 30 días por mes).
# el -1 es para que divida los datos en iguales cantidades de filas y 30 para
# que cada columna tenga 30 datos 
temperaturas_por_mes = temperaturas.reshape(12, 30)  # Reshape en una matriz de meses y días
temperatura_media_por_mes = np.mean(temperaturas_por_mes, axis=1)
#axis es para que determine el promedio (mean) para cada columna 

# 4. Encontrar la mayor diferencia entre la temperatura promedio de dos meses consecutivos.
diferencias_entre_meses = np.diff(temperatura_media_por_mes)
print("el tipo de dato de diferencias entre meses es: ", type(diferencias_entre_meses))
mayor_diferencia_entre_meses = np.max(np.abs(diferencias_entre_meses))

# 5. Encontrar todos los días del año con temperaturas inferiores a 0 grados Celsius (días de helada).
dias_de_helada = np.where(temperaturas < 0)[0] #[0] es para que nos devuelva una lista no una tupla 
mes_con_mas_dias_de_helada = np.argmax(np.bincount(dias_de_helada // 30)) + 1

# 6. Calcular cuántos días del año tuvieron una temperatura dentro de la "zona de confort" (entre 18 y 24 grados Celsius).
dias_zona_confort = np.sum((temperaturas >= 18) & (temperaturas <= 24))

# Imprimir los resultados
print("Temperatura media del año:", temperatura_media)
print("Temperatura mínima del año:", temperatura_minima)
print("Temperatura máxima del año:", temperatura_maxima)
print("Día más caliente del año:", dia_mas_caliente)
print("Día más frío del año:", dia_mas_frio)
print("Temperatura media de cada mes:", temperatura_media_por_mes)
print("Mayor diferencia entre temperatura promedio de dos meses consecutivos:", mayor_diferencia_entre_meses)
print("Días de helada en el año:", len(dias_de_helada))
print("Mes con mayor cantidad de días de helada:", mes_con_mas_dias_de_helada)
print("Días en la zona de confort:", dias_zona_confort)


# In[ ]:




