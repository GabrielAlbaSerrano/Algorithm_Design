#!/usr/bin/env python3
# -*- coding: utf-8 -*-



'''

    PRÁCTICA 1 (PARTE 2): ANÁLISIS DE LA EFICIENCIA DE ALGORITMOS DE 
                          ORDENACIÓN Y DE BÚSQUEDA EN PYTHON

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1 / U2

    APELLIDOS: 
    NOMBRE:    

'''



import matplotlib.pyplot as plt
import numpy as np
import timeit
import time
import random



# ALGORITMOS DE ORDENACION (SELECCIÓN E INSERCIÓN)



'''

EJERCICIO 1: Programa en Python los algoritmos de ordenación por selección y
ordenación por inserción estudiados en las clases de teoría. Usa el código 
visto en las sesiones de laboratorio para visualizar los tiempos de ejecución
de estos dos programas, para determinar cuál es más eficiente en la práctica, 
así como para visualizar la función de coste que define, para cada algoritmo, 
su orden de complejidad.

'''

# No necesitamos la función intercambiar para el algoritmo de ordenación por
# selección ya que en Python podemos realizar asignaciones simultáneas

def ord_seleccion(v): # Ordenación por selección (visto en clase)
    N = len(v)
    for i in range(N):
        pmin = i
        for j in range(i+1,N):
            if v[j] < v[pmin]:
                pmin = j
        v[i],v[pmin] = v[pmin],v[i]
    return v
        

def ord_insercion(v): # Ordenación por inserción (visto en clase)
    N = len(v)
    for i in range(N):
        elem = v[i]
        j = i-1
        while j >= 0 and elem < v[j]:
            v[j+1] = v[j]
            j = j-1
        v[j+1] = elem
    return v


