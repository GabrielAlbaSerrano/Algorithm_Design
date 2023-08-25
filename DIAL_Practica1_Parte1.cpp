#include <iostream>
#include <stdio.h>
#include <time.h>


using namespace std ;


/*

    PRÁCTICA 1: ANÁLISIS DE LA EFICIENCIA DE LOS ALGORITMOS (C/C++)

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1

    APELLIDOS: Alba Serrano
    NOMBRE: Gabriel

*/



int queHace1 (int v[], int N){
    
  int mejor, suma ;
  
  mejor = 0 ;
  
  for (int i = 0 ; i < N ; i++){
      
    for (int j = i ; j < N ; j++){
        
       suma = 0 ;
       
       for (int k = i ; k <= j ; k++) suma = suma + v[k] ;
       
       if (suma > mejor) mejor = suma ;
       
    }
    
  }
  
  return mejor ;
  
}



/*
 
 EJERCICIO 1: Escribe el código en C++ de un algoritmo 'queHace2'
 que resuelva el mismo problema que el del algoritmo anterior
 'queHace1' pero usando solo dos bucles anidados.
 
 */

int queHace2 (int v[], int N){ // O(N^2)
    
  int mejor, suma ; // O(1)
  
  mejor = 0 ; // O(1)
  
  for (int i = 0 ; i < N ; i++){ // O( Sum_{i=0}^{N-1} (N-i) ) = O( N*(N+1)/2 ) = O(N^2)
    
    suma = 0 ; // O(1)
    
    for (int j = i ; j < N ; j++){ // O(N - i)
        
       suma = suma + v[j] ; // O(1)
       
       if (suma > mejor) mejor = suma ; // O(1)
       
    }
    
  }
  
  return mejor ; // O(1)
  
}

/*
 
 EJERCICIO 2: Escribe el código en C++ de un algoritmo 'queHace3'
 que resuelva el mismo problema que el del algoritmo anterior
 'queHace1' pero usando solo un bucle.
 
 */

int queHace3 (int v[], int N){ // O(N-1)
    
  int mejor, suma ; // O(1)
  suma = v[0] ; // O(1)
  mejor = v[0] ; // O(1)
  
  for (int i = 1 ; i < N ; i++){ // O(N-1)
  	
    suma = max(suma+v[i],v[i]) ; // O(1)
    mejor = max(mejor,suma) ; // O(1)
    
  }
  
  return mejor ; // O(1)
  
}

// Otra forma de definir la funcion 'queHace3' seria:

int queHace3b(int v[], int N) { // O(N)
	int s = 0 ; // O(1)
	int r = 0 ; // O(1)
	
	for (int i = 0 ; i < N ; i++){ // O(N)
	    s = max(s+v[i],v[i]) ; // O(1)
	    r = max(r,s) ; // O(1)
    }
    
    return r ; // O(1)
}

int main()
{
    
    /* EJECUCIÓN DE LOS PROGRAMAS */
    
    const int DIM = 50 ;
    int v[DIM] ;
    int N ;
   
    cout << "Introduce la longitud del vector: " ;
    cin >> N ;
    cout << endl ;
    
    cout << "Introduce las " << N << " componentes del vector: \n" ;
    for (int i = 0 ; i < N ; i++) cin >> v[i] ;
    cout << endl ;

    cout << "Vector = " ;
    for (int i = 0 ; i < N ; i++) cout << v[i] << " " ;
    cout << endl << endl ;
    cout << "Resultado de la funcion 'queHace1': " << queHace1(v, N) << "\n" ;
    cout << endl ;
    cout << "Resultado de la funcion 'queHace2': " << queHace2(v, N) << "\n" ;
    cout << endl ;
    cout << "Resultado de la funcion 'queHace3': " << queHace3(v, N) << "\n" ;
    cout << endl ;


    /* MEDIDAS DEL TIEMPO DE EJECUCION DE LOS PROGRAMAS */
  
    
    int repeticiones ;
    int tamanyos[DIM] ;
    double tiempos1[DIM] ;
    clock_t t1, t2 ;
    
    cout << "Introduce el numero de repeticiones: " ;
    cin >> repeticiones ;
    cout << endl ;

    for (int i = 0 ; i < N ; i++) tamanyos[i] = i + 1 ;
  
    cout << "Medidas del tiempo de ejecucion del programa 'queHace1': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock() ;
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          queHace1(v, tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos1[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos1[k] << endl ;
    
    cout << endl ;
    
    
    
    /*
     
     EJERCICIO 3: Escribe el código en C++ para obtener las medidas del tiempo de ejecución
     de los programas 'queHace2' y "queHace3', y compara los resultados obtenido con los del
     programa 'queHace1'. ¿Cuál de los tres programas es más eficiente? ¿Por qué?
     
     */
	
	double tiempos2[DIM] ;
	double tiempos3[DIM] ;
	
	/* queHace2 */ 
	
    cout << "Medidas del tiempo de ejecucion del programa 'queHace2': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock() ;
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          queHace2(v, tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos2[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos2[k] << endl ;
    
    cout << endl ;
    
    /* queHace3 */
    
    cout << "Medidas del tiempo de ejecucion del programa 'queHace3': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock() ;
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          queHace3(v, tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos3[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos3[k] << endl ;
    
    cout << endl ;

	/* Vamos a utilizar el vector con mayor longitud para comparar el tiempo de ejecucion de cada programa */
	
	double n1 = tiempos1[N-1] ;
	double n2 = tiempos2[N-1] ;
	double n3 = tiempos3[N-1] ;
	
	if ( min( min(n1, n2), n3) == n1 ) {
		cout << "El tiempo de ejecucion del programa 'queHace1' es el menor, por lo tanto es el programa mas eficiente" << endl ;	
	}
	
	else if ( min( min(n1, n2), n3) == n2 ) {
		cout << "El tiempo de ejecucion del programa 'queHace2' es el menor, por lo tanto es el programa mas eficiente" << endl ;	
	}
	
	else {
		cout << "El tiempo de ejecucion del programa 'queHace3' es el menor, por lo tanto es el programa mas eficiente" << endl ;
	}
}
