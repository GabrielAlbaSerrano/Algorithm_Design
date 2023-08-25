#include <iostream>
#include <stdio.h>
#include <time.h>


using namespace std ;


/*

    PRÁCTICA 1 (PARTE 2): ANÁLISIS DE LA EFICIENCIA DE ALGORITMOS DE
                          ORDENACIÓN Y DE BÚSQUEDA EN C/C++

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1

    APELLIDOS: Alba Serrano
    NOMBRE: Gabriel

 
*/



/* ALGORITMOS DE ORDENACIÓN (SELECCIÓN E INSERCIÓN) */



/*
 
 EJERCICIO 1: Escribe el código en C++ de los algoritmos
 de ordenación por selección y de ordenación por inserción.
 (OPCIONAL) Escribe también el código en C++ de los algoritmos
 de ordenación quicksort y mergesort.
 
 */

void intercambiar(int v[], int i, int j){
	int aux = v[i] ;
	v[i] = v[j] ;
	v[j] = aux ;
}

void selectionSort(int v[], int N){
	int pmin ;
	for (int i = 0 ; i < N-1 ; i++ ){
		pmin = i ;
		for (int j = i+1 ; j < N ; j++){
			if (v[j] < v[pmin]){
				pmin = j ;
			}
		}
		intercambiar(v,i,pmin) ;
	}
}


void insertionSort(int v[], int N){
	int elem, j;
	for (int i = 0 ; i < N ; i++){
		elem = v[i] ;
		j = i-1 ;
		while (j >= 0 && elem < v[j]){
			v[j+1] = v[j] ;
			j = j-1 ;
		}
		v[j+1] = elem ;
	}
}


/*
	Para las funciones quickSort y mergeSort necesito las
	funciones auxiliares particion y mezclar, respectivamente.
*/



int particion(int v[], int c, int f){
	int piv, i, d, p ;
	piv = v[c] ;
	i = c+1 ;
	d = f ;
	while (i != d+1){
		while (i <= d && v[i] <= piv){
			i = i+1 ;
		}
		while ( i <= d && v[d] >= piv){
			d = d-1 ;
		}
		if (i < d){
			intercambiar(v,i,d) ;
			i = i+1 ;
			d = d-1 ;
		}
	}
	intercambiar(v,c,d) ;
	p = d ;
	return p ;
}

void quickSort(int v[], int inicio, int fin){
	int p ;
	if (inicio < fin){
		p = particion(v,inicio,fin) ;
		quickSort(v,inicio,p-1) ;
		quickSort(v,p+1,fin) ;
	}
}

void mezclar(int v[], int c, int m, int f){
	int w[f+1] ;
	int i, j, k ;
	i = c ;
	j = m+1 ;
	k = c ;
	while (i <= m && j <= f){
		if (v[i] <= v[j]){ w[k] = v[i] ; i = i+1 ; }
		else{ w[k] = v[j] ; j = j+1 ; }
		k = k+1 ;
	}
	if (i > m){
		for (int l = j ; l <= f ; l++){
			w[k] = v[l] ;
			k = k+1 ;
		}
	}
	else{
		for (int l = i ; l <= m ; l++){
			w[k] = v[l] ;
			k = k+1 ;
		}
	}
	for (int l = c ; l <= f ; l++){
		v[l] = w[l] ;
	}
}


void mergeSort(int v[], int inicio, int fin){
	int m ;
	if (inicio < fin){
		m = (inicio + fin)/2 ;
		mergeSort(v,inicio,m) ;
		mergeSort(v,m+1,fin) ;
		mezclar(v,inicio,m,fin) ;
	}
}



/* ALGORITMOS DE BÚSQUEDA (SECUENCIAL Y BINARIA) */



/*
 
 EJERCICIO 2: Escribe el código en C++ de los algoritmos
 de búsqueda secuencias y de búsqueda binaria.
 
 */



int busquedaSecuencial(int v[], int longitud, int item){
	int i = 0 ;
	while (i < longitud && v[i] != item){ i = i+1 ;
	}
	if (i == longitud){ 
		return -1 ; 
	}
	else{ 
		return i ;
	}
}
	
/* El vector v tiene que estar ordenado */ 
int busquedaBinaria(int v[], int item, int s1, int s2){
	int m ;
	if (s1 > s2){
		return -1 ;
	}
	else{
		m = (s1+s2)/2 ;
		if (item < v[m]){
			return busquedaBinaria(v,item,s1,m-1) ;
		}
		else if (item == v[m]){
			return m ;
		}
		else{
			return busquedaBinaria(v,item,m+1,s2) ;
		}
	}
}



