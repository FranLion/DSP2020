from FuncionesTP import *

''' Las funciones para calcular el valor medio, el desvío medio, desvío estandar y el valor rms, pedidos en la consigna, se encuentran definidas en el módulo FuncionesTP. En este script se implementan dichas funciones para calcular los parámetros pedidos para la señal finita x[n]=data de largo N=1000 y la señal senoidal x(t)= 2 + sen(2πft), ambas definidas en el mismo módulo.
'''


#Se calculan los parámetros de la señal data, pedidos en la consigna.
lamedia1=lamedia(data)
desviomedio1=desviomedio(data,lamedia1)
desvioestandar1=desvioestandar(data,lamedia1)
rms1=rms(data)
# Se presentan los resultados.
print ("\n")
print("\t \t   Resultados Item 1: ")
print ("\n")
print("\t   Resultados para la señal x[n]=u[n] de largo N=1000: ")
print("\t   El valor medio es:     ",lamedia1)
print("\t   El desvio medio es:    ",desviomedio1)
print("\t   El desvio estandar es: ",desvioestandar1)
print("\t   El valor rms es:       ", rms1)
# Se calculan los parámetros de la señal senoidal x(t)= 2 + sen(2πft).
lamediasin=lamedia(señal)
desviomediosin=desviomedio(señal,lamediasin)
desvioestandarsin=desvioestandar(señal,lamediasin)
rmssin=rms(señal)
#Se presentan los resultados.
print ("\n")
print("\t   Resultados para la señal senoidal x(t)= 2 + sen(2πft): ")
print("\t   El valor medio es:     ",round(lamediasin,3))
print("\t   El desvio medio es:    ",round(desviomediosin,3))
print("\t   El desvio estandar es: ",round(desvioestandarsin,3))
print("\t   El valor rms es:       ",round(rmssin,3))
