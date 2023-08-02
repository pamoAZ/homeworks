#!/usr/bin/env python
# coding: utf-8

# 1) Abrir el archivo "Emisiones_CO2.csv" y cargar sus datos en un diccionario.

# In[60]:


import os
archivo = open('C:/Users/HP/Desktop/Ciencia De Datos/Clases/Clase 2/Emisiones_CO2.csv', 'r')


# In[43]:


archivo


# In[61]:


dicc_emisiones = {  'cod_pais' : [],
                    'nom_pais' : [],
                    'region' : [],
                    'anio' : [],
                    'co2' : [],
                    'co2_percapita' : []}


# Ejemplo de como utilizar Next()

# In[45]:


# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Crear un iterador a partir de la lista
iterador_numeros = iter(numeros)

# Obtener el primer elemento del iterador usando next()
primer_elemento = next(iterador_numeros)
print(primer_elemento)  # Salida: 1

# Obtener el siguiente elemento del iterador usando next()
segundo_elemento = next(iterador_numeros)
print(segundo_elemento)  # Salida: 2

# Obtener el siguiente elemento del iterador usando next()
tercer_elemento = next(iterador_numeros)
print(tercer_elemento)  # Salida: 3

# Obtener el siguiente elemento del iterador usando next()
cuarto_elemento = next(iterador_numeros)
print(cuarto_elemento)  # Salida: 4

# Obtener el siguiente elemento del iterador usando next()
quinto_elemento = next(iterador_numeros)
print(quinto_elemento)  # Salida: 5

# Intentar obtener otro elemento del iterador (que ya se ha agotado)
# Generará la excepción StopIteration
elemento_extra = next(iterador_numeros)


# In[46]:


"""strip(): Esta función se utiliza para
eliminar espacios en blanco (espacios,
tabulaciones y saltos de línea) al principio
y al final de una cadena"""
texto = "   Hola, esto es un ejemplo.    "
texto_limpio = texto.strip()
print(texto_limpio)


# In[47]:


"""split(): Esta función divide una cadena en subcadenas utilizando un separador específico y 
devuelve una lista de las subcadenas resultantes."""
frase = "Hola,a,todos"
palabras = frase.split(",")
print(palabras)  # Salida: ["Hola", "a", "todos"]


# In[62]:


next(archivo)
for linea in archivo:
    linea = linea.strip()
    campos = linea.split('|')
    dicc_emisiones['cod_pais'].append(campos[0])
    dicc_emisiones['nom_pais'].append(campos[1])
    dicc_emisiones['region'].append(campos[2])
    dicc_emisiones['anio'].append(campos[3])
    dicc_emisiones['co2'].append(campos[4])
    dicc_emisiones['co2_percapita'].append(campos[5])


# In[49]:


dicc_emisiones


# # 2) 
# #### a) ¿Cuántas variables hay?
# #### b) ¿Qué tipos de datos usar para cada una?
# #### c) ¿Qué tipo de variables son?
# #### d) ¿Hay valores faltantes?
# #### e) ¿Cuál es el total de emisiones de CO2 para 'América Latina y Caribe' en el año 2010?

# In[50]:


## a)
llaves = dicc_emisiones.keys()
llaves = list(llaves)
llaves
print('Hay ',len(llaves), 'variables', "que son:", llaves )


# In[31]:


## b) para las columnas de CO2 y CO2 percapita es necesario hacer ETL ó Data wrangling. Así
## pasamos de tipo de dato str a float.
## el resto str


# In[51]:


## c)
## Tipos de variables:
print('Los tipos de variable son:\n Para cod_pais: categórica')
print('Para nom_pais: cualitativo categórica')
print('Para region: cualitativo categórica')
print('Para nom_pais: cualitativo categórica')
print('Para anio: cualitativo ordinal')
print('Para co2: cuantitativo continuo')
print('Para co2_percápita: cuantitativo continuo')


# In[52]:


## d) 
nulo = 0
for indice, elemento in enumerate(dicc_emisiones['cod_pais']):
    if elemento == None:
        nulo += 1
print('La cantidad de nulos para cod pais es: ',nulo)


# In[53]:


## d) 
nulo = 0
for indice, elemento in enumerate(dicc_emisiones['nom_pais']):
    if elemento == None:
        nulo += 1
print('La cantidad de nulos para nom pais es: ',nulo)


# In[54]:


## d) 
nulo = 0
for indice, elemento in enumerate(dicc_emisiones['region']):
    if elemento == None:
        nulo += 1
print('La cantidad de nulos para region es: ',nulo)


# In[55]:


## d) 
nulo = 0
for indice, elemento in enumerate(dicc_emisiones['anio']):
    if elemento == None:
        nulo += 1
print('La cantidad de nulos para anio es: ',nulo)


# In[63]:


## ETL
for indice, elemento in enumerate(dicc_emisiones['co2_percapita']):
    elemento = elemento.replace('.','')
    elemento = elemento.replace(',','.')
    if (elemento != ''):
        elemento = float(elemento)
    else:
        elemento = None
    dicc_emisiones['co2_percapita'][indice] = elemento


# In[ ]:


## d) 
nulo = 0
for indice, elemento in enumerate(dicc_emisiones['co2_percapita']):
    if elemento == None:
        nulo += 1
print('La cantidad de nulos para co2_percapita es: ',nulo)


# In[64]:


type(dicc_emisiones['co2'][100])


# In[ ]:


## e)
import enum


filtro_region = 'América Latina y Caribe'
filtro_anio = '2010'
emisiones = 0
for indice, elemento in enumerate(dicc_emisiones['region']):
    if (dicc_emisiones['region'][indice] == filtro_region):
        if (dicc_emisiones['anio'][indice] == filtro_anio):
            if (dicc_emisiones['co2'][indice] != None):
                emisiones += dicc_emisiones['co2'][indice]
print('las emisiones en: ', filtro_region, 'en ', filtro_anio, 'fueron de ',emisiones, 'kt')

