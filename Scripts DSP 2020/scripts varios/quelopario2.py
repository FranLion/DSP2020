import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

'''Ejercicio 10'''
T=1000
f= np.linspace(-1,1,T)
rect=signal.windows.boxcar(T)
black2=np.blackman(T)
# RF_rectang=abs(np.sin(f*T/2)/np.sin(f/2))
RF_rectang=abs(np.fft.fft(rect))
RF_blackman=abs(np.fft.fft(black2))

with np.errstate(divide='ignore', invalid='ignore'):

    RFdB_r=np.clip(20*np.log10(abs(np.fft.fftshift(RF_rectang))),-200,100)
    RFdB_B=np.clip(20*np.log10(abs(np.fft.fftshift(RF_blackman))),-200,100)

max_RFdB_r=max(RFdB_r)
max_RFdB_B=max(RFdB_B)

RFdB_rn=RFdB_r/max_RFdB_r
RFdB_Bn=RFdB_B/max_RFdB_r

'''Arreglar grafico'''
plt.figure(1)
plt.grid()
plt.plot(f,RFdB_Bn,'g')
plt.plot(f,RFdB_rn,'b')
plt.show()
