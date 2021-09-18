from Funcionestp2 import *
#Ha base y Hb:
# def karplus_strongestirado(n_samples,f1, wavetable_size,fs):
#
#     samples = []
#     current_sample = 0
#     previous_value = 0
#
#     # conseguir la aleatoriedad de nivel dos
#     wavetable = (2 * np.random.randint(0, 2, int(wavetable_size)) - 1).astype(np.float)
#
#     while len(samples) < n_samples:
#
#         if wavetable_size >= fs/4:
#             ro=0.45
#             S=0
#             #aca hago el karplus strong y los guardo en wavetable
#             wavetable[current_sample] = (0.5)*(wavetable[current_sample] + previous_value)
#             #aca le agrego a samples lo muestra i que estoy bucleando
#             samples.append(wavetable[current_sample])
#             #aca le digo al bucle que lea siempre la ultima muestra del vector que me importa
#             previous_value = samples[-1]
#             #acumulador
#             current_sample += 1
#             #Resto de la division entre el vector wavetable y el sample que estoy bucleando
#             current_sample = (ro)*current_sample % wavetable.size
#         else:
#             S=0.9
#             ro=0
#             #aca hago el karplus strong y los guardo en wavetable
#             wavetable[current_sample] = ((1-S)*(wavetable[current_sample]) + S*(previous_value))
#             #aca le agrego a samples lo muestra i que estoy bucleando
#             samples.append(wavetable[current_sample])
#             #aca le digo al bucle que lea siempre la ultima muestra del vector que me importa
#             previous_value = samples[-1]
#             #acumulador
#             current_sample += 1
#             #Resto de la division entre el vector wavetable y el sample que estoy bucleando
#             current_sample = current_sample % wavetable.size
#
#     return np.array(samples),S,ro

def el_estirador(senal,D,S) :

    rho = 0.996
    g0 = (1-S)*rho
    g1 = S*rho

    b = np.array([1.0]) # Zeros numerator coefficients
    a = np.array([1.0] + ([0]*(D-3)) + [-g0, -g1]) # Poles denominator coefficients
    samples = sp.lfilter(b,a,senal)

    return samples

fs=48000

n_samples=2*fs

#f1 va desde 2 hasta 44100 cuanto mas chico el f1 mas alta es la frecuencia
f=20
D=int(fs/f)
#wavetable size es el periodo relativo a la frecuencia que quiero probar
wavetable_size = fs // f

estirar=karplus_strong(n_samples, 1, wavetable_size)

estira3=el_estirador(estirar,D,0.5)

sf.write('estira3.wav',estira3,fs)
plt.plot(estira3)
plt.show()
