%Refiner slp for a small illustrative problem
function [f,g] = refrecodem(x)
crude = x(1);
pg = x(2);
sf1 = x(3);
su1 = x(4);
sf2 = x(5);
su2 = x(6);
sf3 = x(7);
su3 = x(8);
csf = 22;
csu = 20;
%f = 0.0341*crude + 0.19*pg; %original
%f = 3.41*crude + 19*pg; %original*100- deterministic
f = 3.41*crude + 19*pg-0.25*(sf1*csf+su1*csu)-...
                        .5*(sf2*csf+su2*csu)-...
                      0.25*(sf3*csf+su3*csu);


f = -f; %for maximization

%Next three are equality constraints and they must
%go before inequalities in MATLAB constr
g(1) = -pg-sf1+su1+6;   % The equality constraints are also multiplied by negative like the objective function
g(2) = -pg-sf2+su2+10;
g(3) = -pg-sf3+su3+14;
%inequalities
g(4) = crude -100;      % <= 0
g(5) = -0.27*crude+pg+10; 

