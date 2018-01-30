#include "matrix.hpp"
#include "polynomial.hpp"
#include <cmath>
#include <iostream>

#define PI 3.14159265358979323846

Matrix vandermonte(std::vector<double> v){
  int n = v.size();
  Matrix V = Matrix(n,n);
  for(int i=0; i < n; i++)
    for(int j = 0; j < n; j++)
      V(i,j) = pow(v[i],j);
  return V;
}

Polynomial interpol(std::vector<double> points, std::vector<double> values){
  Matrix V = vandermonte(points);
  std::vector<double> coeff = V.gaussSolve(values);
  Polynomial p = Polynomial(coeff);
  return p;
}

int main(){
  int n = 5;
  double left = -1.5;
  double right = 1.5;
  double h = (right - left)/(n-1);
  
  
  std::vector<double> v(n), w(n);
  double x = left;
  for(int i = 0; i < n; i++){
    v[i] = x;
    w[i] = tan(x);
    x += h;
  }
  Polynomial p = interpol(v,w);
  p.print();
  
  return 0;
}
