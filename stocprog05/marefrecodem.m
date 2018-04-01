%main program to run the small illustartive
%refinery problem

clear;
options(1)=1;
options(13)=3; %to specify the number of equalities
x = zeros(8,1);
vlb=zeros(8,1);

%x = constr('refrecodem',x,options,vlb)
x = fmincon('refrecodemobj',x,[],[],[],[],vlb,[],'refrecodemcon')

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
plot(x(1),x(2),'r*')
cr=0:100;
plot(cr,10*ones(1,length(cr)))
fill([100,100,74.041],[10,17,10],'g')