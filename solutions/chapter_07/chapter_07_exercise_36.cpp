#include "matrix.hpp"
#include <cmath>
#include <vector>
#include <iostream>
#include <iomanip>

double f_exact(double x){
  return -0.659305*exp(x) + 0.0030549*exp(4*x) + x*x/4 + 5*x/8 + 21/32.0;
}

int main(){
  int n = 24;
  
  double left = 0;    // left interval value
  double right = 1;   // right interval value
  double lb = 0;      // left boundary conditition for u
  double rb = 0;      // right boundary condition for u'
  
  double h = (right - left)/(n-1);  // distance between points
  std::vector<double> u(n+1,0);     // additional point u[n] to the right of the interval
  u[0] = lb;
  
  Matrix A = Matrix(n,n);           // LGS for the values u[1] to u[n]
  std::vector<double> b(n,0);
  
  A(0,0) = -2/(h*h) + 5/h + 4;
  A(0,1) = 1/(h*h) - 5/h;
  for(int i = 1; i < n; i++){
    A(i,i-1) = 1/(h*h);
    A(i,i)   = -2/(h*h) + 5/h + 4;
    A(i,i+1) = 1/(h*h) - 5/h;
  }
  A(n-1, n-2) = -1;
  A(n-1, n-1) =  1;
  
  double x = 0;
  for(int i = 0; i < n-1; i++){
    x += h;
    b[i] = x*x;
  }
  b[0] += -u[0]/(h*h);
  b[n-1] = h*rb;
  
  std::vector<double> u_right = A.gaussSolve(b);
  
  for(int i = 0; i < n; i++)
    u[i+1] = u_right[i];
  
  std::cout << std::fixed;
  std::cout << std::setprecision(6);
//  list of results
  x = 0; //  current point, variable already initialized before
  std::cout << "x\t\t  approx\t\t  exact" << std::endl;
  for(int i = 0; i < n; i++){
    std::cout << x
              << "\t| "
              << u[i]
              << "\t| "
              << f_exact(x)
              << std::endl;
    x += h;
  }
}
