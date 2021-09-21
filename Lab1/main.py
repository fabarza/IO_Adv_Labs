from metodos import *

'''
------------------------------------------PPL-------------------------------------------

. Para poder  tener una  noción de las  proporciones de  cada  sabor, 
la dulcería determinó que la mezcla no puede contener más del 40% del caramelo A y debe tener 
al menos 30% de B para que sea  rentable la producción. El entusiamo  es  tan  ferviente, que 
han puesto un cartel, promocionando el producto, fuera de su tienda aun cuando no han deter-
minado una receta con cantidades exactas. Todos entran en pánico porque un cliente ya realizó
un pedido de  este  nuevo producto y los  trabajadores de la  dulcería  necesitan saber ¿Cuál 
es la menor cantidad en gramos que se puede  ocupar  de  cada uno para poder generar  la mayor 
cantidad de bolsitas de 200 gramos en total?

--------------------------------Variables de desición------------------------------------

A_gr: gramos de caramelos del sabor A 
B_gr: gramos de caramelos del sabor B

--------------------------------------Restricciones--------------------------------------

A_gr + B_gr  = 200 gr.
A_gr        <= 0.4 * (A_gr + B_gr)
B_gr        >= 0.3 * (A_gr + B_gr)
A_gr > 0
B_gr > 0

           *** Se asume que A_gr y B_gr sólo pueden tomar valores positivos ***

-----------------------------------Función objetivo---------------------------------------

Minimizar el costo de la producción de bolsitas de 200 gramos con caramelos de sabores A y B:
 ->                           F(a,b) = 300 * A_gr + 800 * B_gr

-------------------------------------Instrucciones-----------------------------------------

•	Indique si el espacio factible es distinto de vacío (10)
•	Indique si el espacio factible es cerrado o abierto (10)

Si el espacio factible es distinto de vacío y cerrado, entonces el programa deberá:

•	Mostrar gráficamente las curvas de nivel de la función objetivo (5)
•	Mostrar gráficamente, el espacio factible (5)
•	Identificar el conjunto de posibles soluciones del PPL (10)
•	Identificar una solución óptima del problema (10)

------------------------------------------------------------------------------------------
'''
#---------------------------------------Desarrollo----------------------------------------

def main():
    f_objetivo = funcion_objetivo()
    rest = restricciones()
    return
main()

#-----------------------------------------------------------------------------------------