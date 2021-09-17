import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from Func import *
''' Diseña un filtro pasa bajos FIR de fase lineal generalizada para distintas tipos de ventanas'''

def BS_fir(Ap,As,wp1,ws1,wp2,ws2,FS,id_window):
    ''' Datos'''
    Gp=20*np.log10(Ap)
    Gs=20*np.log10(As)
    wc1=(wp1+ws1)/2
    deltaw1=round(ws1-wp1,3)
    wc2=(wp2+ws2)/2
    deltaw2=round(wp2-ws2,3)
    deltaw=min(deltaw1,deltaw2)
    hfir=[]
    n=[]
    M=0
    tipo="Ventana"
    if id_window==1:#Rectangular
        M=int((4/deltaw)-1)
        h,n=iBS(M,wc1,wc2)
        wind=signal.windows.boxcar(M+1)
        hfir=h*wind
        tipo="Rectangular"
    elif id_window==2:#Barlett
        M=int(8/deltaw)
        h,n=iBS(M,wc1,wc2)
        wind=signal.windows.bartlett(M+1)
        hfir=h*wind
        tipo="Barlett"
    elif id_window==3:#Hanning
        M=int(8/deltaw)
        h,n=iBS(M,wc1,wc2)
        wind=signal.windows.hann(M+1)
        hfir=h*wind
        tipo="Hanning"
    elif id_window==4:#Hamming
        M=int(8/deltaw)
        h,n=iBS(M,wc1,wc2)
        wind=signal.windows.hamming(M+1)
        hfir=h*wind
        tipo="Hamming"
    elif id_window==5:#Blackman
        M=int(12/deltaw)
        h,n=iBS(M,wc1,wc2)
        wind=signal.windows.blackman(M+1)
        hfir=h*wind
        tipo="Blackman"
    elif id_window==6:#Kaiser
        A=-Gs
        M=Kaiser_M(A,deltaw)
        beta=beta_K(A)
        h,n=iBS(M,wc1,wc2)
        wind=signal.windows.kaiser(M+1,beta)
        hfir=h*wind
        tipo=f"Kaiser(beta={round(beta,5)})"
    else: print("Opción incorrecta, ingresa entre 1 y 6.")
    '''Resultados'''
    HFIL=np.fft.fft(hfir,FS)
    faseFIL=np.angle(HFIL)
    HFIR=20*np.log10(abs(HFIL))
    freq=np.arange(0,1,1/int(FS/2))
    iwp1=np.where(np.float64(freq)==wp1)
    iws1=np.where(np.float64(freq)==ws1)
    iwp2=np.where(np.float64(freq)==wp2)
    iws2=np.where(np.float64(freq)==ws2)
    print(f"Ventana: {tipo}, M={M}, wc1={wc1}, wc2={wc2} , deltaw={deltaw}")
    print(f"Gp1={HFIR[iwp1]}")
    print(f"Gs1={HFIR[iws1]}")
    print(f"Gp2={HFIR[iwp2]}")
    print(f"Gs2={HFIR[iws2]}")

    '''Graficos'''
    plt.figure()
    plt.subplot(311)
    plt.plot(freq,HFIR[0:int(FS/2)],'b')
    plt.xlabel('w')
    plt.ylabel('|H(jw)|')
    plt.subplot(312)
    plt.plot(freq,faseFIL[0:int(FS/2)],'r')
    plt.xlabel('w')
    plt.ylabel('<H(jw')
    plt.subplot(313)
    plt.plot(freq,(M/2)*np.ones(len(freq)),'g')
    plt.xlabel('w')
    plt.ylabel('RG(H(jw))')
    plt.axis([0,1,(M/2)-0.5,(M/2)+0.5])
    plt.subplots_adjust(hspace = 0.9)
    plt.show()
