'''from IO_Adv_Labs.Lab1.funciones import evaluarFuncion'''
import matplotlib.pyplot as plt
import numpy as np
import sys
from metodos import evaluarFuncion
import grafico

'''
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
# ---------------------------------------Desarrollo----------------------------------------


def main():
    info = leerDatos()
    x1 = np.linspace(0, 10, 1)
    y1 = np.linspace(0, 10, 1)

    # for i in x1:
    #     plt.plot(i, i)

    plt.show()


# -----------------------------------------------------------------------------------------

def leerDatos():
    if(len(sys.argv) < 2):
        print("Ingrese la ruta del archivo")
        sys.exit()
    else:
        try:
            file = open(sys.argv[1])
        except OSError as e:
            print(e)
        else:
            list = []
            list.append(file.readline().rstrip("\n"))
            list.append(file.readline().rstrip("\n"))

            for line in file.readlines():
                list.append(line.rstrip("\n"))

    return list


main()
