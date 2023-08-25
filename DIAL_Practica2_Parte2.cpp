#include <iostream>
#include <stdio.h>
#include <time.h>



using namespace std ;



/*

    PRÁCTICA 1 (PARTE 2): DISEÑO DE ALGORITMOS ITERATIVOS EFICIENTES EN C/C++

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1

    APELLIDOS:  Alba Serrano
    NOMBRE:     Gabriel

 
*/



/* ALGORITMOS PARA EL PROBLEMA DE LA RAÍZ CUADRADA ENTERA */



int raiz_ent1(int n)     // O(√n)
{
    
    int r = 0 ;
	while (n >= (r+1)*(r+1)){
		r = r+1 ;
	}
	return r ;
	
}



int raiz_ent2(int n)     // O(n)
{
    
	int r = n ;
	while (r*r > n){
		r = r-1 ;
	}
	return r ;

}



int raiz_ent3(int n)     // O(log(n))
{
    
    int r = 0 ;
    int y = n+1 ;
    int h ;
    while (y != r+1){
    	h = (r+y)/2 ;
    	if (h*h < n){
    		r = h ;
		}
		else{
			y = h ;
		}
	}
    return r ;
}



int raiz_ent4(int n, int a, int b)     // O(log(n))
{
    
    int m, r ;
    if (b == a+1){
    	r = a ;
	}
	else if (b > a + 1){
		m = (a+b)/2 ;
		if (m*m <= n){
			r = raiz_ent4(n,m,b) ;
		}
		else{
			r = raiz_ent4(n,a,m) ;
		}
	}
	return r ;
    
}





int main(){
     
    
    /* DATOS DE ENTRADA */
    
    
    int n, r ;
    
    cout << "Introduce el valor a calcular su raiz entera: " ;
    cin >> n ;
    cout << endl ;
    
    r = raiz_ent1(n) ;
    
    cout << "La raiz entera es: " << r << endl ;
    
    r = raiz_ent2(n) ;
    
    cout << "La raiz entera es: " << r << endl ;
    
    r = raiz_ent3(n) ;
    
    cout << "La raiz entera es: " << r << endl ;
    
    r = raiz_ent4(n, 0, n) ;
    
    cout << "La raiz entera es: " << r << endl ;
    
    
    /* MEDIDAS DEL TIEMPO DE EJECUCION DE LOS PROGRAMAS */
      
        
    int repeticiones = 1000 ;
    int tamanyos[repeticiones] ;
    double tiempos[repeticiones] ;
    clock_t t1, t2 ;
        
    cout << endl ;
    cout << "Introduce el numero de repeticiones: " ;
    cin >> repeticiones ;
    cout << endl ;

    for (int i = 0 ; i < repeticiones ; i++) tamanyos[i] = i + 1 ;
        
        
    /* TIEMPOS DE EJECUCIÓN DE LOS ALGORITMOS DE RAIZ CUADRADA ENTERA */
        
        
    cout << "Medidas del tiempo de ejecucion del programa 'raiz_ent1': \n" << endl ;

    for (int k = 0 ; k < repeticiones ; k++){
        
       t1 = clock() ;
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          raiz_ent1(tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < repeticiones ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    
    cout << "Medidas del tiempo de ejecucion del programa 'raiz_ent2': \n" << endl ;

    for (int k = 0 ; k < repeticiones ; k++){
        
       t1 = clock() ;
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          raiz_ent2(tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < repeticiones ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    
    cout << "Medidas del tiempo de ejecucion del programa 'raiz_ent3': \n" << endl ;

    for (int k = 0 ; k < repeticiones ; k++){
        
       t1 = clock() ;
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          raiz_ent3(tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < repeticiones ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    
    cout << "Medidas del tiempo de ejecucion del programa 'raiz_ent4': \n" << endl ;

    for (int k = 0 ; k < repeticiones ; k++){
        
       t1 = clock() ;
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          raiz_ent4(tamanyos[k],0,tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < repeticiones ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
        
}
