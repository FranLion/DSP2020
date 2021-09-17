import matplotlib.pyplot as plt
import numpy as np
import math
import heapq
import time
import soundfile as sf
from convolucion import *
from scipy import signal

''' Definimos las funciones que se utilizan en el programa. '''

def lamedia(input):
    mu=np.sum(input)/(len(input))
    return mu

def desviomedio(input,media):
    d=np.sum(abs(input-media))/(len(input))
    return d

def desvioestandar(input,media):
    sigma=((np.sum(abs(input-media)**2))/(len(input)))**(1/2)
    return sigma

def rms(input):
    rms=((np.sum(abs(input**2)))/(len(input)))**(1/2)
    return rms

#Generar ruido
def normalizar(input):
    media=lamedia(input)
    desviacion=desvioestandar(input,media)
    for i in range(len(input)):
        input[i]=(input[i]-media)/desviacion
    return input

def SNR(señal,ruido):
    media=lamedia(señal)
    sigmanoise=desvioestandar(ruido,lamedia(ruido))
    SNR=media/sigmanoise
    return SNR

def senales_con_ruido(senal,mu,sigma,N):
''' Genera señales con ruido, hace el promedio en ensamble y devuelve el SNR de la señal promediada y el sigma de los ruidos promedios'''
    ruidos=np.zeros(len(senal))
    senales_ruido=np.zeros(len(senal))
    for i in range(0,N):
        ruido=np.random.normal(mu, sigma, len(senal))
        senales_ruido=senal+ruido+senales_ruido
        ruidos=ruidos+ruido
    promsenal=senales_ruido*(1/N)
    promruido=ruidos*(1/N)
    media=lamedia(promsenal)
    sigma=desvioestandar(promruido)
    SNR=media/sigma
    return SNR, sigma

def mediamovild(x,M):
    y=np.zeros(len(x))
    aux=np.append(x,np.zeros(M))
    for i in range(len(x)):
        for j in range(0,M+1):
            y[i]=y[i]+aux[i+j]
        y[i]=y[i]*(1/(M+1))
    return y

def mediamovildr(x,M):
    y=np.zeros(len(x))
    y[0]=(1/(M+1))*np.sum(x[:M+1])
    aux=np.append(x,np.zeros(M))
    for i in range(1,len(x)):
        y[i]=y[i-1]+(1/(M+1))*aux[i+M]-(1/(M+1))*aux[i-1]
    return y

def plotear(**kwargs):
figure,axis = plt.subplots(3)
axis[0].plot(cLineal)
axis[1].plot(cCircular)
axis[2].plot(cCirc)
plt.show()
