clear all, clc;
%assignment2problem2
C = 10;%define parameters
% options = optimoptions('fmincon', 'Algorithm', 'interior - point') ;
%[x, fval, exitflag, output, Lambda] = fmincon(@(x)problem2(x, C), [.25;6;.1], [], [], [], [], [], [], @(x)constraintp2(x, C), options);
% x %outputs values of x1, x2 and x3
% mu = Lambda.ineqnonlin
% lambda = Lambda.eqnonlin

%as an unconstrained optimization
x =[.25;6;.1];
options = optimoptions('fminunc', 'Algorithm', 'quasi - newton'); % indicate gradient is provided

while C > 1e - 6
C
[x, feval] = fminunc(@(x)problem2(x, C), x, options)

C = C / 10;
end

