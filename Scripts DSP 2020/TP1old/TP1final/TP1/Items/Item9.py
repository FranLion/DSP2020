from FuncionesTP import *

''' En este inciso se grafica la respuesta en frecuencia del filtro media móvil con una resolución de 44100 Hz. Cabe señalar que el largo de la ventana obtenido en el Item 5 corresponde a M=2.
'''
M=2 #El largo de la ventana es L=M+1.
w=np.arange(-1*np.pi,np.pi,2*np.pi/44100) #Se genera un vector de muestras con frecuencia de sampleo de 44100 Hz.
H=abs((1/(M))*((np.sin(w*(M)/2))/(np.sin(w/2)))) #Respuesta en frecuencia del filtro media móvil.

# Se Grafican los resultados.
plt.figure('Item 9 Grafico de magnitud para respuesta del filtro')
plt.plot(w,H)
# Gráfico de magnitud de respuesta en frecuencia del filtro media móvil.
plt.title('Respuesta en frecuencia FMM')
plt.xlabel('ω [rad/s]')
plt.ylabel('|H[ω]|')
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], ['-π', '-π/2', '0', 'π/2', 'π'])
plt.show()

# >>> locs, labels = xticks()  # Get the current locations and labels.
# >>> xticks(np.arange(0, 1, step=0.2))  # Set label locations.
# >>> xticks(np.arange(3), ['Tom', 'Dick', 'Sue'])  # Set text labels.
# >>> xticks([0, 1, 2], ['January', 'February', 'March'],
# ...        rotation=20)  # Set text labels and properties.
# >>> xticks([])  # Disable xticks.
