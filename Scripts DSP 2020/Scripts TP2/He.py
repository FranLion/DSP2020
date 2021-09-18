from Funcionestp2 import *

fs=44100
p1=55
p2=20

sample1 = karplus_strong(1*fs, 1 ,p1 ,fs)

sample2 = karplus_strong(3*fs, 0.707 ,p2 ,fs)

he_s1,n=He(sample1,21,fs)
# sf.write('karputo.wav', sample1, fs)
sf.write('karputoHe.wav', he_s1, fs)

sp1=plt.figure('Karputo')
plt.subplot(2,1,1)
plt.plot(sample1,'#738EB6')
plt.title('Señal generada por la cuerda')
plt.grid('both')
plt.ylabel('Amplitud relativa [n]')
plt.xlabel('Número de muestra [n]')
plt.subplot(2,1,2)
plt.plot(he_s1,'#BF76D2')
plt.title('Señal generada por la percusión')
plt.grid('both')
plt.ylabel('Amplitud relativa [n]')
plt.xlabel('Número de muestra [n]')
plt.subplots_adjust(hspace = 1.2)
plt.show()
