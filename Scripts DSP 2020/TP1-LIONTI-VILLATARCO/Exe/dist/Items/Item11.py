from FuncionesTP import *

'''En este Script se busca estudiar la convolución de las señales de audio importadas 'Midi69.wav' y 'RIR.wav' mediante el algoritmo de la DFT. Para ello se comparan los resultados de la convolución lineal, la convolución circular tomando el largo de la señal RIR y la convolución circular equivalente a la lineal. '''

cLineal=FFT_convLineal(Midi69,RIR) #Convolución lineal mediante FFT.
cCirc,nc=FFT_cConv(Midi69,nMidi,RIR,nRIR,2) #Convolución circular tomando el largo de la señal RIR(señal N°2) mediante FFT.
cCircular,nconv=FFT_convCircular(Midi69,nMidi,RIR,nRIR) #Convolución circular equivalente a convolución lineal mediante FFT.

#Gráficos
sp1=plt.figure('Item 11: Comparación de convoluciones con DFT')
plt.subplot(3,1,1)
plt.plot(cLineal,'#738EB6')
# Gráfico de la convolución lineal y[n]= Midi69*RIR.
plt.title('Convolución lineal')
plt.grid('both')
plt.ylabel('y[n]')
plt.xlabel('Número de muestras [n]')
sp1=plt.subplot(3,1,2)
plt.plot(nconv,cCircular,'#BF76D2')
#Gráfico de la convolución circular y[n]= Midi69*RIR equivalente a la lineal.
plt.title('Convolución circular equivalente a lineal')
plt.grid('both')
plt.ylabel('y[n]')
plt.xlabel('Número de muestras [n]')
sp1=plt.subplot(3,1,3)
plt.plot(nc,cCirc,'#e0503f')
#Gráfico de la convolución circular y[n]= Midi69*RIR de largo igual a la señal RIR.
plt.title('Convolución circular con largo RIR')
plt.grid('both')
plt.ylabel('y[n]')
plt.xlabel('Número de muestras [n]')
plt.subplots_adjust(hspace = 1.2)
plt.show()
