# import soundfile as sf
# import matplotlib.pyplot as plt
# import numpy as np
# import wave
# import time
# [m69,Fs] = sf.read("Midi69.wav")
#
# d=0.5 #segundos
# D=int(round(d*Fs))
# zpad=np.zeros(D)
# delay=np.append(zpad,m69)
# a=(2**(1/2))/2
#
# x=np.append(m69,zpad)
# n=np.arange(0,len(x))
# y=0
# a=0
#
# try:
#     while True:
#         a=a+1
#         b=1/a
#         zpad=np.zeros(a)
#         x=np.append(m69,zpad)
#         delay=np.append(zpad,m69)#x[n-D]
#         delay2=y+delay
#         y=x+b*delay#y[n]=x[n]+b*y[n-D]
#         print("Retardo agregado")
#         time.sleep(1)
#         result = np.where(y != 0)
#         print('a:',a)
#         print("Largo total: ",len(y))
#         print("Ultima posición distinta de cero: ", result[0][-1])
# except KeyboardInterrupt:
#     print("Hard Exit Initiated. Goodbye!")
#
#
#     # for tu hermana i:
# y[0]=(1/(M+1))*np.sum(x[:M+1])
# # D=int(round(d*Fs))
# A=1
# zpad=np.zeros(A)
# x=np.append(m69,zpad)
# n=np.arange(0,len(x))
#
#
# aux=np.append(x,np.zeros(M))
#     #Media movil recursiva
# for i in range(1,len(x)):
#
#
#     y[i]=y[i-D] #Se divide por M+1 ya que este es el largo de ventana
# return y
#
# y=y+x
#
#
#
#
#
#
#
# def mediamovildr(x,L):
#     #Implementación recursiva del filtro media móvil de largo L a una señal x.
#     M=L-1 #Según la definición utilizada para implementar el FMM el largo de la ventana es M+1
#     y=np.zeros(len(x))#Asiganciones de espacios en memoria
#     y[0]=(1/(M+1))*np.sum(x[:M+1])
#     aux=np.append(x,np.zeros(M))
#     #Media movil recursiva
#     for i in range(1,len(x)):
#         y[i]=y[i-D]+(1/(M+1))*aux[i+M]-(1/(M+1))*aux[i-1] #Se divide por M+1 ya que este es el largo de ventana
#     return y
#
# # try:
# #     while True:
# #         print("Olis")
# #         time.sleep(1)
# # except KeyboardInterrupt:
# #     print("Hard Exit Initiated. Goodbye!")


a=3%10

print(a)
