from FuncionesTP import *

#Generar señales
L=int(0.01*len(señal)) #Tomar el largo de 1% de la señal
Largo=len(señal)
blackman=wBlackman(L)
sBlack=np.convolve(señal,blackman) #Aplicar la convolución lineal entre la señal y la ventana Blackman
sfd=mediamovild(señal,L) #Aplicar media movil directa
sfr=mediamovildr(señal,L) #Idem recursiva

#Normalizaciones
sfd_norm=sfd/max(sfd)
sfr_norm=sfr/max(sfr)
sBlack_norm=sBlack/max(sBlack)
FFT_Black=abs(np.fft.fft(sBlack))
f = np.arange(0,fs/2,(fs/2)/int(len(t)/2))

#Gráficos
figure=plt.figure('Item 7')
plt.subplot(3,1,1)
plt.plot(sBlack_norm[8000:8150],color='#1c8b82')
# Gráfico del filtrado provocado por la convolución entre la señal y la ventana de largo L
plt.yticks([0.9998,0.9999,1])
plt.title('Ventana Blackman normalizada')
plt.xlabel('Muestras [n]')
plt.ylabel('xfb [n]')
plt.grid('both')
plt.subplot(3,1,2)
plt.plot(sfd_norm[8000:8150],color='#553E4E')
# Gráfico del filtrado generado por la media movil directa
plt.title('Media movil directa')
plt.xlabel('Muestras [n]')
plt.ylabel('xfd [n]')
plt.grid('both')
plt.subplot(3,1,3)
plt.plot(sfr_norm[8000:8150],color='#7e093e')
# Gráfico del filtrado generado por la media movil recursiva
plt.title('Media movil recursiva')
plt.ylabel('xfr [n]')
plt.xlabel('Muestras [n]')
plt.subplots_adjust(hspace = 1.2)
plt.grid('both')
plt.show()
