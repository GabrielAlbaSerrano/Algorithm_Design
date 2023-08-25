# -*- coding: utf-8 -*-
"""

    PRÁCTICA 3 (PARTE 2): DIVIDE Y VENCERÁS
    AUTORES: Joaquín Velarde Noval y Gabriel Alba Serrano

"""




import matplotlib.pyplot as plt
import numpy as np
import timeit
import time
import random


# Voy a implementar una solución del Ejercicio 1 de la Hoja 6 (Divide y Vencerás)

# Voy a definir una función auxiliar 'mediana_medianas(v,k)' que calcula el
# k-esimo menor elemento del vector v utilizando el método de Divide y Vencerás
# visto en clase

def mediana_medianas(v, k):
    n = len(v)

    # Caso base: si el vector tiene longitud <= 12, devuelve la mediana directamente
    if n <= 12:
        return sorted(v)[k - 1]

    # Divide el vector en grupos de tamaño 5
    grupos = [v[i:i + 5] for i in range(0, n, 5)]

    # Calcula las medianas de los grupos
    medianas = [sorted(grupo)[len(grupo) // 2] for grupo in grupos]

    # Llama recursivamente a la función para encontrar la mediana de las medianas
    mm = mediana_medianas(medianas, len(medianas) // 2 + 1)

    # Partición del vector original en dos subvectores:
    # uno con elementos menores a la mediana de las medianas
    # y otro con elementos mayores a la mediana de las medianas
    menores = [elem for elem in v if elem < mm]
    mayores = [elem for elem in v if elem > mm]

    if k <= len(menores):
        return mediana_medianas(menores, k)
    elif k > len(v) - len(mayores):
        return mediana_medianas(mayores, k - (len(v) - len(mayores)))
    else:
        return mm
    


def cercanos_mediana(v, k): # Función que calcula los k elementos más cercanos a la mediana
    n = len(v)
    d = []  # Lista para almacenar las distancias
    
    # Si k es igual a la longitud del vector, se devuelve el vector completo
    if k == n:
        return v  
    
    else:
        # Calculamos la mediana de las medianas
        m = mediana_medianas(v, (n+1) // 2)
        
        # Calculamos las distancias entre cada elemento y la mediana
        d = [abs(v[i] - m) for i in range(n)]

        # Definimos el k-ésimo menor valor de las distancias
        k_esimo = mediana_medianas(d, k)

        # Buscamos los índices de los elementos con distancias iguales al k-ésimo valor
        ind_iguales = [j for j in range(len(d)) if d[j] == k_esimo]

        # Buscamos los índices de los elementos con distancias menores al k-ésimo valor
        ind_menores = [j for j in range(len(d)) if d[j] < k_esimo]

        # Concatenamos los índices de los elementos seleccionados
        indices = ind_menores + ind_iguales
        
        # Obtenemos los elementos correspondientes a los índices seleccionados
        result = [v[j] for j in indices[:k]]

    return result


# Ahora vamos a analizar su complejidad:


MAX_LEN = 1000  # Maximum length of input list

# Initialise results containers

lengths = []
times = []


for length in range(5, MAX_LEN, 5) :
    
    # Generate random lists
    
    v  = [random.randint(-99, 99) for _ in range(length)]
    k = random.randint(1,length)

    # Time execution (algoritmo cercanos_mediana D&V)
    
    start = time.perf_counter()
    cercanos_mediana(v,k)
    end = time.perf_counter()

    # Store results (cercanos_mediana D&V)
    
    lengths.append(length)
    times.append(end - start)
    
 

# Plot results

plt.style.use("dark_background")
plt.figure().canvas.manager.set_window_title("Cercanos a la mediana - Time Complexity")
plt.xlabel("List Length")
plt.ylabel("Execution Time")
plt.plot(lengths, times, label="cercanos_mediana Divide&Venceras")
plt.legend()
plt.tight_layout()
plt.show()

# Polynomial fit

ns = np.linspace(1, 3000, 100, dtype=int)
ts = [timeit.timeit('cercanos_mediana(lst, k)',
                setup='lst = list(range({})); random.shuffle(lst); k = random.randint(1, {})'.format(n, n),
                globals=globals(),
                number=1000)
      for n in ns]

plt.plot(ns, ts, 'or')

degree = 5
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], '-b')