int main()
{
    
    
    /* DATOS DE ENTRADA */
    
    
    const int DIM = 50 ;
    int v[DIM] ;
    int N ;
   
    cout << "Introduce la longitud del vector: " ;
    cin >> N ;
    cout << endl ;
    
    cout << "Introduce las " << N << " componentes del vector: \n" ;
    for (int i = 0 ; i < N ; i++) cin >> v[i] ;
    cout << endl ;
    
    
    /* ALGORITMOS DE ORDENACIÓN (SELECCIÓN E INSERCIÓN) */
    
    
    int w[DIM] ;
    for (int i = 0 ; i < N ; i++) w[i] = v[i] ;
    
    cout << "Ordenar el vector (1.- Seleccion | 2.- Insercion | 3.- QuickSort | 4.- MergeSort): " ;
    int opcion ;
    cin >> opcion ;
    cout << endl ;
    
    if (opcion == 1) {
        
        cout << "Resultado de la funcion 'selectionSort': " ;
        selectionSort(w, N) ;
        for (int i = 0 ; i < N ; i++) cout << w[i] << " " ;
        cout << endl << endl ;
        
    }
        
    if (opcion == 2) {
        
        cout << "Resultado de la funcion 'insertionSort': " ;
        insertionSort(w, N) ;
        for (int i = 0 ; i < N ; i++) cout << w[i] << " " ;
        cout << endl << endl ;
        
    }
    
    if (opcion == 3) {
        
        cout << "Resultado de la funcion 'quickSort': " ;
        quickSort(w, 0, N-1) ;
        for (int i = 0 ; i < N ; i++) cout << w[i] << " " ;
        cout << endl << endl ;
        
    }
    
    if (opcion == 4) {
        
        cout << "Resultado de la funcion 'mergeSort': " ;
        mergeSort(w, 0, N-1) ;
        for (int i = 0 ; i < N ; i++) cout << w[i] << " " ;
        cout << endl << endl ;
        
    }
    
    
    /* ALGORITMOS DE BÚSQUEDA (SECUENCIAL Y BINARIA) */
        
    
    cout << "Introduce el elemento a buscar en el vector ordenado: " ;
    int item ;
    cin >> item ;
    cout << endl ;
    
    if (busquedaSecuencial(w, N, item) != -1) cout << "SI encontrado (busqueda secuencial)" << endl ;
    else cout << "NO encontrado (busqueda secuencial)" << endl ;
    cout << endl ;
    
    if (busquedaBinaria(w, item, 0, N) != -1) cout << "SI encontrado (busqueda binaria)" << endl ;
    else cout << "NO encontrado (busqueda binaria)" << endl ;
    cout << endl ;
        
    
    /* MEDIDAS DEL TIEMPO DE EJECUCION DE LOS PROGRAMAS */
  
    
    int repeticiones ;
    int tamanyos[DIM] ;
    double tiempos[DIM] ;
    clock_t t1, t2 ;
    
    cout << "Introduce el numero de repeticiones: " ;
    cin >> repeticiones ;
    cout << endl ;

    for (int i = 0 ; i < N ; i++) tamanyos[i] = i + 1 ;
    
    
    /* TIEMPOS DE EJECUCIÓN DE LOS ALGORITMOS DE ORDENACIÓN (SELECCIÓN E INSERCIÓN) */
    
    
    for (int i = 0 ; i < N ; i++) w[i] = v[i] ;
  
    cout << "Medidas del tiempo de ejecucion del programa 'selectionSort': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          selectionSort(w, tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    
    for (int i = 0 ; i < N ; i++) w[i] = v[i] ;
    
    cout << "Medidas del tiempo de ejecucion del programa 'insertionSort': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          insertionSort(w, tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;

    
    /* (OPCIONAL) TIEMPOS DE EJECUCIÓN DE LOS ALGORITMOS DE ORDENACIÓN (MERGESORT Y QUICKSORT) */
    
    
    /* quickSort */
    
    for (int i = 0 ; i < N ; i++) w[i] = v[i] ;
    
    cout << "Medidas del tiempo de ejecucion del programa 'quickSort': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          quickSort(w, 0, tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
	
	/* mergeSort */
	
	for (int i = 0 ; i < N ; i++) w[i] = v[i] ;
  
    cout << "Medidas del tiempo de ejecucion del programa 'mergeSort': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          mergeSort(w, 0, tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    
    
    /* TIEMPOS DE EJECUCIÓN DE LOS ALGORITMOS DE BÚSQUEDA (SECUENCIAL Y BINARIA) */
    
    
    cout << "Medidas del tiempo de ejecucion del programa 'busquedaSecuencial': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          busquedaSecuencial(w, tamanyos[k], tamanyos[0]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    
    cout << "Medidas del tiempo de ejecucion del programa 'busquedaBinaria': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          busquedaBinaria(w, 0, tamanyos[k], tamanyos[0]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    
}
