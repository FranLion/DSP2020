from FuncionesTP import *

señal,n,fs=senalTP() #Importo la señal sinusoidal definida en el Item 1.
L=int(0.01*len(señal)) #Asignacion de largo de 1% para la ventana
Largo=len(señal)
ri_MM=np.ones(L)/(L) #Respuesta al impulso del FMM de largo igual al 1% del largo de la señal.
sFMM=np.convolve(señal,ri_MM) #FMM a través de convolución lineal.
sfd=mediamovild(señal,L-1) #Aplicar la función de media movil directa
sfr=mediamovildr(señal,L-1) #Aplicar la función de media movil recursiva

#Normalización
sfd_norm=sfd/max(sfd) #Directa
sfr_norm=sfr/max(sfr) #Recursiva
sFMM_norm=sFMM/max(sFMM) #Convolución lineal

#Gráficos
t=np.arange(0,Largo) #Vector de muestras
sp1=plt.figure('Item 6')
plt.subplot(3,1,1)
plt.plot(t[int(Largo/64):int(Largo/48)],sfd_norm[int(Largo/64):int(Largo/48)],'#738EB6')
#Grafico normalizado de la señal filtrada con la media movil directa
plt.title('Señal filtrada con media movil directa')
plt.grid('both')
plt.ylabel('Señal x[n]')
plt.xlabel('Número de muestra [n]')
plt.subplot(3,1,2)
plt.plot(t[int(Largo/64):int(Largo/48)],sfr_norm[int(Largo/64):int(Largo/48)],'#BF76D2')
#Grafico normalizado para la señal filtrada con la media movil recursiva
plt.title('Señal filtrada con media movil recursiva')
plt.grid('both')
plt.ylabel('Señal x[n]')
plt.xlabel('Número de muestra [n]')
plt.subplot(3,1,3)
plt.plot(t[int(Largo/64):int(Largo/48)],sFMM_norm[int(Largo/64):int(Largo/48)],'#e0503f')
#Grafico normalizado para la señal filtrada con la convolución lineal
plt.title('Señal filtrada a traves de convolución')
plt.grid('both')
plt.ylabel('Señal x[n]')
plt.xlabel('Número de muestra [n]')
plt.subplots_adjust(hspace = 1.2)
plt.show()
