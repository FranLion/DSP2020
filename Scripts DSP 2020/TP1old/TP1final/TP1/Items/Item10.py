from FuncionesTP import *

''' Este Script compara gráficamente las respuetas en frecuencia en dB de las ventanas rectangular y blackman, ambas de largo T=1000 y con resolución dada por una Fs=44100 Hz.
'''
T=1000 #Largo de las ventanas.

#Se calculan las Respuestas en frecuencias de las ventanas con las definiciones de Scipy y usando FFT.
wRect=signal.windows.boxcar(T)
wBlackman = signal.blackman(T)
RFdB_R=RFdB_ventanas(np.fft.fft(wRect,fs),T) # Respuesta en Frecuencia de la ventana rectangular en dB.
RFdB_B=RFdB_ventanas(np.fft.fft(wBlackman,fs),T) # Respuesta en Frecuencia de la ventana blackman en dB.
f=np.arange(-1*np.pi,np.pi,2*np.pi/fs)
#Gráficos
#El siguiente gráfico es el utilizado para reportar los resultados del punto 10 debido a que presenta mayor precisión
plt.figure('Item 10')
plt.plot(f,np.fft.fftshift(RFdB_B),'#065535', label=' Ventana Blackman')
#Gráfico de la respuesta en frecuencia de la ventana Blackman
plt.plot(f,np.fft.fftshift(RFdB_R),'#f24738', label='Ventana Rectangular')
#Gráfico de la respuesta en frecuencia de la ventana rectangular
plt.legend()
plt.axis([-np.pi/32, np.pi/32, -80, 0])
plt.title("Respuesta en frecuencia ")
plt.ylabel("Amplitud [dB]")
plt.xlabel("Frecuencia angular ω [Rad/s]")
plt.xticks([-np.pi/32, 0, np.pi/32], ['-π/32','0', 'π/32'])
plt.grid('both')
plt.show()
