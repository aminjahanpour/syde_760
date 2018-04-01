%constraints problem 2
function[c,ceq]=constraintp2(x,C)
ceq(1)=x(1)-x(3);
c(1)=1-x(1)*x(2);
c(2)=-x(1)-x(2)^2;
c(3)=x(1)-0.5;