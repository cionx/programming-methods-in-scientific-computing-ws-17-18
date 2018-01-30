#include "quaternion.hpp"
#include<iostream>


int main(){
  Quaternion q1(1,2,3,4), q2(2,3,4,5);
  std::cout << "Q1: ";
  q1.print();
  std::cout << "Negative of Q1: ";
  (-q1).print();
  std::cout << "Conjugate of Q1: ";
  q1.conjugate().print();
  std::cout << "Absolute value of Q1: " << q1.abs() << std::endl;
  std::cout << "Q2: ";
  q2.print();
  std::cout << "Test for Q1 = Q2: " << (q1 == q2) << std::endl;
  std::cout << "Test for Q1 = Q1: " << (q1 == q1) << std::endl;
  std::cout << "Q1 * Q2: ";
  (q1 * q2).print();
  std::cout << "Q2 * Q1: ";
  (q2 * q1).print();
  std::cout << "Q1 / Q2: ";
  (q1 / q2).print();
  std::cout << "(Q1 / Q2) * Q2: ";
  ((q1/q2)*q2).print();
  std::cout << "Hamilton equations:" << std::endl;
  Quaternion i = Quaternion({0,1,0,0});
  Quaternion j = Quaternion({0,0,1,0});
  Quaternion k = Quaternion({0,0,0,1});
  std::cout << "i^2 = ";
  (i*i).print();
  std::cout << "j^2 = ";
  (j*j).print();
  std::cout << "k^2 = ";
  (k*k).print();
  std::cout << "ijk = ";
  (i*j*k).print();
  
  return 0;
}
