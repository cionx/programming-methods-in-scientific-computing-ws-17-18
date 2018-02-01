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
  std::vector<double> coeff = gaussSolve(V,values);
  Polynomial p = Polynomial(coeff);
  return p;
}

int main(){
  int n = 5;            // number of points
  double left = -1.5;   // left interval boundary
  double right = 1.5;   // right interval boundary
  double h = (right - left)/(n-1);  // length of subintervals
  
  
  std::vector<double> v(n), w(n);
  double x = left;            // current x value
  for(int i = 0; i < n; i++){ // creates coordinates to be interpolated
    v[i] = x;
    w[i] = tan(x);
    x += h;
  }
  Polynomial p = interpol(v,w);
  p.print();
  
  return 0;
}
