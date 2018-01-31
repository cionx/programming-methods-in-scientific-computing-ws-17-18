#include <cmath>
#include <iostream>

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
  std::cout.precision(10); // set output precision
  std::cout << simpson(sin,0,PI,2000) << std::endl;
	return 0;
}
