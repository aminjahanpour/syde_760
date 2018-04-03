x0 =[0; 0];

[x, obj, info, iter, nf, lambda] = sqp (x0, @obj, @eq, @g)

