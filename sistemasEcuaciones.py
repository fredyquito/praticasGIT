import numpy as np
from sympy import *


#definimos la matriz de ecuaciones solo letras
A = np.array([[3,5], [2,-1]])

#definir el vector de terminos independientes
B = np.array([7,-4])

#resolver el sistema de ecuaciones

x = np.linalg.solve(A,B)

#convertimos el resultado en fracciones

#defino lista para guardar los resultados
fracciones = []
#recorro el resultado de la resolucion de las ecuaciones y uso la funcion Rational para expresar el resultado en fracciones 
for decimal in x:
    fraccion = Rational(decimal).limit_denominator()
    fracciones.append(fraccion)
#imprimo solucion en forma de quebrados
print(fracciones)