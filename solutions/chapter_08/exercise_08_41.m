%  untested

%  u'' = -2;
%  u(0) = 0, u(5) = 3;
%  
%  dydx = @(x,y) [y(2) -2]';
%  bvs = @(lb, rb)[lb(1) rb(1)-3]';
%  sol_init = bvpinit([0 5], [0 0]);
%  
%  sol = bvp4c(dydx, bvs, sol_init);
%  x = linspace(0,5);
%  w = deval(sol, x, 1);
%  u = w(1,:);
%  
%  plot(x,u);



%  u'' - 2 u' + u = 0
%  u(0) = u(1) = 0

dydx = @(x,y) [y(2), 2 * y(2) + y(1)];
bvs = @(lb, rb)[lb(1) rb(1)];
sol_init = bvpinit([0 5] [0 0]);

sol = bvp4c(dydx, bvs, sol_init);
x = linspace(0,1);
w = deval(sol, x, 1);
u = w(1,:);

plot(x,u);
