fs = 44100;
t = 0.5;
step = 1/fs;
n= linspace(0,t,fs/2);
N = length(n);
puto=(fs/2)/(N/2);
wsize=1;
f = linspace(0,puto,fs/2);
b = (1/wsize)*ones(1,wsize);
x= 2 + sin(2*pi*10000*n);
y = filter(b,1,x);
caca=fft(y);
realcaca=abs(caca);
losmaxis=maxk(realcaca,10);
rkk=realcaca(1:22050);
plot(f,rkk)
hold on
legend('Input Data','Filtered Data')

% t = linspace(-pi,pi,100);
% rng default  %initialize random number generator
% % x = sin(t) + 0.25*rand(size(t));
% windowSize = 3; 
% b = (1/windowSize)*ones(1,windowSize);
% a = 1;
% y = filter(b,a,x);
% plot(t,x)
% hold on
% plot(t,y)
% legend('Input Data','Filtered Data')