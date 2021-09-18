from Funcionestp2 import *

eps=0.001

fs=44100

T=1/fs

n_samples=fs*2

pa=1/2

f1=10
f2=250
f3=500
f4=1000
f5=5000

p1=fs/f1

N= int(np.floor(p1 -pa-eps))

a1=2*(abs(np.cos(2*np.pi*f1)+1))**-1
# a2=2*(abs(np.cos(2*np.pi*f2)+1))**-1
# a3=2*(abs(np.cos(2*np.pi*f3)+1))**-1
# a4=2*(abs(np.cos(2*np.pi*f4)+1))**-1
# a5=2*(abs(np.cos(2*np.pi*f5)+1))**-1

def delayhc(senal,d,a,N):
    # d=int(round(t*fs))
    delay=np.zeros((N,len(senal)+(N*d)))
    x=np.append(senal,np.zeros(N*d))
    y=np.zeros_like(x)
    dly=np.zeros_like(x)
    for i in range(0,N):
        D=(i+1)*d
        zpad=np.zeros(D)
        aux=np.append(zpad,senal)
        delay[i]=np.append(aux,np.zeros(len(x)-len(aux)))
        dly=delay[i]+dly #x[n-D]
    y=a*(x+dly)
    return y

cuerda=karplus_strong(n_samples,1,N)

z1=delayhc(cuerda,2,a1,N)
# z2=delayhc(cuerda,2,a2,N)
# z3=delayhc(cuerda,2,a3,N)
# z4=delayhc(cuerda,2,a4,N)
# z5=delayhc(cuerda,2,a5,N)

sf.write('cuerdac.wav',cuerda,fs)
sf.write('Hc1.wav',z1,fs)
# sf.write('Hc2.wav',z2,fs)
# sf.write('Hc3.wav',z3,fs)
# sf.write('Hc4.wav',z4,fs)
# sf.write('Hc5.wav',z5,fs)

fftz1=np.fft.fft(z1)
# fftz2=np.fft.fft(z2)
fdB=20*np.log10(abs(z1))
fase1=np.angle(fftz1)
# fase2=np.angle(fftz2)
# plt.plot(fdB[0:2500])

plt.subplot(2,1,1)
plt.plot(cuerda,'#738EB6')
plt.title('Señal generada por la cuerda')
plt.grid('both')
plt.ylabel('Amplitud relativa [n]')
plt.xlabel('Número de muestra [n]')
plt.subplot(2,1,2)
plt.plot(fdB,'#BF76D2')
plt.title('El deca papa')
plt.grid('both')
plt.ylabel('Amplitud relativa [n]')
plt.xlabel('Número de muestra [n]')
plt.subplots_adjust(hspace = 1.2)

plt.show()
