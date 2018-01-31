x_interval = [0 10];  % interval on which we work

dydx = @(x,y) [y(2) y(3) -1/y(1)]';
y0 = [1 0 0];         % initial values

[x,y] = ode45(dydx, x_interval, y0);
u = y(:,1);

plot(x,u);
