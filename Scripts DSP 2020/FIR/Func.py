import numpy as np
from scipy import signal

def beta_K(A):
    A=abs(A)
    beta=0
    if A>=21 and A<=50:
        beta=0.5842*((A-21)**(0.4)) + 0.07886*(A-21)
    elif A > 50:
        beta=0.1102*(A-8.7)
    return beta
def Kaiser_M(A,deltaw):
    M=int((A-8)/(2.285*deltaw*np.pi))+1
    return M
def iLP(M,wc):
    n=np.linspace(0,M,M+1)
    n0=M/2
    h=np.sinc(wc*(n-n0))*wc
    return h,n

def iHP(M,wc):
    n=np.linspace(0,M,M+1)
    n0=(M/2)
    PT=np.sinc(1*(n-n0))*1
    LP=np.sinc(wc*(n-n0))*wc
    h=PT-LP
    return h,n

def iBP(M,wc1,wc2):
    n=np.linspace(0,M,M+1)
    n0=(M/2)
    LP1=np.sinc(wc1*(n-n0))*wc1
    LP2=np.sinc(wc2*(n-n0))*wc2
    h=LP2-LP1
    return h,n

def iBS(M,wc1,wc2):
    n=np.linspace(0,M,M+1)
    n0=(M/2)
    LP=np.sinc(wc1*(n-n0))*wc1
    LP1=np.sinc(1*(n-n0))*1
    LP2=np.sinc(wc2*(n-n0))*wc2
    BP=LP1-LP2
    h=LP+BP
    return h,n
