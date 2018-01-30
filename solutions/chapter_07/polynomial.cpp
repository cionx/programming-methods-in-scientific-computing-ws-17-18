#include "polynomial.hpp"
#include <cmath>
#include <vector>
#include <iostream>
#include <string>

#define EPS 1.E-14



Polynomial::Polynomial(std::vector<double> coefficients){
  coeff = coefficients;
}

Polynomial::Polynomial(double c){
  coeff = {c};
}

Polynomial Polynomial::operator*(Polynomial p){
  int d1 = coeff.size();
  int d2 = p.coeff.size();
  std::vector<double> result(d1+d2-1, 0);
  for(int i = 0 ; i < d1; i++){
    for(int j = 0; j < d2; j++){
      result[i+j] += coeff[i]*p.coeff[j];
    }
  }
  return Polynomial(result);
}

Polynomial Polynomial::operator+(Polynomial p){
  int d1 = coeff.size();
  int d2 = p.coeff.size();
  std::vector<double> result(std::max(d1,d2), 0);
  for(int i = 0; i < d1; i++)
    result[i] += coeff[i];
  for(int j = 0; j < d2; j++)
    result[j] += p.coeff[j];
  return Polynomial(result);
}

Polynomial Polynomial::operator-(Polynomial p){
  int d1 = coeff.size();
  int d2 = p.coeff.size();
  std::vector<double> result(std::max(d1,d2), 0);
  for(int i = 0; i < d1; i++)
    result[i] += coeff[i];
  for(int j = 0; j < d2; j++)
    result[j] -= p.coeff[j];
  return Polynomial(result);
}

Polynomial Polynomial::operator-(){
  int d = coeff.size();
  std::vector<double> result;
  for(int i = 0; i < d; i++)
    result.push_back(-coeff[i]);
  return Polynomial(result);
}

double Polynomial::operator()(double x){
  double result = 0;
  int d = coeff.size();
  for(int i = 0; i < d; i++)
    result += coeff[i]*pow(x,i);
  return result;
}

Polynomial Polynomial::clean(){
  int d = coeff.size();
  std::vector<double> result(d,0);
  for(int i = 0; i < d; i++)
    if(std::abs(coeff[i]) > EPS)
      result[i] = coeff[i];
    return Polynomial(result);
}

bool Polynomial::operator==(Polynomial p){
  Polynomial diff = (*this) - p;
  diff = diff.clean();
  int d = diff.coeff.size();
  for(int i = 0; i < d; i++)
    if(diff.coeff[i] != 0)
      return false;
    return true;
}

void Polynomial::print(){
  Polynomial p = (*this).clean();
  
  if(p == Polynomial(0))
    std::cout << "0";
  else{
    int d = p.coeff.size();
    bool first = true;          // if other coefficients have already been printed
    double c;                   // current coefficient
    std::string prefix, power;  // prefix and power for the summands
    for(int i = d-1; i >= 0; i--){
      c = p.coeff[i];
      prefix, power = "";
      
      if (c > 0){
        if (!first)
          prefix = " + ";
      }
      else if (c < 0){
        if(!first)
          prefix = " - ";
        else
          prefix = "-";
      }
      
      if (i >= 2)
        power = "x^" + std::to_string(i);
      else if(i == 1)
        power = "x";
      
      if(c != 0){
        std::cout << prefix << (c > 0 ? c : -c) << power;
        first = false;
      }
    }
    std::cout << std::endl;
  }
}
