function g = fun(x, r);

mu0 = 2;
rbar = r / mu0;
%g(1) = x(1) + (x(1) - 1) / r;
%g(2) = x(2) - r / (x(2) + 1);
%note that x(3) is lambda and x(4) is mu
g(1) = mu0 * (x(1) - x(3));
g(2) = mu0 * (x(2) - x(4));
g(3) = (x(1) - 1) + rbar * x(3);
g(4) = x(4) * (x(2) + 1) - mu0^2 * rbar;
g(5) = mu0^2 + (x(3)^2) + (x(4)^2) - x(5)^2; %x(5) is beta0