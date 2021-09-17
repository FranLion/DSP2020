from FuncionesTP import *

'''
En este ejercicio se generan 6 señales de ruido con distribución Gaussiana y con los largos pedidos
en la consigna. Cada ruido se genera con una media nula y una desviación estandar igual a 1.
'''
# Se generan los ruidos
Señalrandom1 = np.random.normal(0, 1, 5) #ruido de largo 5
Señalrandom2 = np.random.normal(0, 1, 10) #ruido de largo 10
Señalrandom3 = np.random.normal(0, 1, 100) #ruido de largo 100
Señalrandom4 = np.random.normal(0, 1, 1000) #ruido de largo 1000
Señalrandom5 = np.random.normal(0, 1, 10000) #ruido de largo 10000
Señalrandom6 = np.random.normal(0, 1, 100000)#ruido de largo 100000

#A continuación se calculan la media y la desviación estándar de cada ruido generado utilizando las funciones pedidas en el Item 1 y que se encuentran definidas en el módulo "FuncionesTP"(FuncionesTP.py). Se redondea a dos decimales para fines prácticos.
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
dif1=int(round(abs((desvioestandar1-1))*100))
dif2=int(round(abs((desvioestandar2-1))*100))
dif3=int(round(abs((desvioestandar3-1))*100))
dif4=int(round(abs((desvioestandar4-1))*100))
dif5=int(round(abs((desvioestandar5-1))*100))
dif6=int(round(abs((desvioestandar6-1))*100))

# Se presentan los resultados obtenidos en una tabla.
datos=[[5,desvioestandar1,dif1], [10,desvioestandar2,dif2], [100,desvioestandar3,dif3], [1000,desvioestandar4,dif4], [10000,desvioestandar5,dif5],[100000,desvioestandar6,dif6]]
Tabla =   """\
        +------------------------------+
        |        N |        σ |      % |
        |------------------------------|
        {}
        +------------------------------+\
        """
Tabla = (Tabla.format('\n \t'.join("| {:>8d} | {:>8} | {:>6d} |".format(*fila)
 for fila in datos)))
print ("\n")
print("\t \tResultados Item 2  ")
print (Tabla)
