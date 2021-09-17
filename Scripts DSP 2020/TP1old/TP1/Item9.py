from FuncionesTP import *
''' En este inciso se grafica la respuesta en frecuencia del filtro media móvil con una resolución de 44100 Hz. Cabe señalar que el largo de la ventana obtenido en el Item 5 corresponde a M+1=2.
'''
M=1 #El largo de la ventana es L=M+1.
w=np.arange(-1*np.pi,np.pi,2*np.pi/44100) #Se genera un vector de muestras con frecuencia de sampleo de 44100 Hz.
H=abs((1/(M+1))*((np.sin(w*(M+1)/2))/(np.sin(w/2)))) #Respuesta en frecuencia del filtro media móvil.

# Se Grafican los resultados.
plt.figure('Item 9 Grafico de magnitud para respuesta del filtro')
plt.plot(w,H)
# Gráfico de magnitud de respuesta en frecuencia del filtro media móvil.
plt.title('Respuesta en frecuencia')
plt.xlabel('Frecuencia angular ω [rad/s]')
plt.ylabel('Respuesta H[ω]')
plt.show()
