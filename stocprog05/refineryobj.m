%Refiner slp for a small illustrative problem
function f = refineryobj(x)
crude = x(1);
pg = x(2);
%f = 0.0341 * crude + 0.19 * pg; %original
f = 3.41 * crude + 19 * pg; %original * 100

f = -f; %for maximization

