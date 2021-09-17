from FuncionesTP import *

s1,n,fs=senalTP()
N = len(n)
M=1 # el valor de M es igual a el ingresado + 1

# Comparación de tiempos de ejecución de ambas funciones.
t = time.time()  # Iniciar tiempo.
xfd=mediamovild(s1,M)  # Ejecutar función.
tiempo_d = time.time()-t  # Calcular tiempo de ejecucion total.
t = time.time()  # Iniciar tiempo.
xfr= mediamovildr(s1,M)  # Ejecutar función.
tiempo_r = time.time()-t  # Calcular tiempo de ejecucion total.

#Reporte de resultados temporales
print("Resultados para la comparación de tiempos de ejecución: ")

print ("\n")

print(f"Directo: {round(tiempo_d,3)}, Recursiva: {round(tiempo_r,3)}")

#FFT's
FFTd=abs(np.fft.fft(xfd)) #Calcular la FFt para la señal filtrada con media movil directa
FFTr=abs(np.fft.fft(xfr)) #Idem recursiva
Maxlabel1=heapq.nlargest(2, FFTd) #Crear un vector de valores máximos de la señal FFTd
Maxlabel1=int(Maxlabel1[1]) #Almacenar el valor maximo en una variable
Maxlabel2=heapq.nlargest(2, FFTr) #Idem recursiva
Maxlabel2=int(Maxlabel2[1])

#Gráficos
f = np.arange(0,fs/2,(fs/2)/int(N/2)) #Crear un vector de muestras para graficar con relacion a la Frecuencia de sampleo
t = np.arange(0,N)
sp1=plt.figure('Item 5 comparación de filtrados')
plt.subplot(3,1,1)
plt.plot(t[0:round(N/64)],s1[0:round(N/64)],'#738EB6') #Gráfico de la señal del punto uno
plt.title('Señal antes de filtrar')
plt.grid('both')
plt.ylabel('Señal x[n]')
plt.xlabel('Número de muestra [n]')
sp1=plt.subplot(3,1,2)
plt.plot(t[0:round(N/64)],xfd[0:round(N/64)],'#BF76D2') #Grafico de la señal filtrada con la media movil directa
plt.title('Filtrado de media movil directa')
plt.grid('both')
plt.ylabel('Señal x[n]')
plt.xlabel('Número de muestra [n]')
sp1=plt.subplot(3,1,3)
plt.plot(t[0:round(N/64)],xfr[0:round(N/64)],'#e0503f') #Grafico de la señal filtrada con la media movil recursiva
plt.title('Filtrado de media movil recursiva')
plt.grid('both')
plt.ylabel('Señal x[n]')
plt.xlabel('Número de muestra [n]')
plt.subplots_adjust(hspace = 1)
sp2=plt.figure('Item 5 comparación de filtrados con FFT')
plt.subplot(2,1,1)
plt.plot(f,FFTd[0:int(N/2)],'#FF4646') #Grafico en frecuencia de la señal filtrada con la media movil directa
plt.title('Filtro de media movil directa')
plt.grid('both')
plt.ylabel('Señal X[k]')
plt.xlabel('Frecuencia [Hz]')
plt.Axes.annotate(sp1, f"{round(Maxlabel1)}",xy=(10100,Maxlabel1-1100))
sp2=plt.subplot(2,1,2)
plt.plot(f,FFTr[0:int(N/2)],'#327345') #Grafico en frecuencia de la señal filtrada con la media movil recursiva
plt.grid('both')
plt.ylabel('Señal X[k]')
plt.xlabel('Frecuencia [Hz]')
plt.Axes.annotate(sp2, f"{round(Maxlabel2)}",xy=(10100,Maxlabel2-1100))
plt.title('Filtro de media movil recursiva')
plt.subplots_adjust(hspace = 0.6)
plt.show()
