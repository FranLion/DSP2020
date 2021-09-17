import numpy as np
import math

def convLin(x,h):
    X=np.fft.fft(x)
    H=np.fft.fft(h)
    Y=X*H
    y=np.fft.ifft(Y)
    return y

def convCirc(x,h):
    L=len(x)
    M=len(h)
    xc=np.append(x,np.zeros(M-1))
    hc=np.append(h,np.zeros(L-1))
    X=np.fft.fft(xc)
    H=np.fft.fft(hc)
    Y=X*H
    y=np.fft.ifft(Y)
    return y

def conv_sum(x1,nx1,x2,nx2):
    # nnx1 = np.arange(0,len(nx1))
    # nnx2 = np.arange(0,len(nx2))
    # n1 = nnx1[0]
    # n2 = nnx1[-1]
    # n3 = nnx2[0]
    # n4 = nnx2[-1]
    nny = np.arange(0,len(nx1)+len(nx2)-1)
    ny = np.arange(0,len(x1)+len(x2)-1) + nx1[0]+nx2[0]
    y = np.convolve(x1, x2)
    return y[nny], ny
