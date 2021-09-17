import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from scipy import signal

'''
En el presente módulo se importan las librerías y se definen las variables y las funciones que se necesiten en distintos items.
'''

'''Definición de Variables Globales'''
#Definición de señal de entrada x[n]=data de longitud N=1000.(Items 1,2 y 4)
data=np.ones(1000)

#Definición de la señal senoidal x(t)= 2 + sen(2πft). (Items 1, 5, 6 y 7)
frec=10000
fs = 44100
duración = 0.5
t=np.arange(0,duración,1/fs) #vector de muestras
señal=2 + np.sin(2*np.pi*frec*t) #defino funcion sen(2pi*f*t)

#Importación de Archivos .wav (Item 8 y 11).
[RIR,Fs] = sf.read("Audio\RIR.wav")
[Midi69,Fs1] = sf.read("Audio\Midi69.wav")
nMidi=np.arange(0,len(Midi69))
nRIR=np.arange(0,len(RIR))

''' Definición de Funciones. '''
def senalTP():
    f=10000
    fs = 44100
    t = 0.5
    n=np.arange(0,t,1/fs) #vector de muestras
    señal=2 + np.sin(2*np.pi*f*n) #defino funcion sen(2pi*f*t)
    return señal,n,fs

def lamedia(input):
    #Defino la función del calculo de media
    mu=np.sum(input)/(len(input))
    return mu

def desviomedio(input,media):
    #Defino la función del cálculo del desvío medio
    d=np.sum(abs(input-media))/(len(input))
    return d

def desvioestandar(input,media):
    #Defino la función del cálculo del desvío estándar
    sigma=((np.sum(abs(input-media)**2))/(len(input)))**(1/2)
    return sigma

def rms(input):
    #Defino la función del cálculo de RMS
    rms=((np.sum(abs(input**2)))/(len(input)))**(1/2)
    return rms

def normalizar(input):
    # Función para normalizar la distribución de valores de una señal
    media=lamedia(input)
    desviacion=desvioestandar(input,media)
    for i in range(len(input)):
        input[i]=(input[i]-media)/desviacion
    return input

def calc_SNR(senal,ruido):
    #Calcula la relación señal/ruido (SNR) de una señal y ruido determinado.(Devuelve SNR y desvio estandar del ruido)
    media=lamedia(senal)
    sigmanoise=desvioestandar(ruido,lamedia(ruido))
    SNR=np.max(senal)/sigmanoise
    return SNR , sigmanoise

def senales_con_ruido(senal,mu,sigma,N):
    # Genera señales con ruido, hace el promedio en ensamble y devuelve el SNR de la señal promediada y el sigma del promedio de los ruidos.
    # (Utiliza la función calc_SNR)
    ruidos=np.zeros(len(senal))
    senales_ruido=np.zeros(len(senal))
    for i in range(0,N):
        ruido=np.random.normal(mu, sigma, len(senal))
        senales_ruido=senal+ruido+senales_ruido
        ruidos=ruidos+ruido
    promsenal=senales_ruido*(1/N)
    promruido=ruidos*(1/N)
    SNR , sigmanoise = calc_SNR(promsenal,promruido)
    return SNR, sigmanoise

def mediamovild(x,L):
    #Implementación directa del filtro media móvil de largo L a una señal x.
    M=L-1 #Según la definición utilizada para implementar el FMM el largo de la ventana es L=M+1
    y=np.zeros(len(x))#Asiganciones de espacios en memoria
    aux=np.append(x,np.zeros(M))
    #Media movil directa
    for i in range(len(x)):
        for j in range(0,M+1):
            y[i]=y[i]+aux[i+j]
        y[i]=y[i]*(1/(M+1)) #Divido por el largo L=M+1
    return y

def mediamovildr(x,L):
    #Implementación recursiva del filtro media móvil de largo L a una señal x.
    M=L-1 #Según la definición utilizada para implementar el FMM el largo de la ventana es M+1
    y=np.zeros(len(x))#Asiganciones de espacios en memoria
    y[0]=(1/(M+1))*np.sum(x[:M+1])
    aux=np.append(x,np.zeros(M))
    #Media movil recursiva
    for i in range(1,len(x)):
        y[i]=y[i-1]+(1/(M+1))*aux[i+M]-(1/(M+1))*aux[i-1] #Se divide por M+1 ya que este es el largo de ventana
    return y

def wBlackman(M):
    #Devuelve una ventana Blackman de largo M.
    a0=(7935/18608)#Se utilizan los valores exactos de los coeficientes
    a1=(9240/18608)
    a2=(1430/18608)
    m=np.linspace(0,M-1,M)
    blackman=a0 - ((a1)*np.cos((2*np.pi*m)/(M))) + ((a2)*np.cos((4*np.pi*m)/(M)))
    return blackman

def Importar_Audio(file,señal):
    #Importa archivos .wav. Devuelve la señal, la Frecuencia de sampleo y el vector de muestras(en ese orden).
    [señal,Fs] = sf.read(file)
    n=np.arange(0,len(señal))
    return señal,Fs,n

