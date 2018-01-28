n = 20;
x = 0 : n;
y = x + 2*(rand(size(x)) - 0.5);

A = zeros(length(x), 2);
A(:,1) = x';
A(:,2) = ones(length(y),1);

a = (A\y')';

hold on;
plot(x, y, '*');
plot(x, a(1)*x + a(2));
