n = 20;     % number of points
x = 0 : n;  % x values
y = x + 2*(rand(size(x)) - 1);  % y values

A = zeros(length(x), 2);    % initialize zero matrix
A(:,1) = x';                % insert x values in first column
A(:,2) = ones(length(y),1); % insert ones into second column

a = (A\y')';  % find coefficients of regression line

hold on;                % to plot both points and the line 
plot(x, y, '*');        % plotting the points
plot(x, a(1)*x + a(2)); % plotting the line
set(h, 'PaperUnits','centimeters');
set(h, 'Units','centimeters');
pos=get(h,'Position');
set(h, 'PaperSize', [pos(3) pos(4)]);
set(h, 'PaperPositionMode', 'manual');
set(h, 'PaperPosition',[0 0 pos(3) pos(4)]);
print('-dpdf','exercise_08_39_figure_test.pdf')
