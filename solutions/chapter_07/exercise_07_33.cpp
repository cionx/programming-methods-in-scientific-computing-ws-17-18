#include <cmath>
#include <iostream>
#include <iomanip>

#define PI 3.14159265358979323846

double simpson(double f(double), double a, double b, int n){
  double h = (b-a)/n;     // length of subintverals
	double result = f(a);   // current sum
  double x = a;           // left border of current subinterval
	for(int i = 1; i < n; i++) {
    result += 4*f(x+h/2);
    result += 2*f(x+h);
    x += h;
  }
	result -= f(b);
  result *= h/6;
	return result;
}

int main(){
  double eps = 1.E-6;
  int n = 0;
  double y = 0;
  do {
    n++;
    y = simpson(sin,0,PI,n);
  }
  while( 2-y >= eps );
  std::cout << std::fixed << std::setprecision(10);
  std::cout << simpson(sin,0,PI,n) << std::endl;
	return 0;
}
