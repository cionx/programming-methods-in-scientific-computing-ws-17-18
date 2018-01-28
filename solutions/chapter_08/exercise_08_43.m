function poisson_solver(f, g, xinter, yinter, m)
  
  n = m-1;
  h = 1/(n+1);
  
  A = gallery('poisson',n);
  
% construction of grid
  xlin = linspace(xinter(1), xinter(2), n+2);
  ylin = linspace(yinter(1), yinter(2), n+2);
  [x,y] = meshgrid(xlin, ylin);
  
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



f = @(x,y) x^2 + y^2;
g = @(x,y) x*(2-x) + y*(1-y);

poisson_solver(f, g, [0,2], [0,1], 100);
