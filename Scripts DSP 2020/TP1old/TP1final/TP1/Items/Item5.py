from FuncionesTP import *
import time
import heapq

'''En este script se implementan las funciones mediamovild y mediamovildr (FuncionesTP) para aplicar el filtro de media movil a la señal senoidal del Item 1 (x(t)=sen(2pi*f*t)) de manera directa y recursiva, respectivamente. Se comparan los tiempos de ejecución de cada una. Finalmente, se aplica el filtro de modo tal que se deja pasar la componente de 10 kHz de dicha señal, atenuendo la energía en la frecuencia indicada alrededor de 3 dB por debajo de la señal original.
'''

s1=señal # Función x(t)=sen(2pi*f*t) definida en módulo FuncionesTP.
n=t
N = len(n)
M=2 # Largo de la ventana del filtro de media movil calculado para conseguir el objetivo solicitado en la consigna.

# Comparación de tiempos de ejecución de ambas funciones.
time1 = time.time()  # Iniciar tiempo.
xfd=mediamovild(s1,M)  # Ejecutar función.
tiempo_d = time.time()-time1  # Calcular tiempo de ejecucion total.
time2 = time.time()  # Iniciar tiempo.
xfr= mediamovildr(s1,M)  # Ejecutar función.
tiempo_r = time.time()-time2  # Calcular tiempo de ejecucion total.

#Reporte de resultados temporales
datos=[["Directa", round(tiempo_d*1000,2)],["Recursiva",round(tiempo_r*1000,2)]]
Tabla = """\
+----------------------------------------------------+
| Implementación del FMM |  Tiempo de ejecución [ms] |
|----------------------------------------------------|
{}
+----------------------------------------------------+\
"""
Tabla = (Tabla.format('\n'.join("| {:<21s}  | {:>25} |".format(*fila)
 for fila in datos)))
print ("\n")
print("                  Resultados Item 5 ")
print (Tabla)

#FFT's
FFT=abs(np.fft.fft(s1)) #FFT de la señal original
FFTd=abs(np.fft.fft(xfd)) #Calcular la FFt para la señal filtrada con media movil directa
FFTr=abs(np.fft.fft(xfr)) #Idem recursiva
Maxlabel1=heapq.nlargest(2, FFTd) #Crear un vector de máximos de la señal FFTd (Corresponderán a los magnitudes en 0 Hz y 10 kHz)
Maxlabel1=int(round(Maxlabel1[1])) #Almacenar el valor maximo en una variable (Es decir la amplitud en 10 kHz)
Maxlabel2=heapq.nlargest(2, FFTr) #Idem recursiva
Maxlabel2=int(round(Maxlabel2[1]))
Maxlabel=heapq.nlargest(2, FFT)
Maxlabel=int(round(Maxlabel[1]))

#Gráficos
f = np.arange(0,fs/2,(fs/2)/int(N/2)) #Crear un vector de muestras para graficar con relacion a la Frecuencia de sampleo
t = np.arange(0,N)
#Gráficos en muestras
sp1=plt.figure('Item 5: Comparación en muestras')
plt.subplot(3,1,1)
plt.plot(t[0:round(N/64)],s1[0:round(N/64)],'#738EB6') #Gráfico de la señal original del punto uno
plt.title('Señal original')
plt.grid('both')
plt.ylabel('x [n]')
plt.xlabel('Número de muestra [n]')
sp1=plt.subplot(3,1,2)
plt.plot(t[0:round(N/64)],xfd[0:round(N/64)],'#BF76D2') #Grafico de la señal filtrada con la media movil directa
plt.title('Señal filtrada por media movil directa')
plt.grid('both')
plt.ylabel('xfd [n]')
plt.xlabel('Número de muestra [n]')
sp1=plt.subplot(3,1,3)
plt.plot(t[0:round(N/64)],xfr[0:round(N/64)],'#e0503f') #Grafico de la señal filtrada con la media movil recursiva
plt.title('Señal filtrada por media movil recursiva')
plt.grid('both')
plt.ylabel('xfr [n]')
plt.xlabel('Número de muestra [n]')
plt.subplots_adjust(hspace = 1.2)
#Gráficos en frecuencias.
plt.figure('Item 5: Comparación en frecuencias')
sp2=plt.subplot(3,1,1)
plt.plot(f,FFT[0:int(N/2)],'#738EB6') #Grafico en frecuencia de la señal filtrada con la media movil directa
plt.title('Señal original')
plt.grid('both')
plt.ylabel('X[k]')
plt.xlabel('Frecuencia [Hz]')
plt.Axes.annotate(sp2, f"{round(Maxlabel)}",xy=(10100,Maxlabel-1100))
sp2=plt.subplot(3,1,2)
plt.plot(f,FFTd[0:int(N/2)],'#BF76D2') #Grafico en frecuencia de la señal filtrada con la media movil directa
plt.title('Señal filtrada por media movil directa')
plt.grid('both')
plt.ylabel('XFD[k]')
plt.xlabel('Frecuencia [Hz]')
plt.Axes.annotate(sp2, f"{round(Maxlabel1)}",xy=(10100,Maxlabel1-1100))
sp2=plt.subplot(3,1,3)
plt.plot(f,FFTr[0:int(N/2)],'#e0503f') #Grafico en frecuencia de la señal filtrada con la media movil recursiva
plt.grid('both')
plt.ylabel('XFR[k]')
plt.xlabel('Frecuencia [Hz]')
plt.Axes.annotate(sp2, f"{round(Maxlabel2)}",xy=(10100,Maxlabel2-1100))
plt.title('Señal filtrada por media movil recursiva')
plt.subplots_adjust(hspace = 1.2)
plt.show()
