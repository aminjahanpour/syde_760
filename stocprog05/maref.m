%main program to run the small illustartive
%refinery problem

clear;
options(1)=1;
x = zeros(2,1);

%x = constr('refinery',x,options)
x = fmincon('refineryobj',x,[],[],[],[],[],[],'refinerycon')

[f,g]=refinery(x);
f=-f; %for maximization
%plotting the graphical solution
pg=0:20;
crf=(f-19*pg)/3.41;

plot(crf,pg,'r.') %objective function plotted
hold
crc=(10+pg)/.27;
plot(crc,pg)
plot(100*ones(1,length(pg)),pg)
cr=0:100;
plot(cr,10*ones(1,length(cr)))
fill([100,100,74.041],[10,17,10],'g')
title('Deterministic Optimization: Feasbile region green shaded')
xlabel('CRUDE')
ylabel('PG')