def main1():
    
    MAX_LEN = 1000  # Maximum length of input list

    # Initialise results containers
    
    lengths_sort_sel  = []
    times_sort_sel    = []

    lengths_sort_ins  = []
    times_sort_ins    = []

    for length in range(0, MAX_LEN, 5) :
        
        # Generate random lists
        
        v  = [random.randint(-99, 99) for _ in range(length)]
        w = []
        for elem in v :
            w.append(elem)

        # Time execution (algoritmo de ordenacion por selección)
        
        start = time.perf_counter()
        ord_seleccion(v)
        end = time.perf_counter()

        # Store results
        
        lengths_sort_sel.append(length)
        times_sort_sel.append(end - start)

        # Time execution (algoritmo de ordenacion por inserción)
        
        start = time.perf_counter()
        ord_insercion(w)
        end = time.perf_counter()

        # Store results
        
        lengths_sort_ins.append(length)
        times_sort_ins.append(end - start)
        
        

    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos de ordenacion - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_sort_sel, times_sort_sel, label="ord_seleccion()")
    plt.plot(lengths_sort_ins, times_sort_ins, label="ord_insercion()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    # Polynomial fir for ord_insercion
    
    ns = np.linspace(1, 3000, 100, dtype = int)
    ts = [timeit.timeit('ord_insercion(lst)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]

    plt.plot(ns, ts, 'or')

    degree = 5
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')
    
    """ Polynomial fir for ord_seleccion
    
    ns = np.linspace(1, 3000, 100, dtype = int)
    ts = [timeit.timeit('ord_seleccion(lst)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]

    plt.plot(ns, ts, 'og')

    degree = 5
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')
    """


# ALGORITMOS DE ORDENACION (QUICKSORT Y MERGESORT)


    
'''

EJERCICIO 2: Programa en Python los algoritmos de ordenación "quicksort" 
y "mergesort", y compara su eficiencia con los algoritmos de ordenación 
anteriores.

'''   

def particion(v): # Función auxiliar del algoritmo quickSort
    # Sustituimos en el pseudódigo: c = 0 , f = N-1
    N = len(v)
    piv = v[0]
    i = 1
    d = N-1
    while i != d+1:
        while i <= d and v[i] <= piv:
            i = i+1
        while i <= d and v[d] >= piv:
            d = d-1
        if i < d:
            v[i], v[d] = v[d], v[i]
            i = i+1
            d = d-1
    v[0],v[d] = v[d],v[0]
    p = d
    return p
    

def quickSort(v): # Ordenación por el método quicksort
    # En el pseudocódigo el algoritmo quickSort se inicializa con
    # inicio = 0 ; fin = N-1
    # En la implementación en Python vamos realizar directamente la 
    # inicialización, es decir, no vamos a tener como parámetros de
    # entrada inicio y fin
    N = len(v)
    if N > 1:
        p = particion(v)
        v[:p] = quickSort(v[:p])
        v[p+1:] = quickSort(v[p+1:])
    return v


def mezclar(v): # Función auxiliar del algoritmo mergeSort
    # Sustituimos en el pseudódigo: c = 0 , f = N-1
    N = len(v)
    m = N//2
    w = [0]*N
    i = 0
    j = m
    k = 0
    while i < m and j < N:
        if v[i] <= v[j]:
            w[k] = v[i]
            i = i+1
        else:
            w[k] = v[j]
            j = j+1
        k = k+1
    if i >= m:
        for l in range(j,N): 
            w[k] = v[l]
            k = k+1
    else:
        for l in range(i,m): 
            w[k] = v[l]
            k = k+1
    return w
    """ Según el pseudocódigo el algoritmo terminaría así,
        pero lo he adaptado para simplificarlo
    for l in range(N):
        v[l] = w[l]
    return v
    """
    

def mergeSort(myList): # Ordenación por el método mergesort
    # En el pseudocódigo el algoritmo quickSort se se inicializa con
    # inicio = 0 ; fin = N-1
    # En la implementación en Python vamos realizar directamente la 
    # inicialización, es decir, no vamos a tener como parámetros de
    # entrada inicio y fin
    N = len(myList)
    if N > 1:
        m = N//2
        myList[:m] = mergeSort(myList[:m])
        myList[m:] = mergeSort(myList[m:])
        myList = mezclar(myList)
    return myList


def main2():
    
    MAX_LEN = 1000  # Maximum length of input list
    
    # Initialise results containers
    
    lengths_sort_sel = []
    times_sort_sel   = []

    lengths_sort_ins = []
    times_sort_ins   = []
    
    lengths_quick = []
    times_quick   = []
    
    lengths_merge = []
    times_merge   = []

    for length in range(0, MAX_LEN, 100) :
        
        # Generate random list
        
        v = [random.randint(-99, 99) for _ in range(length)]
        v1 = []
        v2 = []
        v3 = []
        for elem in v :
            v1.append(elem)
            v2.append(elem)
            v3.append(elem)

        # Time execution (algoritmo de ordenacion por selección)
        
        start = time.perf_counter()
        ord_seleccion(v)
        end = time.perf_counter()

        # Store results
        
        lengths_sort_sel.append(length)
        times_sort_sel.append(end - start)

        # Time execution (algoritmo de ordenacion por inserción)
        
        start = time.perf_counter()
        ord_insercion(v1)
        end = time.perf_counter()

        # Store results
        
        lengths_sort_ins.append(length)
        times_sort_ins.append(end - start)

        # Time execution (algoritmo de ordenacion quicksort)

        start = time.perf_counter()
        quickSort(v2)
        end = time.perf_counter()
        
        # Store results
        
        lengths_quick.append(length)
        times_quick.append(end - start)
        
        # Time execution (algoritmo de ordenacion mergesort)

        start = time.perf_counter()
        mergeSort(v3)
        end = time.perf_counter()
        
        # Store results
        
        lengths_merge.append(length)
        times_merge.append(end - start)

        

    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos de ordenacion - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_sort_sel, times_sort_sel, label="ord_seleccion()")
    plt.plot(lengths_sort_ins, times_sort_ins, label="ord_insercion()")
    plt.plot(lengths_merge, times_merge, label="mergeSort()")
    plt.plot(lengths_quick, times_quick, label="quickSort()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    # Se observa una reducción de la complejidad con mergeSort y quickSort,
    # (especialmente con quickSort) respecto a ord_seleccion y ord_insercion


# ALGORITMOS DE BÚSQUEDA (SECUENCIAL Y BINARIA)



'''

EJERCICIO 3: Programa en Python los algoritmos de búsqueda secuencial y 
búsqueda binaria, y compara su eficiencia. Visualiza sus ordenes de 
complejidad.

'''  


def busq_sec(lst, x): # Búsqueda secuencial
    i = 0
    while i < len(lst) and lst[i] != x:
        i += 1
    if i == len(lst):
        return -1
    else:
        return i


def busq_bin(lst, x): # Búsqueda binaria (o dicotómica)
    c = 0
    f = len(lst)-1
    return gbusq_bin(lst,x,c,f)

# Realizamos una inmersión de parámetros

def gbusq_bin(lst, x, c, f):
    if c > f:
        return -1
    else:
        m = (c+f)//2
        if x < lst[m]:
            return gbusq_bin(lst,x,c,m-1)
        elif x == lst[m]:
            return m
        else:
            return gbusq_bin(lst,x,m+1,f)


def main3():
    
    MAX_LEN = 1000  # Maximum length of input list
    
    # Initialise results containers
    
    lengths_busq_sec = []
    times_busq_sec   = []

    lengths_busq_bin = []
    times_busq_bin   = []

    for length in range(0, MAX_LEN, 10) :
        
        # Generate random list
        
        v = [random.randint(-99, 99) for _ in range(length)]
        x = random.randint(-99, 99)
        
        # Sort the list
        
        ord_insercion(v)

        # Time execution (algoritmo de búsqueda secuencial)
        
        start = time.perf_counter()
        busq_sec(v, x)
        end = time.perf_counter()

        # Store results
        
        lengths_busq_sec.append(length)
        times_busq_sec.append(end - start)

        # Time execution (algoritmo de búsqueda binaria)
        
        start = time.perf_counter()
        busq_bin(v, x)
        end = time.perf_counter()

        # Store results
        
        lengths_busq_bin.append(length)
        times_busq_bin.append(end - start)



    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos de búsqueda - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_busq_sec, times_busq_sec, label="busq_sec()")
    plt.plot(lengths_busq_bin, times_busq_bin, label="busq_bin()")
    plt.legend()
    plt.tight_layout()
    plt.show()

    ns = np.linspace(1, 10000, 100, dtype = int) 
    # ts = [timeit.timeit('busq_sec(lst, random.randint(lst[0], lst[len(lst)-1]))',
    #                 setup='lst=list(range({}))'.format(n),
    #                 globals=globals(),
    #                 number=1000)
    #       for n in ns]
    ts = [timeit.timeit('busq_bin(lst, random.randint(lst[0], lst[len(lst)-1]))',
                    setup='lst=list(range({}))'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]
    

    plt.plot(ns, ts, 'or')

    degree = 10
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')

    # Se observa que el algoritmo de búsqueda binaria tiene menor orden de
    # complejidad que el algoritmo de búsqueda secuencial