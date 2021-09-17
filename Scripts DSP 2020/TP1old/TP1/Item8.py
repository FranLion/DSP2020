from FuncionesTP import *

'''En este Script se busca estudiar la convolución de las señales de audio importadas 'Midi69.wav' y 'RIR.wav'.
Para ello se comparan los resultados de la convolución lineal, la convolución circular tomando el largo de la señal RIR y
la convolución circular equivalente a la lineal. Finalmente se exportan los resultados en archivos .wav. '''

#En esta sección se calculan las convoluciones pedidas en la consigna.

cLineal=np.convolve(Midi69,RIR) #Convolución lineal
cCirc,nc=cConv(Midi69,nMidi,RIR,nRIR,2) #Convolución circular tomando el largo de la señal RIR(señal N°2)
cCircular,nconv=convCircular(Midi69,nMidi,RIR,nRIR) #Convolución circular equivalente a convolución lineal.

#Se escriben los archivos .wav para cada señal obtenida.
# sf.write('cLinealout.wav', cLineal, Fs)
# sf.write('cCircout.wav', cCirc, Fs)
# sf.write('cCircularout.wav', cCircular, Fs)

#Se grafican los resultados.
sp1=plt.figure('Item 8: Comparación de convoluciones')
plt.subplot(3,1,1)
plt.plot(cLineal,'#738EB6')
# Gráfico de la convolución lineal y[n]= Midi69*RIR.
plt.title('Convolución lineal')
plt.grid('both')
plt.ylabel('y[n]')
plt.xlabel('Número de muestras [n]')
sp1=plt.subplot(3,1,2)
plt.plot(nconv,cCircular,'#BF76D2')
# Grafico de la convolución circular y[n]= Midi69*RIR equivalente a la lineal.
plt.title('Convolución circular equivalente a lineal')
plt.grid('both')
plt.ylabel('y[n]')
plt.xlabel('Número de muestras [n]')
sp1=plt.subplot(3,1,3)
plt.plot(nc,cCirc,'#e0503f')
# Gráfico de la convolución circular y[n]= Midi69*RIR de largo igual a la señal RIR.
plt.title('Convolución circular con largo RIR')
plt.grid('both')
plt.ylabel('y[n]')
plt.xlabel('Número de muestras [n]')
plt.subplots_adjust(hspace = 1.2)
plt.show()
