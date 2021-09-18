from Funcionestp2 import *

fs=44100

p1 = 55

p2 = 20

n_samples=3*fs

Karpluscuerda = karplus_strong(n_samples, 1 ,p1 ,fs)

Karpluspercusivo = karplus_strong(n_samples, 0.707 ,p2 ,fs)

sf.write('karpluscuerda.wav', sample1, fs)
sf.write('karpluspercusivo.wav', sample2, fs)

#Plots

sp1=plt.figure('Punto 3')
plt.subplot(2,1,1)
plt.plot(sample1,'#738EB6')
plt.title('Señal generada por la cuerda')
plt.grid('both')
plt.ylabel('Amplitud relativa [n]')
plt.xlabel('Número de muestra [n]')
plt.subplot(2,1,2)
plt.plot(sample2,'#BF76D2')
plt.title('Señal generada por la percusión')
plt.grid('both')
plt.ylabel('Amplitud relativa [n]')
plt.xlabel('Número de muestra [n]')
plt.subplots_adjust(hspace = 1.2)
plt.show()
