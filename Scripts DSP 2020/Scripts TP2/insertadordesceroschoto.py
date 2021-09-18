import numpy as np

a=[1,2,3,5,6,7,4,2]

def intercaladordeceros(a,c):

    k=len(a)

    for i in range(0,k-1):

        d=np.insert(0,a,i)

    return d

d=intercaladordeceros(a,3)

print("d",d)
