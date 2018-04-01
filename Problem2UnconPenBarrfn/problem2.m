%Problem 2
function f=problem2(x,C)
fx=100*(x(2)-x(1)^2)^2+(1-x(1))^2+(x(1)-x(3))^2;

ceq(1)=x(1)-x(3);
c(1)=1-x(1)*x(2);
c(2)=-x(1)-x(2)^2;
c(3)=x(1)-0.5;

penfn=(ceq(1).^2)/C;
barfn= -C*sum (log(-c));
f = fx+penfn+barfn;