fs = 44100;
t = 0.5;
step = 1/fs;
n= linspace(0,t,fs);
N = length(n);
puto=(fs/2)/(N/2);
f = linspace(0,fs/2,puto);
x= 2 + sin(2*pi*10000*n);
% y= filter(3,'linear',x);
y = filter(f,3,x);
caca=fft(y);
realcaca=abs(caca);
losmaxis=maxk(realcaca,2);
rkk=realcaca(1:22051);
plot(f,rkk);