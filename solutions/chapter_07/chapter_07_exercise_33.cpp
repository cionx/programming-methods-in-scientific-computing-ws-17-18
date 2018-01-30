#include<cmath>
#include<iostream>

#define PI 3.14159265358979323846

double simpson(double f(double), double a, double b, unsigned int steps){
  double h = (b-a)/steps;
	double result = f(a);
  double x = a;
	for(int i = 1; i < steps; i++) {
    result += 4*f(x+h/2);
    result += 2*f(x+h);
    x += h;
  }
	result -= f(b);
  result *= h/6;
	return result;
}

int main(){
  std::cout.precision(10);
  std::cout << simpson(sin,0,PI,2000) << std::endl;
	return 0;
}
