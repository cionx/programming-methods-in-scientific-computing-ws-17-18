#include "matrix.hpp"
#include <cmath>
#include <vector>
#include <iostream>
#include <iomanip>



double f_exact(double x){ return 2*sinh(2*x); }; // the exact solution

int main(){
  int n = 7;                    // number of points
  double left = 0;              // left border
  double right = 1;             // right border
  double lb = 0;                // left boundary value
  double rb = exp(2) - exp(-2); // right boundary value
  
  std::vector<double> u(n,0);
  u[0] = lb;
  u[n-1] = rb;
  
  int m = n-2;                      // number of points in the middle
  double h = (right - left)/(n-1);  // length of intervals
  double C = 2 + 4*h*h;
  
  Matrix A = Matrix(m, m, 0);
  for(int i = 0; i < m; i++)
    A(i,i) = C;
  for(int i = 0; i < m-1; i++){
    A(i,i+1) = -1;
    A(i+1,i) = -1;
  }
  std::vector<double> b(m,0);
  b[0] = u[0];
  b[m-1] = u[n-1];
  std::vector<double> u_inner = A.gaussSolve(b);
  for(int i = 0; i < m; i++){
    u[i+1] = u_inner[i];
  }
  
  std::cout << std::fixed;
  std::cout << std::setprecision(8);
  // x values
  std::cout << "x\t\t| ";
  for(int i = 0; i < n; i++)
    std::cout << (left + i*h) << "\t| ";
  std::cout << std::endl;
  // approx values
  std::cout << "approx(x)\t| ";
  for(int i = 0; i < n; i++)
    std::cout << u[i] << "\t| ";
  std::cout << std::endl;
  // exact values
  std::cout << "exact(x)\t| ";
  for(int i = 0; i < n; i++)
    std::cout << f_exact(left + i*h) << "\t| ";
  std::cout << std::endl;

}
