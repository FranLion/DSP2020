from Funcionestp2 import *

eps=0.001

fs=44100

T=1/fs

n_samples=fs*2

pa=1/2

f1=220

p1=fs/f1

N= int(np.floor(fs/f1 -pa-eps))

pc=p1-N-pa

c=(1-pc)/(1+pc)

Q=0.1


def IIRdelbueno(senal,a,N):
    delayline=np.zeros(N)
    x=np.append(senal,delayline)
    y=np.zeros_like(x)
    for i in range(len(x)):
        y[i]=(1-a)*x[i]+a*delayline[N-1]
        delayline=np.append(y[i],delayline[0:N-1])
    return y

Karpluscuerda = karplus_strong(n_samples,1,N)

K

Karesult = Karpluscuerda -Q*Karpluscuerda

# y0=IIRdelbueno(Karpluscuerda,RL0,1)
# y1=IIRdelbueno(Karpluscuerda,RL1,1)
# y2=IIRdelbueno(Karpluscuerda,RL2,1)
# y3=IIRdelbueno(Karpluscuerda,RL3,1)
# y4=IIRdelbueno(Karpluscuerda,RL4,1)
# y5=IIRdelbueno(Karpluscuerda,RL5,1)
# y6=IIRdelbueno(Karpluscuerda,RL6,1)

sf.write('RL0.wav',y0,fs)
sf.write('RL1.wav',y1,fs)
sf.write('RL2.wav',y2,fs)
sf.write('RL3.wav',y3,fs)
sf.write('RL4.wav',y4,fs)
sf.write('RL5.wav',y5,fs)
sf.write('RL6.wav',y6,fs)

# ffty=np.fft.fft(y0)
# fdB=20*np.log10(abs(ffty))
# fase1=np.angle(ffty)

# fase2=np.angle(fftz2)
# plt.plot(fdB[0:2500])

# plt.plot(fdB)
# plt.plot(fdB[0:int(fs/2)])
# plt.show()
