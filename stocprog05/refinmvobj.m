%Refiner slp for a small illustrative problem
function f = refinmvobj(x)
crude = x(1);
pg = x(2);
%f = 0.0341*crude + 0.19*pg; %original


%for markovitz, minimize variance
varcrude =1;
varpg = 9;
f = varcrude*crude^2+varpg*pg^2;