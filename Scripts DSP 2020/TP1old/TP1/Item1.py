from FuncionesTP import *

señal,n,fs=senalTP() #defino funcion sen(2pi*f*n)
data = np.ones(1000)
lamedia1=lamedia(data)
desviomedio1=desviomedio(data,lamedia1)
desvioestandar1=desvioestandar(data,lamedia1)
rms1=rms(data)

#Reporte de resultados
print("El valor medio es: ",lamedia1)
print("El desvio medio es: ",desviomedio1)
print("El desvio estandar es: ",desvioestandar1)
print("El valor rms es: ", rms1)

print ("\n")

print("Resultados para la señal sinusoidal: ")

print ("\n")

lamediasin=lamedia(señal)
desviomediosin=desviomedio(señal,lamediasin)
desvioestandarsin=desvioestandar(señal,lamediasin)
rmssin=rms(señal)

print("El valor medio es: ",lamediasin)
print("El desvio medio es: ",desviomediosin)
print("El desvio estandar es: ",desvioestandarsin)
print("El valor rms es: ",rmssin)
