#include<cmath>
#include<iostream>
#include<functional>

#define PI 3.14159265358979323846f 

double simpson(std::function<double(double)> f, double a, double b, unsigned int steps){
	double delta = (b-a)/(2*steps);
	double result = f(a);
	for(int i=1;i<steps;i++) result += 2*f(a+2*i*delta);
	for(int i=0;i<steps;i++) result += 4*f(a+(2*i+1)*delta);
	result += f(b);
	result *= delta/3;
	return result;
}

int main(){
	std::cout << simpson([](double x){return sin(x);},0,PI,99999);
	return 0;
}