from FuncionesTP import *
# blackman=np.blackman(1000)
# RF_blackman=(np.fft.fft(blackman))
# RFdB_B=np.clip(20*np.log10(RF_blackman/max(RF_blackman)),-100,50)

T=1000
#f= np.linspace(-1*np.pi,np.pi,T)
f=np.arange(-1*np.pi,np.pi,2*np.pi/(192000-1))
print(len(f))
a0=0.42
a1=0.5
a2=0.08
H1=(np.sin(f*T/2)/np.sin(f/2))
H2=(np.exp(-1j*(np.pi)/T)*(np.sin((T*f/2)-np.pi)/np.sin((f-(2*np.pi/T))/2)))+((np.exp(1j*(np.pi)/T))*(np.sin((f+(2*np.pi/T))*T/2)/np.sin((f+(2*np.pi/T))/2)))
H3=(np.exp(1j*(2*np.pi)/T)*(np.sin((f-(4*np.pi/T))*T/2)/np.sin((f-(4*np.pi/T))/2)))+(np.exp(1j*(2*np.pi)/T)*(np.sin((f+(4*np.pi/T))*T/2)/np.sin((f+(4*np.pi/T))/2)))
RF_blackman=abs(np.exp(-1j*((T-1)*f)/2)*(a0*H1)-(a1*H2)+(a2*H3))
RFdB_B=np.clip(20*np.log10(RF_blackman/max(RF_blackman)),-100,50)
plt.figure(1)
plt.plot(RFdB_B)
# plt.plot(np.fft.fftshift(RF_blackman),'g')
plt.show()
