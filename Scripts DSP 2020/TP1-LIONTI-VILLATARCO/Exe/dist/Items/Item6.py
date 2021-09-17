from FuncionesTP import *


L=int(0.01*len(señal))
Largo=len(señal)
ri_MM=np.ones(L)/(L) #Respuesta al impulso del FMM de largo igual al 1% del largo de la señal.
sFMM=np.convolve(señal,ri_MM) #FMM a través de convolución lineal.
sfd=mediamovild(señal,L)
sfr=mediamovildr(señal,L)
sfd_norm=sfd/max(sfd)
sfr_norm=sfr/max(sfr)
sFMM_norm=sFMM/max(sFMM)
#Se comparan los resultados en un gráfico
t=np.arange(0,Largo)
sp1=plt.figure('Item 6')
plt.subplot(3,1,1)
plt.plot(t[int(Largo/64):int(Largo/48)],sfd_norm[int(Largo/64):int(Largo/48)],'#738EB6')
plt.title('Señal filtrada con media movil directa')
plt.grid('both')
plt.ylabel('xfd [n]')
plt.xlabel('Número de muestra [n]')
plt.subplot(3,1,2)
plt.plot(t[int(Largo/64):int(Largo/48)],sfr_norm[int(Largo/64):int(Largo/48)],'#BF76D2')
plt.title('Señal filtrada con media movil recursiva')
plt.grid('both')
plt.ylabel('xfr [n]')
plt.xlabel('Número de muestra [n]')
plt.subplot(3,1,3)
plt.plot(t[int(Largo/64):int(Largo/48)],sFMM_norm[int(Largo/64):int(Largo/48)],'#e0503f')
plt.title('Señal filtrada a traves de convolución')#Para éste gráfico se observa que la fase de la señal ilustrada es levemente diferente al de las anteriores.
#Ésto puede atribuirse a que la operación de la convolución lineal agrega muestras debido a que de esta manera puede operar entre los vectores o matrices.
#Por ende el largo de la señal resultante se ve afectado.
plt.grid('both')
plt.ylabel('y [n]')
plt.xlabel('Número de muestra [n]')
plt.subplots_adjust(hspace = 1.2)
plt.show()
