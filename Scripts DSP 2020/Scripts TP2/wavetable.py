import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

fs=44100

p1 = 55

p2 = 20

def make_sine_wavetable(n_samples, amps, phases, freqs):

    """Genero una tabla de ondas a traves de sumas senoidales."""

    t = np.linspace(0, 1, num=n_samples)

    wavetable = np.zeros_like(t)

    for amp, phase, freq in zip(amps,phases,freqs):

        wavetable += amp * np.sin(np.sin(2 * np.pi * freq * t + phase)) + \
                         amp / 2 * np.sin(np.sin(2 * np.pi * 2 * freq * t + phase))

    return wavetable

def karplus_strong(wavetable, n_samples):

    "Synthesizes a new waveform from an existing wavetable, modifies last sample by averaging."

    samples = []

    current_sample = 0

    previous_value = 0

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

    return np.array(samples)

def karplus_strong_perc(wavetable, n_samples, prob):

    "Desde la tabla de onda anterior usando una distribucion binomial se genera un nuevo promedio."

    samples = []

    current_sample = 0

    previous_value = 0

    while len(samples) < n_samples:

        r = np.random.binomial(1, prob)

        sign = float(r == 1) * 2 - 1

        wavetable[current_sample] = sign * 0.5 * (wavetable[current_sample] + previous_value)

        samples.append(wavetable[current_sample])

        previous_value = samples[-1]

        current_sample += 1

        current_sample = current_sample % wavetable.size

    return np.array(samples)

wavetable_size1 = fs // p1

wavetable_size2 = fs // p2

# conseguir la aleatoriedad de nivel dos
wavetable1 = (2 * np.random.randint(0, 2, wavetable_size1) - 1).astype(np.float)

wavetable2 = (2 * np.random.randint(0, 2, wavetable_size2) - 1).astype(np.float)

sample1 = karplus_strong(wavetable1, 2 * fs)

sample2 = karplus_strong_perc(wavetable2, fs, 0.2)

sf.write('karputo.wav', sample1, fs)
sf.write('karputodrum.wav', sample2, fs)

#Plots

sp1=plt.figure('Karputo')
plt.subplot(2,1,1)
plt.plot(sample1,'#738EB6')
plt.title('Señal generada por la cuerda')
plt.grid('both')
plt.ylabel('Amplitud relativa [n]')
plt.xlabel('Número de muestra [n]')
plt.subplot(2,1,2)
plt.plot(sample2,'#BF76D2')
plt.title('Señal generada por la percusión')
plt.grid('both')
plt.ylabel('Amplitud relativa [n]')
plt.xlabel('Número de muestra [n]')
plt.subplots_adjust(hspace = 1.2)
plt.show()
