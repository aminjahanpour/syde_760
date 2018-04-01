%main program to run the small illustartive
%refinery problem

clear all;
close all
x = zeros(8,1);
vlb=zeros(8,1);
options=optimset('Algorithm','sqp')
%x = constr('refrecodem',x,options,vlb)
meanobj=[];
stdobj=[];
xsol=[];
thets=[];
for thet=0.0:.05:1.5;
    thets=[thets;thet]
x = fmincon(@(x)refrecodemobj(x,thet),x,[],[],[],[],vlb,[],@(x)refrecodemcon(x),options);
xsol=[xsol x];
[m,v]=refrecodestats(x,thet);
meanobj=[meanobj;m];
stdobj=[stdobj;sqrt(v)];
end
plot(stdobj,meanobj)
title('Efficient Frontier')
xlabel('Risk - Standard dev.')
ylabel('Expected Net Benefits')
% [f,g]=refinery(x);
% f=-f; %for maximization
% %plotting the graphical solution
% pg=0:20;
% crf=(f-19*pg)/3.41;
% 
% plot(crf,pg,'r.') %objective function plotted
% hold
% crc=(10+pg)/.27;
% plot(crc,pg)
% plot(100*ones(1,length(pg)),pg)
% plot(x(1),x(2),'r*')
% cr=0:100;
% plot(cr,10*ones(1,length(cr)))
% fill([100,100,74.041],[10,17,10],'g')