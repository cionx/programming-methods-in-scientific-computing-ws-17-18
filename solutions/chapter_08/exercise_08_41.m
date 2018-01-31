dydx = @(x,y) [y(2), 2 * y(2) - y(1)];  % the differential equation
bvs = @(lb, rb)[lb(1), rb(1)]';         % boundary conditions
sol_init = bvpinit([0 1], [0 0]);       % assumptions to work with
sol = bvp4c(dydx, bvs, sol_init);       % solve the bvp

% plotting the solution
x = linspace(0,1);
w = deval(sol, x, 1);
u = w(1,:);
plot(x,u); % the zero function
