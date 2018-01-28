function poisson_solver(f,g,m)
  
  n = m-1;
  h = 1/(n+1);
  
  A = gallery('poisson',n);
  
% construction of grid
  lin = linspace(0,1,n+2);
  [x,y] = meshgrid(lin);
  
% initialize solution matrix with 0s
  u = zeros(n+2, n+2);

% insert boundary values
  u(:,1) = arrayfun(g, x(:,1), y(:,1));
  u(:,n+2) = arrayfun(g, x(:,n+2), y(:,n+2));
  u(1,:) = arrayfun(g, x(1,:), y(1,:));
  u(n+2,:) = arrayfun(g, x(n+2,:), y(n+2,:));
  
% initialize solution matrix with 0s
  F = zeros(n, n);

% insert function values f_ij
  F = arrayfun(f, x(2:n+1,2:n+1), y(2:n+1,2:n+1));

% modify boundary-adjacent values
  F(:,1) += ( u(2 : n+1, 1) / h^2 );   % left column
  F(:,n) += ( u(2 : n+1, n+2) / h^2 ); % right column
  F(1,:) += ( u(1, 2 : n+1) / h^2 );   % top row
  F(n,:) += ( u(n+2, 2 : n+1) / h^2 ); % bottom row
  
% as column-vector
  F = reshape(F, n*n, 1);
  
% solve the inner points
  u_inner = A \ (h*h*F);
  
% store values in solution-matrix
  u(2:n+1, 2:n+1) = reshape(u_inner,n,n);
  
% plot that shit
  mesh(x,y,u, 'LineWidth', 1);
  xlabel('x');
  ylabel('y');
end



% (1)

f = @(x,y) 1.25 * exp(x + y/2);
g = @(x,y) exp(x + y/2);

poisson_solver(f, g, 100);



% (2)

f = @(x,y) 20 * cos(3*pi*x) * sin(2*pi*y);
function z = g(x,y)
  z = 0;
  if x == 0
    z = y.^2;
  elseif y == 0
    z = x.^3;
  elseif (y == 1) || (x == 1)
    z = 1;
  end
end

poisson_solver(f, @g, 100);
