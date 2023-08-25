/*


    PRÁCTICA 3 (PARTE 1): DISEÑO DE ALGORITMOS RECURSIVOS EN DAFNY

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1

    APELLIDOS: Alba Serrano
    NOMBRE:    Gabriel


*/



/*


	EJERCICIO 5.3: SUMA DE UN VECTOR

	Considera la siguiente especificación de un algoritmo para sumar todos
	los elementos de un vector de enteros dado:


	     { P : N >= 0 }

	     fun suma_vector(v[0..N) de ent) dev s : int 

	     { Q : s = ( Sumatorio i : 0 <= i < N : v[i] ) }	


	a) Diseña un algoritmo recursivo lineal no final planteando una INMERSIÓN 
	   NO FINAL.

	b) Diseña un algoritmo recursivo lineal final planteando una INMERSIÓN 
	   FINAL.


*/



// FUNCIÓN AUXILIAR PARA ESPECIFICAR LA SUMA DE UN VECTOR



function sum_vector(v : array?<int>, n : nat) : int

	requires  v != null && 0 <= n <= v.Length

	decreases n

	reads v

{

	if n == 0 then 0
	else sum_vector(v, n - 1) + v[n - 1]

}



// INMERSIÓN NO FINAL



method suma_vector1(v : array?<int>) returns (s : int)     // O(v.Length)

	requires v != null
	ensures  s == sum_vector(v, v.Length)

{

	s := gsuma_vector(v, v.Length) ;

}



method gsuma_vector(v : array?<int>, n : nat) returns (s : int)     // O(n)

	requires  v != null && 0 <= n <= v.Length
	ensures   s == sum_vector(v, n)

	decreases n

{

	if n == 0 {

		s := 0 ;

	} else {

		var s1 : int ;

		s1 := gsuma_vector(v, n - 1) ;

		s := s1 + v[n - 1] ;

	}

}



// INMERSIÓN FINAL



method suma_vector2(v : array?<int>) returns (s : int)     // O(v.Length)

	requires v != null
	ensures  s == sum_vector(v, v.Length)

{

	s := gfsuma_vector(v, 0, 0) ;

}



method gfsuma_vector(v : array?<int>, n : nat, w : int) returns (s : int)     // O(N - n)

	requires  v != null && 0 <= n <= v.Length && w == sum_vector(v, n)
	ensures   s == sum_vector(v, v.Length)

	decreases v.Length - n

{

	if n == v.Length {

		s := w ;

	} else {

		s := gfsuma_vector(v, n + 1, w + v[n]) ;

	}

}





/*



	EJERCICIO 5.7: PRODUCTO ESCALAR DE DOS VECTORES

	Diseña algoritmos recursivos para calcular el producto escalar de dos 
	vectores de enteros dados de igual longitud, planteando, primero, una 
	inmersión no final, y después, una inmersión final.



*/


// FUNCIÓN AUXILIAR PARA ESPECIFICAR EL PRODUCTO ESCALAR DE DOS VECTORES

function prod_escalar(v : array?<int>, w : array?<int>, n : nat) : int

	requires  v != null && w != null
	requires v.Length == w.Length
	requires 0 <= n <= v.Length

	decreases v.Length - n

	reads v
	reads w

{

	if n == v.Length then 0
	else prod_escalar(v, w, n + 1) + v[n] * w[n]

}

// INMERSIÓN NO FINAL

method prod_escalar_no_final(v : array?<int>, w : array?<int>) returns (s : int)     // O(v.Length)

	requires v != null && w != null
	requires v.Length == w.Length
	ensures  s == prod_escalar(v, w, 0)

{

	s := gprod_escalar(v, w, 0) ;

}


method gprod_escalar(v : array?<int>, w : array?<int>, n : nat) returns (s : int)     // O(N-n)

	requires  v != null && w != null
	requires v.Length == w.Length
	requires 0 <= n <= v.Length
	ensures s == prod_escalar(v, w, n)

	decreases v.Length - n

{

	if n == v.Length {

		s := 0 ;

	} else {

		var s1 : int ;

		s1 := gprod_escalar(v, w, n + 1) ;

		s := s1 + v[n] * w[n] ;

	}

}


// INMERSIÓN FINAL


method prod_escalar_final(v : array?<int>, w : array?<int>) returns (s : int)     // O(v.Length)

	requires v != null && w != null
	requires v.Length == w.Length
	ensures  s == prod_escalar(v, w, 0)

{

	s := gfprod_escalar(v, w, v.Length, 0) ;

}



method gfprod_escalar(v : array?<int>, w : array?<int>, n : nat, r : int) returns (s : int)     // O(n)

	requires  v != null && w != null
	requires v.Length == w.Length
	requires 0 <= n <= v.Length
	requires r == prod_escalar(v, w, n)
	ensures s == prod_escalar(v, w, 0)

	decreases n

{

	if n == 0 {

		s := r ;

	} else {

		s := gfprod_escalar(v, w, n - 1, r + v[n-1] * w[n-1]) ;


	}

}


// PROGRAMA PRINCIPAL PARA PROBAR LOS ALGORITMOS RECURSIVOS DISEÑADOS

method Main()
{

	var v := new int[] [-1, 2, 5, -5, 8] ;
	var w := new int[] [ 1, 0, 5,  5, 8] ;
	var s1 := suma_vector1(v) ;
	var s2 := suma_vector1(w) ;
	var p1 := prod_escalar_no_final(v,w) ;
	var p2 := prod_escalar_final(v,w) ;

	print("\n") ;
	print("La suma del primer vector es: ") ;
	print(s1) ;
	print("\n") ;
	print("La suma del segundo vector es: ") ;
	print(s2) ;
	print("\n") ;

	print("El producto escalar de v y w con un algoritmo obtenido por inmersion no final es: ") ;
	print(p1) ;
	print("\n") ;
	print("El producto escalar de v y w con un algoritmo obtenido por inmersion final es: ") ;
	print(p2) ;

	print("\n\n") ;

	
}