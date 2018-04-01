%Refiner slp for a small illustrative problem
function [fbar varz] = refrecodestats(x,thet)
crude = x(1);
pg = x(2);
sf1 = x(3);
su1 = x(4);
sf2 = x(5);
su2 = x(6);
sf3 = x(7);
su3 = x(8);
csf =20;
csu = 20;
%f = 0.0341*crude + 0.19*pg; %original
%f = 3.41*crude + 19*pg; %original*100- deterministic
z(1)=(sf1*csf+su1*csu);
z(2)=(sf2*csf+su2*csu);
z(3)=(sf3*csf+su3*csu);
p=[0.25 0.5 0.25];
zbar=p*z';
z2bar=p*(z.^2)';
varz=z2bar-zbar^2';
                  
fbar = 3.41*crude + 19*pg-zbar;

