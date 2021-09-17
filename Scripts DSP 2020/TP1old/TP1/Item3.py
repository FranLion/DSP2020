from FuncionesTP import *

'''En este ejercicio se generan 3 señales, cada una compuesta por la señal del Item 1 "data" más un ruido añadido(con sigma 0.1, 1 y 3 respectivamente). Finalmente se imprimen los resultado del SNR calculado para cada señal. '''

# Se generan los 3 ruidos y se añaden a la señal original.
ruido01 = np.random.normal(0, 0.1,len(data))
ruido1 = np.random.normal(0, 1, len(data))
ruido3 = np.random.normal(0, 3, len(data))
x01 = data + ruido01
x1 = data + ruido1
x3 = data + ruido3
# Se normalizan las señales generadas utilizando la función "normalizar" definida en FuncionesTP.py
x01=normalizar(x01)
x1=normalizar(x1)
x3=normalizar(x3)
# Se calculan los valores de SNR para cada señales a través de funciones de nuestro módulo de funciones.
SNR1=np.max(x01)/desvioestandar(ruido01,lamedia(ruido01))
SNR2=np.max(x1)/desvioestandar(ruido1,lamedia(ruido1))
SNR3=np.max(x3)/desvioestandar(ruido3,lamedia(ruido3))
# Se presentan los resultados.
print("SNR de la señal x01: ",SNR1)
print("SNR de la señal x1: ",SNR2)
print("SNR de la señal x3: ",SNR3)

#Gráficos
plt.figure('Item 3')
plt.subplot(3,1,1)
plt.plot(x01,'#e52121')
plt.grid('both')
plt.title('Señal x01')
plt.xlabel('Muestras [n]')
plt.ylabel('Amplitud')
plt.subplot(3,1,2)
plt.plot(x1,'#604444')
plt.grid('both')
plt.title('Señal x1')
plt.xlabel('Muestras [n]')
plt.ylabel('Amplitud')
plt.subplot(3,1,3)
plt.plot(x3,'#e35d6a')
plt.title('Señal x3')
plt.xlabel('Muestras [n]')
plt.ylabel('Amplitud')
plt.grid('both')
plt.subplots_adjust(hspace = 1.2)
plt.show()
