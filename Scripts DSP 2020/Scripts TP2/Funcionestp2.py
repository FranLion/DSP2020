import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import soundfile as sf

def delays(senal,t,fs,a,N):
    d=int(round((t/1000)*fs))
    delay=np.zeros((N,len(senal)+(N*d)))
    x=np.append(senal,np.zeros(N*d))
    y=np.zeros_like(x)
    dly=np.zeros_like(x)
    for i in range(0,N):
        D=(i+1)*d
        zpad=np.zeros(D)
        aux=np.append(zpad,senal)
        delay[i]=np.append(aux,np.zeros(len(x)-len(aux)))
        dly=(a**(i+1))*delay[i]+dly #x[n-D]
    y=x+dly
    return y

def IIR_delay(senal,a,t,fs):
    D=int(round((t/100)*fs))
    delayline=np.zeros(D)
    x=np.append(senal,delayline)
    y=np.zeros_like(x)
    for i in range(len(x)):
        y[i]=x[i]+a*delayline[D-1]
        delayline=np.append(y[i],delayline[0:D-1])
    return y

#Ha y Hb:
def karplus_strong(n_samples, prob , wavetable_size):

    "Desde la tabla de onda anterior usando una distribucion binomial se genera un nuevo promedio."
    samples = []
    current_sample = 0
    previous_value = 0
    # wavetable_size = fs // p

    # conseguir la aleatoriedad de nivel dos
    wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)

    if prob ==1:

        while len(samples) < n_samples:

            #aca hago el karplus strong y los guardo en wavetable
            wavetable[current_sample] = 0.5 * (wavetable[current_sample] + previous_value)

            #aca le agrego a samples lo muestra i que estoy bucleando
            samples.append(wavetable[current_sample])

            #aca le digo al bucle que lea siempre la ultima muestra del vector que me importa
            previous_value = samples[-1]

            #acumulador
            current_sample += 1

            #Resto de la division entre el vector wavetable y el sample que estoy bucleando
            current_sample = current_sample % wavetable.size

    else:

        while len(samples) < n_samples:

            #Utilizo binomial
            r = np.random.binomial(1, prob)
            sign = float(r == 1) * 2 - 1
            wavetable[current_sample] = sign * 0.5 * (wavetable[current_sample] + previous_value)
            samples.append(wavetable[current_sample])
            previous_value = samples[-1]
            current_sample += 1
            current_sample = current_sample % wavetable.size

    return np.array(samples)

def Ha(senal,D,S) :
    #D=fs/f1
    rho = 0.996
    g0 = (1-S)*rho
    g1 = S*rho

    b = np.array([1.0]) # Zeros numerator coefficients
    a = np.array([1.0] + ([0]*(D-3)) + [-g0, -g1]) # Poles denominator coefficients
    y = signal.lfilter(b,a,senal)

    return y

# def Hc(senal,C):
#     b=np.array([C,1])
#     a=np.array([1,-C])
#     y=signal.lfilter(b, a, senal)
#     return y

def Hd(senal,L,fs):
    T=1/fs
    RL=np.exp(-np.pi*L*T)
    b=np.array([1-RL])
    a=np.array([1,-RL])
    y=signal.lfilter(b,a,senal)
    return y

def He(senal,mu,N):
    D=int(mu*N)
    b=np.zeros(D)
    b[0]=1
    b[D-1]=-1
    a=np.array([1])
    y=signal.lfilter(b, a, senal)
    return y
