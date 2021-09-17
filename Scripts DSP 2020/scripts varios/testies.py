import matplotlib.pyplot as plt
import numpy as np
import math
import heapq
import time
import soundfile as sf
from convolucion import *
from scipy import signal

# mu = 3
# variance = 2
# sigma = math.sqrt(variance)
# x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
# plt.plot(x, stats.norm.pdf(x, mu, sigma))
# plt.show()

# def mediamovild(x,M,defas):
#     # for i in range(len(x)):
#     cumsum = np.cumsum(np.insert(x,M,defas))
#     salida = (cumsum[M:]- cumsum[:-M])/float(M)
#     # salida[i]=np.cumsum(M)
#     return salida
#     # return cumsum / float(M)
# mmd=mediamovild(data,3,3)

'''
Cosas para el punto 1

for i in range(0, len(data)):

    data[i] = int(data[i])

print ("\n")

print("La lista ingresada es: ",data)

print ("\n")

rmsdata = data

for i in range(0, len(rmsdata)):

    rmsdata[i] = abs(rmsdata[i])**2

## definicion de funciones:

def lamedia(input):
    # return np.sum(input)/(len(input))
    return st.mean(input)

def desviomedio(input,media):
    # return np.sum(abs(input-media))/(len(input))
    return st.median(input)

def desvioestandar(input,media):
    # return (np.sum(abs(input-media)**2)/len(input))**1/2
    return st.stdev(input)

def rms(input):
    # return (np.sum(input)/len(input))**1/2
    return (st.mean(input))**1/2

'''

def mediamovild(x,M):
    y=np.zeros(len(x))
    aux=np.append(x,np.zeros(M))
    for i in range(len(x)):
        for j in range(0,M+1):
            y[i]=y[i]+aux[i+j]
        y[i]=y[i]*(1/(M+1))
    return y

# xfd=mediamovild(data,50)

# print("La media movil es: ",xfd)

def mediamovildr(x,M):
    y=np.zeros(len(x))
    y[0]=(1/(M+1))*np.sum(x[:M+1])
    aux=np.append(x,np.zeros(M))
    for i in range(1,len(x)):
        y[i]=y[i-1]+(1/(M+1))*aux[i+M]-(1/(M+1))*aux[i-1]
    return y

    #xfr=mediamovildr(data,50)
#
# print("mmd recursiva: ", xfr)

# F = 10000
#
# T = 1/F
#
# Fs = 44100
#
# Ts = 1/Fs
#
# t = np.arange(0,0.5*T,Ts)
#
# señal = 2 + np.sin(2*np.pi*F*t)
#
# señalfft = np.fft.fft(señal)
#
# print("fft: ",señalfft)
#
# plt.plot(t,señalfft)
#
# plt.show()

fs = 44100
t = 0.5
n=np.arange(0,t,1/fs) #vector de muestras
N = len(n)
x=2 + np.sin(2*np.pi*10000*n) #defino funcion sen(2pi*f*t)
X=np.fft.fft(x) #calculo de la dft
Xr=np.fft.rfft(x)
Xmax=max(X)

# cont=0
# while X>=10000:
#     cont=cont+1
#     maximos[cont]=X[cont]

X1=abs(X) #tomo el modulo
w0=10000*np.pi/22050
M=16
w=np.arange(-1*np.pi,np.pi,2*np.pi/22050)
print('tuco: ',len(w))
H=abs((1/(M+1))*((np.sin(w*(M+1)/2))/(np.sin(w/2))))

M=int(0.01*len(x))
# Comparación de tiempos de ejecución de ambas funciones.
t = time.time()  # Iniciar tiempo.
xfd=mediamovild(x,M)  # Ejecutar función.
tiempo_d = time.time()-t  # Calcular tiempo de ejecucion total.

t = time.time()  # Iniciar tiempo.
xfr= mediamovildr(x,M)  # Ejecutar función.
tiempo_r = time.time()-t  # Calcular tiempo de ejecucion total.

