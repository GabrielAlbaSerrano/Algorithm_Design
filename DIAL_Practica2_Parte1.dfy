/*


    PRÁCTICA 2 (PARTE 1): ESPECIFICACIÓN Y VERIFICACIÓN DE ALGORITMOS SENCILLOS EN DAFNY

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1

    APELLIDOS: Alba Serrano
    NOMBRE: Gabriel


*/



/*

     Completa la especificación y el código de los siguientes algoritmos para que las verificaciones realizadas
     con Dafny sean todas correctas.

*/



method Ejercicio_2_1_a(x : int, y : int)

   requires x > 0
   requires y > 0
   ensures  x + y > 0

{

}


method Ejercicio_2_1_d(x : int, y : int)

   requires x*y < 0
   ensures  x > 0 <==> y < 0

{

}


method Ejercicio_2_2_a(x : int) returns (y : int)
   
    requires x >= -2
    ensures  y >= 0

{

    y := x + 2 ;

}


method Ejercicio_2_2_b(x : int) returns (y : int)

    requires x <= 20/3
    ensures  y <= 20

{

    y := 3 * x ;

}


method Ejercicio_2_2_d(x : int) returns (y : int)

    requires true
    ensures  y == x + 1

{

    y := x + 1 ;

}


method Ejercicio_2_2_f(x : int) returns (y : int)

    requires true
    ensures  y == x % 2

{

    y := x % 2 ; 

}


method Ejercicio_2_2_g(b : bool, x : int) returns (b2 : bool)

    requires !b && x <= 0 
    requires x >= 0 
    ensures  !b2

{

    b2 := b || (x > 0) ;

}


method Ejercicio_2_3_a(x : int, y : int) returns (x1 : int, y1 : int)

    requires true
    ensures  x1 == old(y)
    ensures  y1 == old(x)

{

    x1, y1 := y, x ;

}


method Ejercicio_2_3_b(x : int, y : int) returns (x1 : int, y1 : int)

    requires x + y > 0
    ensures  x1 + y1 > 0

{

    x1, y1 := x + 1, y - 1 ;

}


method Ejercicio_2_3_c(x : int, y : int) returns (x1 : int, y1 : int)

    requires x + y > 0
    ensures  x1 + y1 > 0

{

    x1, y1 := y + 1, x - 1 ;

}


method Ejercicio_2_3_d(x : int, y : int, z : int) returns (x1 : int, y1 : int, z1 : int)

    requires true
    ensures  x1 + y1 + z1 == 2*x + 2*y

{

    x1, y1, z1 := x + 1, y - 1, x + y ;

}


method Ejercicio_2_4_a(x : int) returns (y : int)

    requires x*x + 1 > 0
    ensures  y > 0

{

    var z : int ;

    z := x * x ;
    y := z + 1 ;

}


method Ejercicio_2_4_b(x : int, y : int) returns (z : int)

    requires y - x > 0
    ensures  z > 0

{

    var z1 : int ;

    z1 := x + y      ;
    z  := 2 * y - z1 ;

}


method Ejercicio_2_4_c(x : int, y : int) returns (z : int)

    requires x != 2
    ensures  z > 0

{
    var t : int ;

    z := 4 * x ;
    z := x*x - z ;
    z := z + 4 ;

}


method Ejercicio_2_4_d(x : int, y : int) returns (z1 : int, z2 : int)

    requires true
    ensures  z1 == z2

{

    z1 := x ;
    z2 := x ;

}


method Ejercicio_2_5_a(x : int) returns (y : int)

    requires x == 4 || x == -4
    ensures  y == 4

{

    if x >= 0 {

        y := x ;
  
    } else {

        y := -x ;

    }

}


method Ejercicio_2_5_b(x : int, n : int) returns (y : int)

    requires x == 2*n || x == 2*n - 1
    ensures  y == n

{

    if x % 2 == 0 {

        y := x / 2 ;
  
    } else {

        y := x / 2 + 1 ;

    }

}


method Ejercicio_2_5_c(x : int, y : int) returns (z : int)

    requires x > y || x == y || x < y
    ensures  z > y

{

    if x > y { 

        z := x ;

    } else if x == y {

        z := x + 1 ;

    } else if x < y {

        z := y + 2 ;

    }

}


method Ejercicio_2_6(x : int, y : int) returns (z1 : int, z2 : int)

    requires true
    ensures  z1 == old(y)
    ensures  z2 == old(x)

{

    z1 := x  - y  ;
    z2 := z1 + y  ;
    z1 := z2 - z1 ;

}

