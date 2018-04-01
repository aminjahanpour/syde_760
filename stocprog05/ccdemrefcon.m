%Refiner slp for a small illustrative problem
function [g,geq] = ccdemrefcon(x)
crude = x(1);
pg = x(2);
%f = 0.0341*crude + 0.19*pg; %original


g(1) = crude -100;
g(2) = -pg+10;
g(3) = -0.27*crude+pg+10; 
%for CC add the following
zalpha = -1.75;    % = 4 % prob of exceedance = corrosponding to 96 % probability of non-exceedance
varcr=.001; varpg=.001;
g(3)=g(3)-zalpha*sqrt(varcr*crude^2+varpg*pg^2);
geq=[];
