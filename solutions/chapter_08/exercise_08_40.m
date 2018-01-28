# u * u''' = -1
# u(0) = 1,
# u'(0) = u''(0) = 0

x_interval = [0 10];

dydx = @(x,y) [y(2) y(3) -1/y(1)]';
y0 = [1 0 0];

[x,y] = ode45(dydx, x_interval, y0);
u = y(:,1);

plot(x,u);
