#!/usr/bin/env python
# coding: utf-8

# 1) Crear una función capaz de convertir números enteros de base 10 a base 2. Debe recibir como parámetro el número a convertir<br>
# Consideraciones:<br> 
# a. Tratar de resolverlo sin usar la función format(nro,"b")<br>
# b. El pdf "conversion-de-decimal-a-binario.pdf" puede servir de ayuda.

# In[2]:


def aBinario(numero):
  
    if numero < 0:
        print('Debe ingresar un número mayor que cero')
        return None
    if numero == 0:
        return numero
    if type(numero) != int:
        print('Debe ingresar un número entero')
        return None
    else:
        ''' Creamos una lista vacia para ir guardando los valores '''
        lista_binaria = []
        ''' Definimos el primer binario del numero ingresado '''
        modulo = numero%2
        lista_binaria.append(modulo)
        ''' Definimos una lista vacia para los cocientes '''
        lista_cocientes = []
        cociente = numero // 2
        lista_cocientes.append(cociente)
        
        for i in lista_cocientes:
            if i == 1:
                break
            else:
                nuevo_cociente = i//2
                lista_cocientes.append(nuevo_cociente)
        ''' Ahora ya que tenemos la lista de cocientes, vamos a crear la lista binaria '''
        for i in lista_cocientes:
            
            if i == 1:
                lista_binaria.append(1)
            else:
                binario = i%2
                lista_binaria.append(binario)

        ''' Ahora chequeamos que el valor que hayamos introducido coincida con la
            lista binaria creada '''
        lista_binaria_invertida = lista_binaria[::-1]
        contador = len(lista_binaria)
        numero_entero = 0
        j = 0
        for i in lista_binaria_invertida:
            longitud_de_lista = len(lista_binaria)
            contador -= 1
            if i == 1:
                j = 2
                numero_entero += j**(contador)
            else:
                j = 0        
                    
        print('Lista de cocientes: \n')
        print (lista_cocientes)
        print('Lista de binarios: \n')
        print (lista_binaria[::-1])
        print('Valor calculado a partir de la lista binaria: \n')
        return(numero_entero)


# In[6]:


aBinario(4)


# 2) Convertir de decimal a binario las fracciones 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9. Luego analizar los resultados y observar qué particularidad se encuentra en los mismos. Se puede usar Python o una calculadora, lo importante es ver si hay algo que podemos notar...
# 
# Salida esperada:

# In[7]:


def fraccion_a_Binario(fraccion):
    if fraccion >= 1:
        print('Debe ingresar un valor menor a uno')
        return None
    if type(fraccion) != float:
        print('Debe ingresar un valor flotante')
        return None
    if fraccion == 0.0:
        return 0
    if fraccion < 0:
        print('El valor no puede ser negativo')
        return None
    else:
        # Creamos la variable binario en formato str
        binario = '0.'
        # Creamos la lista de multiplicados vacía
        lista_multiplicados = []
        # Multiplicamos el primer valor por 2 (porque así es el proceso)
        valor = fraccion * 2
        # Añadimos ese valor a la lista de multiplicados
        lista_multiplicados.append(valor)
        multiplo = 0
        contador = 0
        for i in lista_multiplicados:
            contador += 1
            if i == 1.0:
                break
            if i > 1.0:
                """Esta parte lo que hace es, cuando el valor es mayor
                    que 1.0, se le resta 1.0. Por ejemplo 1.25- 1.0, y al
                    resultado de eso se lo multiplica por 2. Es así como
                    armamos la lista de multiplicados. Luego esa lista es
                    la que se usa para determinar si va un uno o un cero"""
                multiplo = (i - 1.0)*2
                lista_multiplicados.append(multiplo)
            else:
                multiplo = i * 2
                lista_multiplicados.append(multiplo)
        print ('Valores mutiplicados')
        ''' Si los valores multiplicados son mayores a 1.0 el valor binario es 1
            caso contrario, el valor es 0'''
        print (lista_multiplicados)

        for i in lista_multiplicados:
            if i >= 1.0:
                binario +=  '1'
            if i < 1.0:
                binario += '0'
        print('\nValor decimal binario:')
        return binario


# In[8]:


fraccion_a_Binario(1/7)


# In[1]:


import os

# Obtenemos la ruta absoluta del directorio actual
ruta_actual = os.path.abspath("")

# Imprimimos la ruta absoluta
print("La dirección donde se está guardando el código de Python es:", ruta_actual)


# In[ ]:




