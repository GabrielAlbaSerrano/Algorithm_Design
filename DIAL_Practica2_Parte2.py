#!/usr/bin/env python3
# -*- coding: utf-8 -*-



'''

    PRÁCTICA 2 (PARTE 2): DISEÑO DE ALGORITMOS ITERATIVOS EFICIENTES EN PYTHON

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



def raiz_ent1(n):
    r = 0 
    while n >= (r + 1) * (r + 1):
        r = r + 1
    return r


def raiz_ent2(n):
    r = n
    while r * r > n:
         r = r - 1
    return r


def raiz_ent3(n):
    r = 0
    y = n + 1
    
    while y != r + 1:
        h = (r + y) // 2
        if h * h <= n:
            r = h
        else:
            y = h 
            
    return r

def raiz_ent4(n, a, b):
    r = 0
    if b == a + 1:
         r = a
    elif b > a + 1:
        m = (a + b) // 2

        if m*m <= n: 
             r = raiz_ent4(n, m, b)
        else:
             r = raiz_ent4(n, a, m)
    
    return r




def main1():
    
    MAX_LEN = 135  # Maximum length of input list.

    # Initialise results containers:
    
    lengths_raiz_ent1  = []
    times_raiz_ent1    = []
    
    lengths_raiz_ent2  = []
    times_raiz_ent2    = []
    
    lengths_raiz_ent3  = []
    times_raiz_ent3    = []
    
    lengths_raiz_ent4  = []
    times_raiz_ent4    = []
    

    for length in range(0, MAX_LEN, 1):
        
        # Time execution (raiz_ent1):
        
        start = time.perf_counter()
        raiz_ent1(length)
        end = time.perf_counter()

        # Store results (raiz_ent1):
        
        lengths_raiz_ent1.append(length)
        times_raiz_ent1.append(end - start)
        
        # Time execution (raiz_ent2):
        
        start = time.perf_counter()
        raiz_ent2(length)
        end = time.perf_counter()

        # Store results (raiz_ent2):
        
        lengths_raiz_ent2.append(length)
        times_raiz_ent2.append(end - start)
        
        # Time execution (raiz_ent3):
        
        start = time.perf_counter()
        raiz_ent3(length)
        end = time.perf_counter()

        # Store results (raiz_ent3):
        
        lengths_raiz_ent3.append(length)
        times_raiz_ent3.append(end - start)
        
        # Time execution (raiz_ent4):
        
        start = time.perf_counter()
        raiz_ent4(length,0,length)
        end = time.perf_counter()

        # Store results (raiz_ent4):
        
        lengths_raiz_ent4.append(length)
        times_raiz_ent4.append(end - start)
        
    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos raiz cuadrada entera - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    
    plt.plot(lengths_raiz_ent1, times_raiz_ent1, label="raiz_ent1()")
    plt.plot(lengths_raiz_ent2, times_raiz_ent2, label="raiz_ent2()")
    plt.plot(lengths_raiz_ent3, times_raiz_ent3, label="raiz_ent3()")
    plt.plot(lengths_raiz_ent4, times_raiz_ent4, label="raiz_ent4()")
    
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    print("\n")
    n = int(input("1.- raiz_ent1() | 2.- raiz_ent2() | 3.- raiz_ent3() | 4.- raiz_ent4 "))
    
    if n == 1 :
    
        ns = np.linspace(0, 1000, 100, dtype = int)
        ts = [timeit.timeit('raiz_ent1(n)',
                setup='n={}'.format(n),
                globals=globals(),
                number=1000)
              for n in ns]
    
        plt.plot(ns, ts, 'or')
    
        degree = 5
        coeffs = np.polyfit(ns, ts, degree)
        p = np.poly1d(coeffs)
        plt.plot(ns, [p(n) for n in ns], '-b')
        
    elif n == 2 :
    
        ns = np.linspace(0, 1000, 100, dtype = int)
        ts = [timeit.timeit('raiz_ent2(n)',
                setup='n={}'.format(n),
                globals=globals(),
                number=1000)
              for n in ns]
    
        plt.plot(ns, ts, 'or')
    
        degree = 5
        coeffs = np.polyfit(ns, ts, degree)
        p = np.poly1d(coeffs)
        plt.plot(ns, [p(n) for n in ns], '-b')
    
    elif n == 3 :
    
        ns = np.linspace(0, 1000, 100, dtype = int)
        ts = [timeit.timeit('raiz_ent3(n)',
                setup='n={}'.format(n),
                globals=globals(),
                number=1000)
              for n in ns]
    
        plt.plot(ns, ts, 'or')
    
        degree = 5
        coeffs = np.polyfit(ns, ts, degree)
        p = np.poly1d(coeffs)
        plt.plot(ns, [p(n) for n in ns], '-b')
        
    elif n == 4 :
        
        ns = np.linspace(0, 1000, 100, dtype = int)
        ts = [timeit.timeit('raiz_ent4(n,0,n)',
                setup='n={}'.format(n),
                globals=globals(),
                number=1000)
              for n in ns]
    
        plt.plot(ns, ts, 'or')
    
        degree = 5
        coeffs = np.polyfit(ns, ts, degree)
        p = np.poly1d(coeffs)
        plt.plot(ns, [p(n) for n in ns], '-b')




                
def potencia1(a, b):
    x = 0
    p = 1
    
    while not x == b:
        p = a * p
        x = x + 1
    
    return p



def potencia2(a, b):
    x = a
    y = b
    p = 1
    
    while y != 0:
        if y % 2 == 0:
            x = x * x
            y = y // 2
        else:
            p = p * x
            y = y - 1
    
    return p





def main2():
    
    MAX_LEN = 1000  # Maximum length of input list.

    # Initialise results containers:
    
    lengths_potencia1  = []
    times_potencia1    = []
    
    lengths_potencia2  = []
    times_potencia2    = []

    for length in range(0, MAX_LEN, 10):
        
        # Generate values:
    
        a = 2
        b = length

        # Time execution (potencia1):
        
        start = time.perf_counter()
        potencia1(a, b)
        end = time.perf_counter()

        # Store results (potencia1):
        
        lengths_potencia1.append(length)
        times_potencia1.append(end - start)

        # Time execution (potencia2):
        
        start = time.perf_counter()
        potencia2(a, b)
        end = time.perf_counter()

        # Store results (potencia2):
        
        lengths_potencia2.append(length)
        times_potencia2.append(end - start)
        
    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos potencia - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_potencia1, times_potencia1, label="potencia1()")
    plt.plot(lengths_potencia2, times_potencia2, label="potencia2()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    ns = np.linspace(0, 1000, 100, dtype = int)
    ts = [timeit.timeit('potencia2(2, len(lst))',
            setup='lst=list(range({})); random.shuffle(lst)'.format(n),
            globals=globals(),
            number=1000)
          for n in ns]

    plt.plot(ns, ts, 'or')

    degree = 5
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')





def log_ent(n, b):
    r = 0
    p = b
    
    while p <= n:
        p = p * b
        r = r + 1
    
    return r





def main3():
    
    MAX_LEN = 1300  # Maximum length of input list.

    # Initialise results containers:
    
    lengths_log_ent  = []
    times_log_ent    = []

    for length in range(0, MAX_LEN, 5):
        
        # Generate values:
    
        a = length
        b = 2

        # Time execution (log_ent):
        
        start = time.perf_counter()
        log_ent(a, b)
        end = time.perf_counter()

        # Store results (log_ent):
        
        lengths_log_ent.append(length)
        times_log_ent.append(end - start)
        
    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos logaritmo entero - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_log_ent, times_log_ent, label="log_ent()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    ns = np.linspace(0, 10000, 100, dtype = int)
    ts = [timeit.timeit('log_ent(len(lst), 2)',
            setup='lst=list(range({})); random.shuffle(lst)'.format(n),
            globals=globals(),
            number=1000)
          for n in ns]

    plt.plot(ns, ts, 'or')

    degree = 5
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')