import os
import numpy as np
import LowPass as LP
import HighPass as hp
import BandPass as bp
import BandStop as bs
'''
Función que limpia la pantalla y muestra nuevamente el menú
'''
def menu():
	os.system('cls') # NOTA: para otro sistema operativo, cambiar 'cls' por 'clear'.
	print("\t \tPROCESAMIENTO DIGITAL DE SEÑALES")

	print ("\n")
	print ("\t \t   Seleccione una opción: ")
	print ("\t \t \t   1 - Rectangular")
	print ("\t \t \t   2 - Barlett")
	print ("\t \t \t   3 - Hanning")
	print ("\t \t \t   4 - Hamming")
	print ("\t \t \t   5 - Blackman")
	print ("\t \t \t   6 - Kaiser")
	print ("\t \t \t   Q - Salir")


def mw(id_filter):
    if id_filter == 1:
        while True:
        	# Mostramos el menú
        	menu()

        	# solicituamos una opción al usuario
        	opcionMenu = input("   Inserte un valor entero (entre 1 y 6) o Q para salir y presione ENTER >> ")
        	if opcionMenu=="1":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		LP.LP_fir(data[0],data[1],data[2],data[3],int(data[4]),1)
        		input("\n\t Item 1 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="2":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		LP.LP_fir(data[0],data[1],data[2],data[3],int(data[4]),2)
        		input("\n\t Item 2 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="3":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		LP.LP_fir(data[0],data[1],data[2],data[3],int(data[4]),3)
        		input("\n\t Item 3 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="4":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		LP.LP_fir(data[0],data[1],data[2],data[3],int(data[4]),4)
        		input("\n\t Item 4 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="5":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		LP.LP_fir(data[0],data[1],data[2],data[3],int(data[4]),5)
        		input("\n\t Item 4 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="6":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		LP.LP_fir(data[0],data[1],data[2],data[3],int(data[4]),6)
        		input("\n\t Item 6 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu =="Q" or opcionMenu =="q":
        		print ("\n")
        		print ("\t \t \t¡MUCHAS GRACIAS!")
        		break
        	else:
        		print ("")
        		input("\t \tNo has pulsado ninguna opción correcta...\n\t \tpulse ENTER para continuar")
    elif id_filter == 2:
        while True:
        	# Mostramos el menú
        	menu()

        	# solicituamos una opción al usuario
        	opcionMenu = input("   Inserte un valor entero (entre 1 y 4) o Q para salir y presione ENTER >> ")

        	if opcionMenu=="1":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		hp.HP_fir(data[0],data[1],data[2],data[3],int(data[4]),1)
        		input("\n\t Item 1 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="2":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		hp.HP_fir(data[0],data[1],data[2],data[3],int(data[4]),2)
        		input("\n\t Item 2 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="3":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		hp.HP_fir(data[0],data[1],data[2],data[3],int(data[4]),3)
        		input("\n\t Item 3 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="4":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		hp.HP_fir(data[0],data[1],data[2],data[3],int(data[4]),4)
        		input("\n\t Item 4 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="5":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		hp.HP_fir(data[0],data[1],data[2],data[3],int(data[4]),5)
        		input("\n\t Item 5 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="6":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		hp.HP_fir(data[0],data[1],data[2],data[3],int(data[4]),6)
        		input("\n\t Item 6 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu =="Q" or opcionMenu =="q":
        		print ("\n")
        		print ("\t \t \t¡MUCHAS GRACIAS!")
        		break
        	else:
        		print ("")
        		input("\t \tNo has pulsado ninguna opción correcta...\n\t \tpulse ENTER para continuar")
    elif id_filter == 3:
        while True:
        	# Mostramos el menú
        	menu()

        	# solicituamos una opción al usuario
        	opcionMenu = input("   Inserte un valor entero (entre 1 y 4) o Q para salir y presione ENTER >> ")

        	if opcionMenu=="1":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		bp.BP_fir(data[0],data[1],data[2],data[3],data[4],data[5],int(data[6]),1)
        		input("\n\t Item 1 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="2":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		bp.BP_fir(data[0],data[1],data[2],data[3],data[4],data[5],int(data[6]),2)
        		input("\n\t Item 2 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="3":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		bp.BP_fir(data[0],data[1],data[2],data[3],data[4],data[5],int(data[6]),3)
        		input("\n\t Item 3 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="4":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		bp.BP_fir(data[0],data[1],data[2],data[3],data[4],data[5],int(data[6]),4)
        		input("\n\t Item 4 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="5":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		bp.BP_fir(data[0],data[1],data[2],data[3],data[4],data[5],int(data[6]),5)
        		input("\n\t Item 5 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="6":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		bp.BP_fir(data[0],data[1],data[2],data[3],data[4],data[5],int(data[6]),6)
        		input("\n\t Item 6 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu =="Q" or opcionMenu =="q":
        		print ("\n")
        		print ("\t \t \t¡MUCHAS GRACIAS!")
        		break
        	else:
        		print ("")
        		input("\t \tNo has pulsado ninguna opción correcta...\n\t \tpulse ENTER para continuar")
    elif id_filter ==4:
        while True:
        	# Mostramos el menú
        	menu()

        	# solicituamos una opción al usuario
        	opcionMenu = input("   Inserte un valor entero (entre 1 y 4) o Q para salir y presione ENTER >> ")

        	if opcionMenu=="1":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		bs.BS_fir(data[0],data[1],data[2],data[3],data[4],data[5],int(data[6]),1)
        		input("\n\t Item 1 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="2":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		bs.BS_fir(data[0],data[1],data[2],data[3],data[4],data[5],int(data[6]),2)
        		input("\n\t Item 2 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="3":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		bs.BS_fir(data[0],data[1],data[2],data[3],data[4],data[5],int(data[6]),3)
        		input("\n\t Item 3 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="4":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		bs.BS_fir(data[0],data[1],data[2],data[3],data[4],data[5],int(data[6]),4)
        		input("\n\t Item 4 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="5":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		bs.BS_fir(data[0],data[1],data[2],data[3],data[4],data[5],int(data[6]),5)
        		input("\n\t Item 5 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu=="6":
        		print ("")
        		data=np.float64(input("Ingrese valores separados por espacios: ").split(' '))
        		bs.BS_fir(data[0],data[1],data[2],data[3],data[4],data[5],int(data[6]),6)
        		input("\n\t Item 6 ejecutado...\n\t pulse una ENTER para continuar")
        	elif opcionMenu =="Q" or opcionMenu =="q":
        		print ("\n")
        		print ("\t \t \t¡MUCHAS GRACIAS!")
        		break
        	else:
        		print ("")
        		input("\t \tNo has pulsado ninguna opción correcta...\n\t \tpulse ENTER para continuar")
    else: print("Opcion incorrecta.")
