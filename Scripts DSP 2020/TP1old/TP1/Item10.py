from FuncionesTP import *
''' Este Script compara gráficamente las respuetas en frecuencia en dB de las ventanas rectangular y blackman, ambas de largo T=1000. En suma, realizamos la misma comparación usando las respuestas en frencuencia calculadas analíticamente(Ver FuncionesTP/RF_boxcar y FuncionesTP/RF_blackman).
'''
T=1000 #Largo de las ventanas.

#Se calculan las Respuestas en frecuencias de las ventanas con las definiciones de Scipy y usando FFT.
wRect=signal.windows.boxcar(T)
wBlackman = signal.blackman(T)
RFdB_R=RFdB_ventanas(np.fft.fft(wRect,fs),T) # Respuesta en Frecuencia de la ventana rectangular en dB.
RFdB_B=RFdB_ventanas(np.fft.fft(wBlackman,fs),T) # Respuesta en Frecuencia de la ventana blackman en dB.

# Se obtienen las Respuestas en frecuencia de las ventanas a partir de las Repuestas en frecuncia calculadas analíticamente.
f=np.arange(-1*np.pi,np.pi,2*np.pi/fs)
RF_rect=RF_boxcar(T,f)
RF_blackman=RF_Blackman(T,f)
RFdB_Rect=RFdB_ventanas(RF_rect,T) # Respuesta en Frecuencia analítica de la ventana rectangular en dB.
RFdB_Black=RFdB_ventanas(RF_blackman,T)  # Respuesta en Frecuencia analítica de la ventana blackman en dB.

#Gráficos
#El siguiente gráfico es el utilizado para reportar los resultados del punto 10 debido a que presenta mayor precisión
plt.figure('Item 10 metodo 1')
plt.plot(f,np.fft.fftshift(RFdB_B),'#065535', label='Blackman')
#Gráfico de la respuesta en frecuencia de la ventana Blackman
plt.plot(f,np.fft.fftshift(RFdB_R),'#f24738', label='Rectangular')
#Gráfico de la respuesta en frecuencia de la ventana rectangular
plt.legend()
plt.axis([-np.pi/32, np.pi/32, -80, 0])
plt.title("Respuesta en frecuencia de la ventana")
plt.ylabel("Amplitud [dB]")
plt.xlabel("Frecuencia angular [Rad/s]")
plt.grid('both')

#El siguiente Gráfico muestra la respuesta en frecuencia en dB de las ventanas calculadas analíticamente a modo de comparación
#con las respuestas en frecuencia caluladas con funciones nativas del lenguaje.
plt.figure('Item 10 metodo 2')
plt.plot(f,RFdB_Black,'#5e508e',label='Blackman')
#Gráfico de la respuesta en frecuencia de la ventana Blackman
plt.plot(f,RFdB_Rect, '#fbbc5a',label='Rectangular')
#Gráfico de la respuesta en frecuencia de la ventana rectangular
plt.legend()
plt.axis([-np.pi/32, np.pi/32, -80, 0])
plt.title("Respuesta en frecuencia de la ventana")
plt.ylabel("Amplitud [dB]")
plt.xlabel("Frecuencia angular [Rad/s]")
plt.grid('both')
plt.show()
