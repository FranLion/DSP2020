from Funcionestp2 import *

eps=0.001

fs=44100

T=1/fs

n_samples=fs*2

pa=1/2

f1=220

p1=fs/f1

N= int(np.floor(p1 -pa-eps))

pc=p1-N-pa

C=(1-pc)/(1+pc)

# p=100

# def delay1(senal,a1,a2):
#     zpad=np.zeros(1)
#     delay=np.append(zpad,senal)
#     x=np.append(senal,zpad)
#     y=a1*x+a2*delay
#     return y
#
cuerda=karplus_strong(n_samples,1,N)
#
# # x1,z1,dly1=delays(cuerda,1,C1,1,1)
# #
# # x2,z2,dly2=delays(cuerda,1,C2,1,1)
#
# z1=delay1(cuerda,C,1)
# z2=delay1(cuerda,C,1)
#
# k1,y1,delayline1=IIR_delay(z1,-C,1)
#
# # k2,y2,delayline2=IIR_delay(z2,-C2,1)
#
# sf.write('HaHbHc.wav',cuerda,fs)
# sf.write('HaHbHc1.wav',y1,fs)
#
# # sf.write('HaHbHc2.wav',y2,fs)
#
# fftz1=np.fft.fft(z1)
# fftz2=np.fft.fft(z2)
# # fdB=20*np.log10(abs(fftz1))
# fase1=np.angle(fftz1)
# fase2=np.angle(fftz2)
# plt.plot(fdB[0:2500])
mu1=1/100
mu2=0.3
mu3=0.5
mu4=0.707
mu5=1/N
y1=He(cuerda,mu1,N)
y2=He(cuerda,mu2,N)
y3=He(cuerda,mu3,N)
y4=He(cuerda,mu4,N)
y5=He(cuerda,mu5,N)

sf.write('mu1.wav',y1,fs)
sf.write('mu2.wav',y2,fs)
sf.write('mu3.wav',y3,fs)
sf.write('mu4.wav',y4,fs)
sf.write('mu5.wav',y5,fs)


#
# def el_estirador(senal,D,S) :
#
#     rho = 0.996
#     g0 = (1-S)*rho
#     g1 = S*rho
#
#     b = np.array([1.0]) # Zeros numerator coefficients
#     a = np.array([1.0] + ([0]*(D-3)) + [-g0, -g1]) # Poles denominator coefficients
#     samples = signal.lfilter(b,a,senal)
#
#     return samples,b,a
# D=int(44100/10000)
# S=0.707
# rho = 0.996
# g0 = (1-S)*rho
# g1 = S*rho


# plt.subplot(2,1,1)
# plt.plot(cuerda,'#738EB6')
# plt.title('Señal generada por la cuerda')
# plt.grid('both')
# plt.ylabel('Amplitud relativa [n]')
# plt.xlabel('Número de muestra [n]')
# plt.subplot(2,1,2)
# plt.plot(y1,'#BF76D2')
# plt.title('Señal generada por la cuerda 2')
# plt.grid('both')
# plt.ylabel('Amplitud relativa [n]')
# plt.xlabel('Número de muestra [n]')
# plt.subplots_adjust(hspace = 1.2)
#
# plt.show()
