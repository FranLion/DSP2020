import os

print("PROCESAMIENTO DE SEÑALES DIGITALES")

print ("\n")

print("TRABAJO PRÁCTICO 1: PROGRAMACIÓN BÁSICA")

print ("\n")

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("Seleccioná un item para ejecutar")
	print ("\t1 - Item 1")
	print ("\t2 - Item 2")
	print ("\t3 - Item 3")
	print ("\t4 - Item 4")
	print ("\t5 - Item 5")
	print ("\t6 - Item 6")
	print ("\t7 - Item 7")
	print ("\t8 - Item 8")
	print ("\t9 - Item 9")
	print ("\t10 - Item 10")
	print ("\t11 - Item 11")
	print ("\t12 - Salir")


while True:
	# Mostramos el menu
	menu()

	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")

	if opcionMenu=="1":
		print ("")
		os.system("Item1.py")
		input("Item 1 ejecutado...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		os.system("Item2.py")
		input("Item 2 ejecutado...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		os.system("Item3.py")
		input("Item 3 ejecutado...\npulsa una tecla para continuar")
	elif opcionMenu=="4":
		print ("")
		os.system("Item4.py")
		input("Item 4 ejecutado...\npulsa una tecla para continuar")
	elif opcionMenu=="5":
		print ("")
		os.system("Item5.py")
		input("Item 5 ejecutado...\npulsa una tecla para continuar")
	elif opcionMenu=="6":
		print ("")
		os.system("Item6.py")
		input("Item 6 ejecutado...\npulsa una tecla para continuar")
	elif opcionMenu=="7":
		print ("")
		os.system("Item7.py")
		input("Item 7 ejecutado...\npulsa una tecla para continuar")
	elif opcionMenu=="8":
		print ("")
		os.system("Item8.py")
		input("Item 8 ejecutado...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		print ("")
		os.system("Item9.py")
		input("Item 9 ejecutado...\npulsa una tecla para continuar")
	elif opcionMenu=="10":
		print ("")
		os.system("Item10.py")
		input("Item 10 ejecutado...\npulsa una tecla para continuar")
	elif opcionMenu=="11":
		print ("")
		os.system("Item11.py")
		input("Item 11 ejecutado...\npulsa una tecla para continuar")
	elif opcionMenu=="12":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
