#include<cmath>
#include<iostream>
#include<functional>
#include "matrix.cpp"
#include "poly.cpp"

#define PI 3.14159265358979323846f 

Matrix vandermonte(std::vector<double> v){
	int n = v.size();
	Matrix m = Matrix(n,n);
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			m(i,j) = pow(v[i],j);
		}
	}
	return m;
}

Matrix inversevandermonte(std::vector<double> v){
	Matrix m = vandermonte(v);
	return m.invert();
}

Polynomial interpol(std::vector<double> points, std::vector<double> values){
	return Polynomial(vandermonte(points).gaussSolve(values));
}
double fun(double x){
	return sin(x);
}

int main(){
	int n = 9;
	std::vector<double> v(n),w(n);
	for(int i=0;i<n;i++){
		v[i] = i;
		w[i] = fun(i);
	}
	interpol(v,w).clean().print();
	return 0;
}
