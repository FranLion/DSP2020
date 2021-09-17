from FuncionesTP import *

'''En este inciso se generan señales a partir de ir añadiendo distintos ruidos a la señal original del Item 1 x[n]=data y realizar un promedio en ensamble de las mismas. Las señales se calculan a partir del promediado de 10, 100 y 1000 señalesde ruido diferentes.
'''
# Se generan las 10 señales de ruido aleatorio con media 0 y sigma 3
z31 =  np.random.normal(0, 3, len(data))
z32 = np.random.normal(0, 3, len(data))
z33 = np.random.normal(0, 3, len(data))
z34 = np.random.normal(0, 3, len(data))
z35 = np.random.normal(0, 3, len(data))
z36 = np.random.normal(0, 3, len(data))
z37 = np.random.normal(0, 3, len(data))
z38 = np.random.normal(0, 3, len(data))
z39 = np.random.normal(0, 3, len(data))
z310 = np.random.normal(0, 3, len(data))

# Genero cada señal sumando la señal de entrada y un ruido
x31 = data + z31
x32 = data + z32
x33 = data + z33
x34 = data + z34
x35 = data + z35
x36 = data + z36
x37 = data + z37
x38 = data + z38
x39 = data + z39
x310 = data + z310

# Saco una señal de ruido promedio de las 10 señales de ruido generadas (solo ruido)
ruidoProm=(1/10)*(z31+z32+z33+z34+z35+z36+z37+z38+z39+z310)

#Promedio de las señales con ruido agregado
Señalprom=(1/10)*(x31+x32+x33+x34+x35+x36+x37+x38+x39+x310)
SNRprom , sigmanoise=calc_SNR(Señalprom,ruidoProm) #Calculo el SNR de la señal promedio con los valores obtenidos y saco el sigma de la señal de ruido promedio.

#Calculamos los SNR y los sigmas para las señales con promedio en ensamble para 1, 10, 100 y 1000 señales de ruido. La función senales_con_ruido automatiza el calculo y está definida en FuncionesTP, esta se usará para presentar los resultados.
SNR1,sigmaruido1=senales_con_ruido(data,0,3,1)
SNR10,sigmaruido10=senales_con_ruido(data,0,3,10)
SNR100,sigmaruido100=senales_con_ruido(data,0,3,100)
SNR1000,sigmaruido1000=senales_con_ruido(data,0,3,1000)

# Se prensentan los resultados
datos=[[1,round(SNR1,2),round(sigmaruido1,2)],[10,round(SNR10,2),round(sigmaruido10,2)], [100,round(SNR100,2),round(sigmaruido100,2)], [1000,round(SNR1000,2),round(sigmaruido1000,2)]]
Tabla = """\
+--------------------------------------------+
|N° Señales promediadas |      SNR |       σ |
|--------------------------------------------|
{}
+--------------------------------------------+\
"""
Tabla = (Tabla.format('\n'.join("| {:>21d} | {:>8} | {:>7} |".format(*fila)
 for fila in datos)))
print("          Resultados obtenidos Item 4 ")
print (Tabla)
