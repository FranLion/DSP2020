import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf

[m69,Fs] = sf.read("Cosas/Midi69.wav")
d=0.5 #segundos
D=int(round(d*Fs))
zpad=np.zeros(D)
delay=np.append(zpad,m69)
a=(2**(1/2))/2


x=np.append(m69,zpad)
n=np.arange(0,len(x))
y=x+a*delay
y-a*delay=x


ny=np.arange(0,len(y))
# print(f"D={D}, señal= {len(m69)}, delay={len(delay)}, x={len(x)}, y={len(y)}")

# sf.write('Midi69+delay.wav', y, Fs)
plt.figure()
plt.plot(n,x,'b',ny,a*delay,'r')
plt.show()
plt.figure()
plt.plot(ny,y)
plt.show()




sf.write('mecho.wav', y, Fs)
