from FuncionesTP import *

'''
En este ejercicio se generan 6 señales de ruido con distribución Gaussiana y con los largos pedidos
en la consigna. Cada ruido se genera con una media nula y una desviación estandar igual a 1.
'''
Señalrandom1 = np.random.normal(0, 1, 5)
Señalrandom2 = np.random.normal(0, 1, 10)
Señalrandom3 = np.random.normal(0, 1, 100)
Señalrandom4 = np.random.normal(0, 1, 1000)
Señalrandom5 = np.random.normal(0, 1, 10000)
Señalrandom6 = np.random.normal(0, 1, 100000)

#A continuación se calculan la media y la desviación estándar de cada ruido generado utilizando las funciones
#pedidas en el Item 1 y que se encuentran definidas en el módulo "Funciones"(Funciones.py).
#Se redondea a dos decimales para fines prácticos.
lamedia1=lamedia(Señalrandom1)
desvioestandar1=round(desvioestandar(Señalrandom1,lamedia1),2)
lamedia2=lamedia(Señalrandom2)
desvioestandar2=round(desvioestandar(Señalrandom2,lamedia2),2)
lamedia3=lamedia(Señalrandom3)
desvioestandar3=round(desvioestandar(Señalrandom3,lamedia3),2)
lamedia4=lamedia(Señalrandom4)
desvioestandar4=round(desvioestandar(Señalrandom4,lamedia4),2)
lamedia5=lamedia(Señalrandom5)
desvioestandar5=round(desvioestandar(Señalrandom5,lamedia5),2)
lamedia6=lamedia(Señalrandom6)
desvioestandar6=round(desvioestandar(Señalrandom6,lamedia6),2)

# Se calculan las diferencias porcentuales con un redondeo a 0 decimales.
dif1=round((desvioestandar1-1)*100,0)
dif2=round((desvioestandar2-1)*100,0)
dif3=round((desvioestandar3-1)*100,0)
dif4=round((desvioestandar4-1)*100,0)
dif5=round((desvioestandar5-1)*100,0)
dif6=round((desvioestandar6-1)*100,0)

# Se presentan los resultados obtenidos.
print(f"     N        σ        %")
print(f"     5     {desvioestandar1}      {int(dif1)}")
print(f"    10     {desvioestandar2}      {int(dif2)}")
print(f"   100     {desvioestandar3}      {int(dif3)}")
print(f"  1000     {desvioestandar4}      {int(dif4)}")
print(f" 10000     {desvioestandar5}       {int(dif5)}")
print(f"100000     {desvioestandar6}       {int(dif6)}")
