%  size = 2000;
%  iter = 2000;
size = 500;
iter = 400;
cutoff = 2;

xlimit = [-2, 0.5];
ylimit = [1, -1];
%  xlimit = [-0.7, -0.8];
%  ylimit = [0.1, 0.2];

x = linspace(xlimit(1), xlimit(2), size);
y = linspace(ylimit(1), ylimit(2), size);

[xx, yy] = meshgrid(x, y);
cc = xx + i*yy;

zz = zeros(length(y), length(x));
nn = zeros(length(y), length(x));

for j = 1 : iter
  zz = zz.^2 + cc;
  nn += (zz < 2);
end

%  nn = log(nn);

%  colormap( [jet();flipud( jet() );0 0 0] );
imagesc(abs(nn));
axis off;
