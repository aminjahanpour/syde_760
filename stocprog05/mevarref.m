%Refiner slp for a small illustrative problem
function [meancon,varcon] = ccdemref(x)
crude = x(1);
pg = x(2);
%f = 0.0341*crude + 0.19*pg; %original
f = 3.41*crude + 19*pg; %original*100
meancon = 0.27*crude-pg;
varcr=.001; varpg=.001;
varcon=(varcr*crude^2+varpg*pg^2);

%feasiblities
g(1) = crude -100;
g(2) = -pg+10;
