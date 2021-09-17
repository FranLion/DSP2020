import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from scipy import signal
'''
En el presente módulo se importan las librerías y se definen las variales globales y las funciones que se necesiten en distintos items.
'''

'''Definición de Variables Globales'''
#Definición de señal de entrada x[n]=data de longitud N=1000.
data=np.ones(1000)

#Definición de la señal senoidal x(t)= 2 + sen(2πft). (Varios Items)
frec=10000
fs = 44100
duración = 0.5
t=np.arange(0,duración,1/fs) #vector de muestras
señal=2 + np.sin(2*np.pi*frec*t) #defino funcion sen(2pi*f*t)

#Importación de Archivos .wav (Item 8 y 11).
[RIR,Fs] = sf.read("RIR.wav")
[Midi69,Fs1] = sf.read("Midi69.wav")
nMidi=np.arange(0,len(Midi69))
nRIR=np.arange(0,len(RIR))

''' Definimos las funciones que se utilizan. '''
def senalTP():
    f=10000
    fs = 44100
    t = 0.5
    n=np.arange(0,t,1/fs) #vector de muestras
    señal=2 + np.sin(2*np.pi*f*n) #defino funcion sen(2pi*f*t)
    return señal,n,fs

def lamedia(input):
    mu=np.sum(input)/(len(input)) #Defino la función del calculo de media
    return mu

def desviomedio(input,media):
    d=np.sum(abs(input-media))/(len(input)) #Defino la función del cálculo del desvío medio
    return d

def desvioestandar(input,media):
    sigma=((np.sum(abs(input-media)**2))/(len(input)))**(1/2) #Defino la función del cálculo del desvío estándar
    return sigma

def rms(input):
    rms=((np.sum(abs(input**2)))/(len(input)))**(1/2) #Defino la función del cálculo de RMS
    return rms

#Generar ruido
def normalizar(input):
    media=lamedia(input)
    desviacion=desvioestandar(input,media)
    for i in range(len(input)):
        input[i]=(input[i]-media)/desviacion
    return input

#Relación señal ruido
def calc_SNR(senal,ruido):
    media=lamedia(senal)
    sigmanoise=desvioestandar(ruido,lamedia(ruido))
    SNR=np.max(senal)/sigmanoise
    return SNR , sigmanoise

def senales_con_ruido(senal,mu,sigma,N):
    # Genera señales con ruido, hace el promedio en ensamble y devuelve el SNR de la señal promediada y el sigma del promedio de los ruidos.
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
    M=L-1 #Según la definición utilizada para implementar el FMM el largo de la ventana es M+1
    #Asiganciones de espacios en memoria
    y=np.zeros(len(x))
    aux=np.append(x,np.zeros(M))
    #Media movil directa
    for i in range(len(x)):
        for j in range(0,M+1):
            y[i]=y[i]+aux[i+j]
        y[i]=y[i]*(1/(M+1))
    return y

def mediamovildr(x,L):
    M=L-1 # Según la definición utilizada para implementar el FMM el largo de la ventana es M+1
    #Asiganciones de espacios en memoria
    y=np.zeros(len(x))
    y[0]=(1/(M+1))*np.sum(x[:M+1])
    aux=np.append(x,np.zeros(M))
    #Media movil recursiva
    for i in range(1,len(x)):
        y[i]=y[i-1]+(1/(M+1))*aux[i+M]-(1/(M+1))*aux[i-1]
    return y
#Ventana Blackman
def wBlackman(M):
    a0=(7935/18608)
    a1=(9240/18608)
    a2=(1430/18608)
    m=np.linspace(0,M-1,M)
    blackman=a0 - ((a1)*np.cos((2*np.pi*m)/(M))) + ((a2)*np.cos((4*np.pi*m)/(M)))
    return blackman

def Importar_Audio(file,señal):
    [señal,Fs] = sf.read(file)
    n=np.arange(0,len(señal))
    return señal,Fs,n

def convCircular(x1,nx1,x2,nx2):
    nny = np.arange(0,len(nx1)+len(nx2)-1)
    ny = np.arange(0,len(x1)+len(x2)-1) + nx1[0] + nx2[0]
    y = np.convolve(x1, x2)
    return y[nny], ny

def cConv(x1,nx1,x2,nx2,l):
    if l==1:
        nny = np.arange(0,len(x1))
        ny = np.arange(0,len(x1)) + nx1[0] + nx2[0]
    elif l==2:
        nny = np.arange(0,len(x2))
        ny = np.arange(0,len(x2)) + nx1[0] + nx2[0]
    y = np.convolve(x1, x2)
    return y[nny], ny

def RF_boxcar(M,f):
    RF_rectang=(np.exp(-1j*((M-1)*f)/2))*(np.sin(f*M/2)/np.sin(f/2))
    return RF_rectang

def RF_Blackman(T,f):
    a0=(7935/18608)
    a1=(9240/18608)
    a2=(1430/18608)
    H0=(np.sin(f*T/2)/np.sin(f/2))
    H1=(np.exp(-1j*(np.pi)/T)*(np.sin((T*f/2)-np.pi)/np.sin((f-(2*np.pi/T))/2)))+((np.exp(1j*(np.pi)/T))*(np.sin((f+(2*np.pi/T))*T/2)/np.sin((f+(2*np.pi/T))/2)))
    H2=(np.exp(1j*(2*np.pi)/T)*(np.sin((f-(4*np.pi/T))*T/2)/np.sin((f-(4*np.pi/T))/2)))+(np.exp(1j*(2*np.pi)/T)*(np.sin((f+(4*np.pi/T))*T/2)/np.sin((f+(4*np.pi/T))/2)))
    RF_blackman=(np.exp(-1j*((T-1)*f)/2))*((a0*H0)-((a1/2)*H1)+((a2/2)*H2))
    return RF_blackman

def RFdB_ventanas(RF,T):
    resp =RF/(T/2.0)
    respN = np.abs(resp/abs(resp).max())
    RFdB = 20 * np.log10(np.maximum(respN, 1e-10))
    return RFdB

def FFT_convLineal(x1,x2):
    y=signal.signaltools.fftconvolve(x1,x2)
    return y

def FFT_convCircular(x1,nx1,x2,nx2):
    nny = np.arange(0,len(nx1)+len(nx2)-1)
    ny = np.arange(0,len(x1)+len(x2)-1) + nx1[0] + nx2[0]
    y = signal.signaltools.fftconvolve(x1, x2)
    return y[nny], ny

def FFT_cConv(x1,nx1,x2,nx2,l):
    if l==1:
        nny = np.arange(0,len(x1))
        ny = np.arange(0,len(x1)) + nx1[0] + nx2[0]
    elif l==2:
        nny = np.arange(0,len(x2))
        ny = np.arange(0,len(x2)) + nx1[0] + nx2[0]
    y = signal.signaltools.fftconvolve(x1, x2)
    return y[nny], ny