def convCircular(x1,nx1,x2,nx2):
    #Calcula la convolución circular de dos señales finitas x1 y x2 (largo L1 y L2, respectivamente),
    #de manera tal que el resultado sea equivalente al de la convolución lineal.
    #Para ello se realiza zero padding para que el resultado tenga un largo L=L1+L2-1.
    #Devuelve la convolución circular y el vector de muestras.(Permite señales no inicializadas en la posición 0)
    nny = np.arange(0,len(nx1)+len(nx2)-1) #Genero largo L=L1+L2-1
    ny = np.arange(0,len(x1)+len(x2)-1) + nx1[0] + nx2[0]
    y = np.convolve(x1, x2)
    return y[nny], ny

def cConv(x1,nx1,x2,nx2,l):
    #Calcula la convolución circular ("a secas") de dos señales x1 y x2 de largos L1 y L2, respectivamente.
    #Devuelve el resultado de largo L=L1 o L=L2, según indique la variable l, y el vector de muestras.
    if l==1:
        nny = np.arange(0,len(x1))
        ny = np.arange(0,len(x1)) + nx1[0] + nx2[0]
    elif l==2:
        nny = np.arange(0,len(x2))
        ny = np.arange(0,len(x2)) + nx1[0] + nx2[0]
    y = np.convolve(x1, x2)
    return y[nny], ny

def RF_boxcar(M,f):
    #Calcula la respuesta en frecuencia de la ventana rectangular de largo M.
    #(Recibe el vector de frecuencias f que ya tendrá una resolución dada por una frecuencia de sampleo determinada.)
    RF_rectang=(np.exp(-1j*((M-1)*f)/2))*(np.sin(f*M/2)/np.sin(f/2))
    return RF_rectang

def RF_Blackman(T,f):
    #Calcula analíticamente la respuesta en frecuencia de la ventana blackman de largo T.
    #(Recibe el vector de frecuencias f que ya tendrá una resolución dada por una frecuencia de sampleo determinada.)
    a0=(7935/18608)
    a1=(9240/18608)
    a2=(1430/18608)
    H0=(np.sin(f*T/2)/np.sin(f/2))
    H1=(np.exp(-1j*(np.pi)/T)*(np.sin((T*f/2)-np.pi)/np.sin((f-(2*np.pi/T))/2)))+((np.exp(1j*(np.pi)/T))*(np.sin((f+(2*np.pi/T))*T/2)/np.sin((f+(2*np.pi/T))/2)))
    H2=(np.exp(1j*(2*np.pi)/T)*(np.sin((f-(4*np.pi/T))*T/2)/np.sin((f-(4*np.pi/T))/2)))+(np.exp(1j*(2*np.pi)/T)*(np.sin((f+(4*np.pi/T))*T/2)/np.sin((f+(4*np.pi/T))/2)))
    RF_blackman=(np.exp(-1j*((T-1)*f)/2))*((a0*H0)-((a1/2)*H1)+((a2/2)*H2))
    return RF_blackman

def RFdB_ventanas(RF,T):
    #Devuelve una respuesta en frecuencia determinada y de largo T, en dB.
    resp =RF/(T/2.0)
    respN = np.abs(resp/abs(resp).max())
    RFdB = 20 * np.log10(np.maximum(respN, 1e-10))
    return RFdB

def FFT_convLineal(x1,x2):
    #Calcula la convolución lineal de dos señales mediante FFT.
    y=signal.signaltools.fftconvolve(x1,x2)
    return y

def FFT_convCircular(x1,nx1,x2,nx2):
    #Calcula la convolución circular usando FFT de dos señales finitas x1 y x2 (largo L1 y L2, respectivamente),
    #de manera tal que el resultado sea equivalente al de la convolución lineal.
    #Para ello se realiza zero padding para que el resultado tenga un largo L=L1+L2-1.
    #Devuelve la convolución circular y el vector de muestras.(Permite señales no inicializadas en la posición 0).
    nny = np.arange(0,len(nx1)+len(nx2)-1)
    ny = np.arange(0,len(x1)+len(x2)-1) + nx1[0] + nx2[0]
    y = signal.signaltools.fftconvolve(x1, x2)
    return y[nny], ny

def FFT_cConv(x1,nx1,x2,nx2,l):
    #Calcula la convolución circular usando FFT de dos señales x1 y x2 de largos L1 y L2, respectivamente.
    #Devuelve el resultado de largo L=L1 o L=L2, según indique la variable l, y el vector de muestras.
    if l==1:
        nny = np.arange(0,len(x1))
        ny = np.arange(0,len(x1)) + nx1[0] + nx2[0]
    elif l==2:
        nny = np.arange(0,len(x2))
        ny = np.arange(0,len(x2)) + nx1[0] + nx2[0]
    y = signal.signaltools.fftconvolve(x1, x2)
    return y[nny], ny

def aux_calcM(L,fs):
    #Función auxiliar para el Item 5 (Parte 1). Devuelve un arreglo de respuestas en frecuencia de FMM cuyos largos son L, L-1 , L-2 y L-3, respectivamente.
    RF_FMM1=abs(np.fft.fft(np.ones(L)/L,fs))
    RF_FMM2=abs(np.fft.fft(np.ones(L-1)/(L-1),fs))
    RF_FMM3=abs(np.fft.fft(np.ones(L-2)/(L-2),fs))
    RF_FMM4=abs(np.fft.fft(np.ones(L-3)/(L-3),fs))
    RF_FMM=np.array([RF_FMM1,RF_FMM2,RF_FMM3,RF_FMM4])
    return RF_FMM
