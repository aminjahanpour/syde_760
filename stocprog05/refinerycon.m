%Refiner slp for a small illustrative problem
function[g, geq] = refinerycon(x)
crude = x(1);
pg = x(2);

g(1) = crude - 100;
g(2) = -pg + 10;
g(3) = -0.27 * crude + pg + 10;
geq =[];
