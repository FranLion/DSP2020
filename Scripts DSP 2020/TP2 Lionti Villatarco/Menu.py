import os
from Funcionestp2 import *
'''
Función que limpia la pantalla y muestra nuevamente el menú
'''
def menu():
	os.system('cls') # NOTA: para otro sistema operativo, cambiar 'cls' por 'clear'.
	print("\t \tPROCESAMIENTO DIGITAL DE SEÑALES")
	print("\t  TRABAJO PRÁCTICO N° 1: ESTUDIO DE EFECTOS\n\t \tDE AUDIO BASADO EN RETARDOS")
	print("\t\t      LIONTI-VILLATARCO")

	print ("\n")
	print ("\t \t   Seleccione una opción: ")
	print ("\t \t \t   1 - ECOS FINITOS")
	print ("\t \t \t   2 - ECOS INFINITOS")
	print ("\t \t \t   3 - ALGORITMO DE KARPLUS-STRONG")
	print ("\t \t \t   4 - ALGORITMO DE KARPLUS-STRONG MODIFICADO")
	print ("\t \t \t   5 - Salir")

while True:
	# Mostramos el menú
	menu()

	# solicituamos una opción al usuario
	opcionMenu = input("   Inserte un valor entero (entre 1 y 5) y presione ENTER >> ")

	if opcionMenu=="1":
		print ("")
		''' Ecos Finitos'''
		m69,fs=sf.read('Midi69.wav')# Se importa una señal de audio
		t=[100,800] #Duración del retardo en ms
		a=[-0.5,0.707] #Valores de atenuación alfa
		y1=delays(m69,t[0],fs,a[1],4)#Se aplican 4 ecos por cada tiempo de retardo
		y2=delays(m69,t[1],fs,a[0],4)
		sf.write('EcosFinitos(800 ms).wav',y2,fs)
		sp1=plt.figure('Ecos Finitos')
		plt.subplot(3,1,1)
		plt.plot(np.append(m69,np.zeros(len(y2)-len(m69))),'#0392cf')
		plt.title('Señal de entrada')
		plt.grid('both')
		plt.ylabel('x [n]')
		plt.xlabel('Número de muestra [n]')
		plt.axis([0,len(y2),-0.3,0.3])
		plt.subplot(3,1,2)
		plt.plot(np.append(y1,np.zeros(len(y2)-len(y1))),'#7bc043')
		plt.title('Señal con 4 ecos(100 ms)')
		plt.grid('both')
		plt.ylabel('y [n]')
		plt.xlabel('Número de muestra [n]')
		plt.axis([0,len(y2),-0.3,0.3])
		plt.subplot(3,1,3)
		plt.plot(y2,'#f37736')
		plt.title('Señal con 4 ecos(800 ms)')
		plt.grid('both')
		plt.ylabel('y [n]')
		plt.xlabel('Número de muestra [n]')
		plt.axis([0,len(y2),-0.3,0.3])
		plt.subplots_adjust(hspace = 1.4)
		plt.show()
		input("\n\t ECOS FINITOS ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="2":
		print ("")
		'''Ecos Infinitos'''
		m69,fs=sf.read('Midi69.wav')# Se importa una señal de audio
		t=[100,800] #Duración del retardo en ms
		a=[-0.5,0.707] #Valores de atenuación alfa
		y1=delays(m69,t[0],fs,a[1],4)#Se aplican 4 ecos por cada tiempo de retardo
		y2=delays(m69,t[1],fs,a[0],4)
		yinf1=IIR_delay(m69,a[1],15,fs)
		yinf2=IIR_delay(m69,0.5,t[0],fs)
		sf.write('EcosInfinitos(15 ms).wav',yinf1,fs)
		sp1=plt.figure('Ecos Infinitos')
		plt.subplot(3,1,1)
		plt.plot(np.append(m69,np.zeros(len(yinf2)-len(m69))),'#c51f5d')
		plt.title('Señal de entrada')
		plt.grid('both')
		plt.ylabel('x [n]')
		plt.xlabel('Número de muestra [n]')
		plt.axis([0,len(yinf2),-0.3,0.3])
		plt.subplot(3,1,2)
		plt.plot(np.append(yinf1,np.zeros(len(yinf2)-len(yinf1))),'#ee4035')
		plt.title('Señal con infinitos ecos (15 ms)')
		plt.grid('both')
		plt.ylabel('y [n]')
		plt.xlabel('Número de muestra [n]')
		plt.axis([0,len(yinf2),-0.3,0.3])
		plt.subplot(3,1,3)
		plt.plot(yinf2,'#9400d3')
		plt.title('Señal con infinitos ecos (100 ms)')
		plt.grid('both')
		plt.ylabel('y [n]')
		plt.xlabel('Número de muestra [n]')
		plt.axis([0,len(yinf2),-0.3,0.3])
		plt.subplots_adjust(hspace = 1.4)
		plt.show()
		input("\n\t ECOS INFINITOS ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="3":
		print ("")
		'''Implementación del algoritmo original de Karplus-Strong'''

		fs=44100
		T=1/fs
		f1=220 #Frecuencia fundamental
		Pa=1/2 #Pa(f1)
		eps=0.001 #epsilon
		P1=fs/f1
		N= int(np.floor(P1-Pa-eps)) #N
		n_samples=fs*2
		cuerda=karplus_strong(n_samples, 1 , N)# Cuerda sintetizada
		drum=karplus_strong(n_samples, 0.707 , N)# Drum sintetizado
		Hcuerda=np.fft.fft(cuerda)
		Hdrum=np.fft.fft(drum)
		freq = np.arange(0,fs/2,(fs/2)/int(len(cuerda)/2))
		sf.write('Cuerda.wav',cuerda,fs)
		sf.write('Drum.wav',drum,fs)

		sp1=plt.figure(figsize=(10,10))
		plt.subplot(2,2,1)
		plt.plot(freq,20*np.log10(abs(Hcuerda[:int(len(cuerda)/2)])),'#7bb8b4')
		plt.title('Cuerda Sintetizada')
		plt.grid('both')
		plt.ylabel('|H(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplot(2,2,2)
		plt.plot(freq,20*np.log10(abs(Hdrum[:int(len(drum)/2)])),'#314d5e')
		plt.title('Drum Sintetizado')
		plt.grid('both')
		plt.ylabel('|H(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplot(2,2,3)
		plt.plot(cuerda[:1000],'#94384d')
		plt.title('Cuerda Sintetizada')
		plt.grid('both')
		plt.ylabel('|H(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplot(2,2,4)
		plt.plot(drum[:1000],'#dc7582')
		plt.title('Drum Sintetizado')
		plt.grid('both')
		plt.ylabel('|H(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplots_adjust(hspace = 1)
		plt.subplots_adjust(wspace = 0.4)
		plt.show()
		input("\n\t ALGORITMO KS ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="4":
		print ("")

		'''Implementación del algoritmo de Karplus-Strong Modificado (MKS)'''
		'''Se Implementan 3 características del MKS, denominadas Ha(z), HL(z) y He(z),respectivamente.'''

		fs=44100
		T=1/fs
		f1=220 #Frecuencia fundamental
		Pa=1/2 #Pa(f1)
		eps=0.001 #epsilon
		P1=fs/f1
		N= int(np.floor(P1-Pa-eps)) #N
		n_samples=fs*2
		cuerda=karplus_strong(n_samples, 1 , N)# Cuerda sintetizada
		drum=karplus_strong(n_samples, 0.707 , N)# Drum sintetizado

		'''Ha(z): Alteración del tiempo de decaimiento'''
		S1=0.51
		S2=0.707
		S3=0.999999
		ya1=Ha(cuerda,int(P1),S1)
		ya2=Ha(cuerda,int(P1),S2)
		ya3=Ha(cuerda,int(P1),S3)
		Ha1=20*np.log10(abs(np.fft.fft(ya1)))
		Ha2=20*np.log10(abs(np.fft.fft(ya2)))
		Ha3=20*np.log10(abs(np.fft.fft(ya3)))
		sf.write('Ha1.wav',ya1,fs)
		sf.write('Ha2.wav',ya2,fs)
		sf.write('Ha3.wav',ya3,fs)

		sp1=plt.figure('Ha(jw): Alteración del tiempo de decaimiento')
		plt.subplot(3,1,1)
		plt.plot(Ha1[:int(len(Ha1)/8)],'#ee4035')
		plt.title('Ha(jw) con S=0.51')
		plt.grid('both')
		plt.ylabel('|Ha1(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplot(3,1,2)
		plt.plot(Ha2[:int(len(Ha2)/8)],'#42bdcb')
		plt.title('Ha(jw) con S=0.707')
		plt.grid('both')
		plt.ylabel('|Ha2(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplot(3,1,3)
		plt.plot(Ha3[:int(len(Ha3)/8)],'#72697d')
		plt.title('Ha(jw) con S=0.999')
		plt.grid('both')
		plt.ylabel('|Ha3(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplots_adjust(hspace = 1.4)
		plt.show()

		'''HL(z): Simulación de dinámica'''
		L1=100
		L2=1000
		L3=20000
		yL1=Hd(cuerda,L1,fs)
		yL2=Hd(cuerda,L2,fs)
		yL3=Hd(cuerda,L3,fs)
		HL1=20*np.log10(abs(np.fft.fft(yL1)))
		HL2=20*np.log10(abs(np.fft.fft(yL2)))
		HL3=20*np.log10(abs(np.fft.fft(yL3)))
		sf.write('HL1.wav',yL1,fs)
		sf.write('HL2.wav',yL2,fs)
		sf.write('HL3.wav',yL3,fs)

		sp1=plt.figure('HL(jw): Simulación de dinámica')
		plt.subplot(3,1,1)
		plt.plot(HL1[:int(len(HL1)/8)],'#2d0f59')
		plt.title('HL(jw) con L=100 Hz')
		plt.grid('both')
		plt.ylabel('|HL1(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplot(3,1,2)
		plt.plot(HL2[:int(len(HL2)/8)],'#b04e5d')
		plt.title('HL(jw) con L=1000 Hz')
		plt.grid('both')
		plt.ylabel('|HL2(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplot(3,1,3)
		plt.plot(HL3[:int(len(HL3)/8)],'#2c504a')
		plt.title('HL(jw) con L=20000 Hz')
		plt.grid('both')
		plt.ylabel('|HL3(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplots_adjust(hspace = 1.4)
		plt.show()

		'''He(z): Simulación de posición de púa'''

		mu1=1/100
		mu2=0.5
		mu3=0.707
		mu4=1/N
		ye1=He(cuerda,mu1,N)
		ye2=He(cuerda,mu2,N)
		ye3=He(cuerda,mu3,N)
		ye4=He(cuerda,mu4,N)
		He1=20*np.log10(abs(np.fft.fft(ye1)))
		He2=20*np.log10(abs(np.fft.fft(ye2)))
		He3=20*np.log10(abs(np.fft.fft(ye3)))
		sf.write('He1.wav',ye1,fs)
		sf.write('He2.wav',ye2,fs)
		sf.write('He3.wav',ye4,fs)

		sp1=plt.figure('He(jw): Posición relativa de la púa')
		plt.subplot(3,1,1)
		plt.plot(He1[:int(len(He1)/8)],'#8c4a3e')
		plt.title('He(jw) con mu=0.001')
		plt.grid('both')
		plt.ylabel('|He1(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplot(3,1,2)
		plt.plot(He2[:int(len(He2)/8)],'#263e06')
		plt.title('He(jw) con mu=0.5')
		plt.grid('both')
		plt.ylabel('|He2(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplot(3,1,3)
		plt.plot(He3[:int(len(He3)/8)],'#012a5e')
		plt.title('He(jw) con mu=1/N')
		plt.grid('both')
		plt.ylabel('|He3(jw)| [dB]')
		plt.xlabel('w [rad/muestra]')
		plt.subplots_adjust(hspace = 1.4)
		plt.show()
		input("\n\t ALGORITMO MKS ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="5":
		print ("\n")
		print ("\t \t \t¡MUCHAS GRACIAS!")
		break
	else:
		print ("")
		input("\t \tNo has pulsado ninguna opción correcta...\n\t \tpulse ENTER para continuar")
