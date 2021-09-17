import matplotlib.pyplot as plt
import numpy as np
import math
import heapq
import time
import soundfile as sf
from convolucion import *
from scipy import signal

'''Ejercicio 8 '''
'''
revisar aca la convolucion
'''
[RIR,Fs] = sf.read("RIR.wav")
[Midi69,Fs1] = sf.read("Midi69.wav")
L=len(Midi69)
K=len(RIR)
cLineal=np.convolve(Midi69,RIR)
cCirc=np.convolve(Midi69[:K],RIR)
cCircular=convCirc(Midi69,RIR)
cLineal=np.real(cLineal)
cCirc=np.real(cCirc)
cCircular=np.real(cCircular)
sf.write('cLinealout.wav', cLineal, Fs)
sf.write('cCircout.wav', cCirc, Fs)
sf.write('cCircularout.wav', cCircular, Fs)
figure,axis = plt.subplots(3)
axis[0].plot(cLineal)
axis[1].plot(cCircular)
axis[2].plot(cCirc)
plt.show()
