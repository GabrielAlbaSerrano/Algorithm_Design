

'''

    PRÁCTICA 1: ANÁLISIS DE LA EFICIENCIA DE ALGORITMOS (PYTHON)

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1

    APELLIDOS: Alba Serrano
    NOMBRE: Gabriel
        
'''



import matplotlib.pyplot as plt
import numpy as np
import timeit
import time
import random



# EJEMPLO: MÁXIMO COMÚN DIVISOR



def mcd_rec(a, b):
    
    if a > b :
        return mcd_rec(a - b, b)
    elif a == b :
        return a
    else :
        return mcd_rec(a, b - a)



def mcd_rec2(a, b):
    
    if b == 0 :
        return a
    else :
        return mcd_rec2(b, a % b)
    
    

def mcd_iter(a, b):
    
    a1 = a
    b1 = b
    
    while a1 != b1 :
        
        if a1 > b1 :
            a1 = a1 - b1
        else :
            b1 = b1 - a1
            
    return a1



def main():
    
    MAX_LEN = 500  # Maximum length of input list.

    # Initialise results containers:
    
    lengths_mcd_rec  = []
    times_mcd_rec    = []
    
    lengths_mcd_rec2 = []
    times_mcd_rec2   = []
    
    lengths_mcd_iter = []
    times_mcd_iter   = []
    

    for length in range(0, MAX_LEN, 10):
        
        # Generate random values:
        
        a = random.randint(length, 10*length)
        b = random.randint(length, 10*length)

        # Time execution (mcd_rec):
        
        start = time.perf_counter()
        mcd_rec(a, b)
        end = time.perf_counter()

        # Store results (mcd_rec):
        
        lengths_mcd_rec.append(length)
        times_mcd_rec.append(end - start)

        # Time execution (mcd_rec2):
        
        start = time.perf_counter()
        mcd_rec2(a, b)
        end = time.perf_counter()

        # Store results (mcd_rec2):
        
        lengths_mcd_rec2.append(length)
        times_mcd_rec2.append(end - start)
        
        # Time execution (mcd_iter):
        
        start = time.perf_counter()
        mcd_iter(a, b)
        end = time.perf_counter()

        # Store results (mcd_iter):
        
        lengths_mcd_iter.append(length)
        times_mcd_iter.append(end - start)
        
        
        
    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos de MCD - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_mcd_rec, times_mcd_rec, label="mcd_rec()")
    plt.plot(lengths_mcd_rec2, times_mcd_rec2, label="mcd_rec2()")
    plt.plot(lengths_mcd_iter, times_mcd_iter, label="mcd_iter()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    
    # Polynomial fit
    
    ns = np.linspace(1, 100000, 100, dtype = int)
    ts = [timeit.timeit('mcd_rec2(lst[0], lst[len(lst) - 1])',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]

    plt.plot(ns, ts, 'or')

    degree = 5
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')



'''

EJERCICIO: Programa en Python los algoritmos 'queHace1', 'queHace2' y 'queHace3'
que has programado anteriormente en C++. Usa el código anterior para visualizar 
los tiempos de ejecución de estos tres programas, para determinar cuál es más 
eficiente en la práctica, así como para visualizar la función de coste que 
define, para cada algoritmo, su orden de complejidad.

'''

def queHace1(v,N): # O(N**3)
    mejor = 0 # O(1)
    for i in range(0,N): # O(N**3)
        for j in range(i,N): # O(suma : i <= j <= N-1 : j-i+1) = O(N**2)
            suma = 0 # O(1)
            for k in range(i,j+1): # O(j-i+1)
                suma += v[k] # O(1)
            if suma > mejor: # O(1)
                mejor = suma
    return mejor

def queHace2(v,N): # O(N**2)
    mejor = 0 # O(1)
    for i in range(0,N): # O(suma : 0 <= i <= N-1 : N-i) = O(N**2)
        suma = 0 # O(1)
        for j in range(i,N): # O(N-i)
            suma += v[j] # O(1)
            if suma > mejor: # O(1)
                mejor = suma # O(1)
    return mejor

def queHace3(v,N): # O(N)
    r, s = v[0], v[0] # O(1)
    for i in range(1,N): # O(N-1-1) = O(N-2)
        s = max(s+v[i] , v[i]) # O(1)
        r = max(r,s) # O(1)
    return r
    


MAX_LEN = 50  # Maximum length of input list.

# Initialise results containers:

lengths_queHace1  = []
times_queHace1    = []

lengths_queHace2 = []
times_queHace2   = []

lengths_queHace3 = []
times_queHace3   = []


for length in range(1, MAX_LEN):
    
    # Generate random values:
    
    v = random.sample(range(-100,100),length)

    # Time execution (queHace1):
    
    start = time.perf_counter()
    queHace1(v,length)
    end = time.perf_counter()

    # Store results (queHace1):
    
    lengths_queHace1.append(length)
    times_queHace1.append(end - start)

    # Time execution (mcd_rec2):
    
    start = time.perf_counter()
    queHace2(v,length)
    end = time.perf_counter()

    # Store results (mcd_rec2):
    
    lengths_queHace2.append(length)
    times_queHace2.append(end - start)
    
    # Time execution (mcd_iter):
    
    start = time.perf_counter()
    queHace3(v,length)
    end = time.perf_counter()

    # Store results (mcd_iter):
    
    lengths_queHace3.append(length)
    times_queHace3.append(end - start)
    
    
    
# Plot results

plt.style.use("dark_background")
plt.figure().canvas.manager.set_window_title("Algoritmos 'queHace' - Time Complexity")
plt.xlabel("List Length")
plt.ylabel("Execution Time (s)")
plt.plot(lengths_queHace1, times_queHace1, label="queHace1")
plt.plot(lengths_queHace2, times_queHace2, label="queHace2")
plt.plot(lengths_queHace3, times_queHace3, label="queHace3")
plt.legend()
plt.tight_layout()
plt.show()


# Polynomial fit for 'queHace1'

ns = np.linspace(1, 100000, 20, dtype = int)
ts = [timeit.timeit('queHace1(lst, len(lst) )',
                setup='lst=random.sample(range(-100,100),{})'.format(n),
                globals=globals(),
                number=1000)
      for n in range(1,len(ns)+1)]

plt.plot(ns, ts, 'or')

degree = 5
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], label="queHace1")


# Polynomial fit for 'queHace2'

ns = np.linspace(1, 100000, 20, dtype = int)
ts = [timeit.timeit('queHace2(lst, len(lst) )',
                setup='lst=random.sample(range(-100,100),{})'.format(n),
                globals=globals(),
                number=1000)
      for n in range(1,len(ns)+1)]

plt.plot(ns, ts, 'or')

degree = 5
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], label="queHace2")


# Polynomial fit for 'queHace3'

ns = np.linspace(1, 100000, 20, dtype = int)
ts = [timeit.timeit('queHace3(lst, len(lst) )',
                setup='lst=random.sample(range(-100,100),{})'.format(n),
                globals=globals(),
                number=1000)
      for n in range(1,len(ns)+1)]

plt.plot(ns, ts, 'or')

degree = 5
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], label="queHace3")
plt.legend()





