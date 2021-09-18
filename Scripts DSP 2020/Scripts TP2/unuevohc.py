from Funcionestp2 import *

fs=44100

C1=0.9

C2=0.9

p=100

n_samples=fs*2


def delay1(senal,a1,a2):
    zpad=np.zeros(1)
    delay=np.append(zpad,senal)
    x=np.append(senal,zpad)
    y=a1*x+a2*delay
    return y

cuerda=karplus_strong(n_samples,1,p,fs)

# x1,z1,dly1=delays(cuerda,1,C1,1,1)
#
# x2,z2,dly2=delays(cuerda,1,C2,1,1)

z1=delay1(cuerda,C1,1)
z2=delay1(cuerda,C1,1)

k1,y1,delayline1=IIR_delay(z1,-C1,1)

k2,y2,delayline2=IIR_delay(z2,-C2,1)

sf.write('HaHbHc.wav',cuerda,fs)
sf.write('HaHbHc1.wav',y1,fs)

sf.write('HaHbHc2.wav',y2,fs)

fftz1=np.fft.fft(z1)
fdB=20*np.log10(abs(fftz1))
fase=np.angle(fftz1)

plt.plot(fdB[0:2500])

# plt.subplot(2,1,1)
# plt.plot(y1,'#738EB6')
# plt.title('Señal generada por la cuerda')
# plt.grid('both')
# plt.ylabel('Amplitud relativa [n]')
# plt.xlabel('Número de muestra [n]')
# plt.subplot(2,1,2)
# plt.plot(y2,'#BF76D2')
# plt.title('Señal generada por la cuerda 2')
# plt.grid('both')
# plt.ylabel('Amplitud relativa [n]')
# plt.xlabel('Número de muestra [n]')
# plt.subplots_adjust(hspace = 1.2)

plt.show()
