#include "polynomial.hpp"
#include <iostream>



int main(){
  Polynomial p({1, 2, 3}), q({0, 2, 1});
  std::cout << "P: ";
  p.print();
  std::cout << "The value P(2): " << p(2) << std::endl;
  std::cout << "-P: ";
  (-p).print();
  std::cout << "Q: ";
  q.print();
  std::cout << "P*Q: ";
  (p*q).print();
  std::cout << "P+Q: ";
  (p+q).print();
  std::cout << "Test P = Q: " << (p == q) << std::endl;
  std::cout << "Test P = P: " << (p == p) << std::endl;
}
