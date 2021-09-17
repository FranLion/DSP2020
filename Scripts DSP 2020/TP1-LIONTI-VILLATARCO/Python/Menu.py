import os
'''
Función que limpia la pantalla y muestra nuevamente el menú
'''
def menu():
	os.system('cls') # NOTA: para otro sistema operativo, cambiar 'cls' por 'clear'.
	print("\t \tPROCESAMIENTO DIGITAL DE SEÑALES")
	print("\t  TRABAJO PRÁCTICO N° 1: PROGRAMACIÓN BÁSICA")
	print("\t\t      LIONTI-VILLATARCO")

	print ("\n")
	print ("\t \t   Seleccione una opción: ")
	print ("\t \t \t   1 - Item 1")
	print ("\t \t \t   2 - Item 2")
	print ("\t \t \t   3 - Item 3")
	print ("\t \t \t   4 - Item 4")
	print ("\t \t \t   5 - Item 5")
	print ("\t \t \t   6 - Item 6")
	print ("\t \t \t   7 - Item 7")
	print ("\t \t \t   8 - Item 8")
	print ("\t \t \t   9 - Item 9")
	print ("\t \t \t  10 - Item 10")
	print ("\t \t \t  11 - Item 11")
	print ("\t \t \t  12 - Salir")


while True:
	# Mostramos el menú
	menu()

	# solicituamos una opción al usuario
	opcionMenu = input("   Inserte un valor entero (entre 1 y 12) y presione ENTER >> ")

	if opcionMenu=="1":
		print ("")
		os.system("Items\Item1.py")
		input("\n\t Item 1 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="2":
		print ("")
		os.system("Items\Item2.py")
		input("\n\t Item 2 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="3":
		print ("")
		os.system("Items\Item3.py")
		input("\n\t Item 3 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="4":
		print ("")
		os.system("Items\Item4.py")
		input("\n\t Item 4 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="5":
		print ("")
		os.system("Items\Item5.py")
		input("\n\t Item 5 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="6":
		print ("")
		os.system("Items\Item6.py")
		input("\n\t Item 6 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="7":
		print ("")
		os.system("Items\Item7.py")
		input("\n\t Item 7 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="8":
		print ("")
		os.system("Items\Item8.py")
		input("\n\t Item 8 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="9":
		print ("")
		os.system("Items\Item9.py")
		input("\n\t Item 9 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="10":
		print ("")
		os.system("Items\Item10.py")
		input("\n\t Item 10 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="11":
		print ("")
		os.system("Items\Item11.py")
		input("\n\t Item 11 ejecutado...\n\t pulse una ENTER para continuar")
	elif opcionMenu=="12":
		print ("\n")
		print ("\t \t \t¡MUCHAS GRACIAS!")
		break
	else:
		print ("")
		input("\t \tNo has pulsado ninguna opción correcta...\n\t \tpulse ENTER para continuar")
