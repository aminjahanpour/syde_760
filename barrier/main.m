r = 10
x =[0 0];;
    fres = 1;
oldx = x;
eps1 = 1e - 6;
iter = 0;
xsol =[];
rs =[];
fsol =[];
while fres > eps1
f = 0.5 * (x(1)^2 + x(2)^2);
fsol =[fsol; f];
iter = iter + 1

[x] = fsolve(@(x) barrex1(x, r), x)
xsol =[xsol;x];
rs =[rs;r];

r = r / 2;

fres = norm(x - oldx)
oldx = x;

end %do