print(f"Directo: {round(tiempo_d,3)}, Recursiva: {round(tiempo_r,3)}")
tucardo=heapq.nlargest(5,X1)
FFTd=abs(np.fft.fft(xfd))
tuco=heapq.nlargest(5,FFTd)
FFTr=abs(np.fft.fft(xfr))
ventanilla=signal.windows.boxcar(M+1)/(M+1)
xfc=np.convolve(x,ventanilla)
FFTc=abs(np.fft.fft(xfc))
print("maximos de conv",heapq.nlargest(5,FFTc) )
print("largo", len(xfc))
tuco1=heapq.nlargest(5,FFTr)
print(tuco)
print(tuco1)
print(tucardo)
f = np.arange(0,fs/2,(fs/2)/int(N/2))
plt.figure(1)
plt.plot(f,X1[0:int(N/2)])
plt.show()

'''Ejercicio 6'''
M=int(0.01*len(x))
ri_MM=np.ones(M+1)/(M+1)
xMM=np.convolve(x,ri_MM)
FFT_MM=abs(np.fft.fft(xMM))
tuco2=heapq.nlargest(5,FFT_MM)
print(tuco2)
f = np.arange(0,fs/2,(fs/2)/int(N/2))
''' Aca viene todo el mambo de la normalización que nose como hacer '''
# xfd_norm=xfd/np.linalg.linalg.norm(xfd)
# xfr_norm=xfr/np.linalg.linalg.norm(xfr)
# xMM_norm=xMM/np.linalg.linalg.norm(xMM)
# print(np.linalg.linalg.norm(xfd))
xfd_norm=xfd/max(xfd)
xfr_norm=xfr/max(xfr)
xMM_norm=xMM/max(xMM)
print(np.linalg.linalg.norm(xfd))
figure,axis = plt.subplots(3)
axis[0].plot(xfd_norm[0:M])
axis[1].plot(xfr_norm[0:M])
axis[2].plot(xMM_norm[0:M])
plt.show()
#
# '''Ejercicio 7'''
# m=np.arange(M-1)
# blackman=0.42 - ((0.5)*np.cos((2*np.pi*m)/(M-1))) + ((0.08)*np.cos((4*np.pi*m)/(M-1)))
# xBlack=np.convolve(x,blackman)
# print(len(xBlack))
# # figure,axis = plt.subplots(3)
# # axis[0].plot(xfd_norm[0:M])
# # axis[1].plot(xfr_norm[0:M])
# # axis[2].plot(xBlack[0:M])
# # plt.show()
#
# '''Ejercicio 8 '''
# '''
# revisar aca la convolucion
# '''
# [RIR,Fs] = sf.read("RIR.wav")
# [Midi69,Fs1] = sf.read("Midi69.wav")
# L=len(Midi69)
# K=len(RIR)
# cLineal=np.convolve(Midi69,RIR)
# cCirc=np.convolve(Midi69[:K],RIR)
# cCircular=convCirc(Midi69,RIR)
# sf.write('RIR.wav', RIR, Fs)
# sf.write('Midi69.wav', RIR, Fs1)
# figure,axis = plt.subplots(3)
# axis[0].plot(cLineal)
# axis[1].plot(cCircular)
# axis[2].plot(cCirc)
# plt.show()
#
# """
# escribir los archivos wav
#
# """
#
# '''Ejercicio 9 '''
# plt.figure(1)
# plt.plot(w,H)
# plt.show()
#
# '''Ejercicio 10'''
# T=1000
# f= np.linspace(-1*np.pi,np.pi,T)
# rect=signal.windows.boxcar(T)
# black2=np.blackman(T)
# # RF_rectang=abs(np.sin(f*T/2)/np.sin(f/2))
# RF_rectang=abs(np.fft.fft(rect))
# RF_blackman=abs(np.fft.fft(black2))
# RFdB_r=np.clip(20*np.log10(np.fft.fftshift(RF_rectang)),-100,100)
# RFdB_B=np.clip(20*np.log10(np.fft.fftshift(RF_blackman)),-100,100)
# '''Arreglar grafico'''
# plt.figure(1)
# # plt.plot(f,RFdB_B)
# # plt.plot(f,RFdB_r)
# plt.grid()
# plt.plot(f,RFdB_B,'g')
# plt.plot(f,RFdB_r,'b')
# plt.show()
#
# '''Ejercicio 11'''
# cLineal_fft=convLin(Midi69,RIR)
# cCirc=convLin(Midi69[:K],RIR)
# cCircular=convCirc(Midi69,RIR)
# figure,axis = plt.subplots(3)
# axis[0].plot(cLineal)
# axis[1].plot(cCircular)
# axis[2].plot(cCirc)
# plt.show()
