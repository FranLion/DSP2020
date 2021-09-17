import os
import MenuWind as mw
'''
Función que limpia la pantalla y muestra nuevamente el menú
'''
def menu():
	os.system('cls') # NOTA: para otro sistema operativo, cambiar 'cls' por 'clear'.
	print("\t \tPROCESAMIENTO DIGITAL DE SEÑALES")

	print ("\n")
	print ("\t \t   Seleccione una opción: ")
	print ("\t \t \t   1 - Low Pass")
	print ("\t \t \t   2 - High Pass")
	print ("\t \t \t   3 - Band Pass")
	print ("\t \t \t   4 - Band Stop")
	print ("\t \t \t   Q - Salir")


while True:
	# Mostramos el menú
	menu()

	# solicituamos una opción al usuario
	opcionMenu = input("   Inserte un valor entero (entre 1 y 4) o Q para salir y presione ENTER >> ")

	if opcionMenu=="1":
		print ("")

		mw.mw(1)
		input("\n\t Item 1 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="2":
		print ("")

		mw.mw(2)
		input("\n\t Item 2 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="3":
		print ("")

		mw.mw(3)
		input("\n\t Item 3 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="4":
		print ("")
		mw.mw(4)
		input("\n\t Item 4 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu =="Q" or opcionMenu =="q":
		print ("\n")
		print ("\t \t \t¡MUCHAS GRACIAS!")
		break
	else:
		print ("")
		input("\t \tNo has pulsado ninguna opción correcta...\n\t \tpulse ENTER para continuar")
