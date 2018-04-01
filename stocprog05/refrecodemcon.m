%Refiner slp for a small illustrative problem
function [g,geq] = refrecodemcon(x)
crude = x(1);
pg = x(2);
sf1 = x(3);
su1 = x(4);
sf2 = x(5);
su2 = x(6);
sf3 = x(7);
su3 = x(8);



%Next three are equality constraints 
geq(1) = -pg-sf1+su1+6;   % The equality constraints are also multiplied by negative like the objective function
geq(2) = -pg-sf2+su2+10;
geq(3) = -pg-sf3+su3+14;
%and then inequalities
g(1) = crude -100;      % <= 0
g(2) = -0.27*crude+pg+10; 


