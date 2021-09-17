import scipy.signal as sp

b=[1,0.5]
a=[-0.5,]
coefs, polos, lineal = sp.residuez(b, a, 0.001)


print('Las fracciones simples son: ',coefs,polos,lineal)
