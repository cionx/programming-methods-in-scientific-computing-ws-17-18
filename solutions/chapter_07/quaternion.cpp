#include "quaternion.hpp"
#include<vector>
#include<iostream>

#define EPS 1.E-14


Quaternion::Quaternion(){
  coord = {0,0,0,0};
}

Quaternion::Quaternion(double x, double i, double j,double k){
  coord = {x,i,j,k};
}

Quaternion::Quaternion(double q[4]){
  coord = {q[0], q[1], q[2], q[3]};
}

Quaternion::Quaternion(double x){
  coord = {x, 0, 0, 0};
}

Quaternion Quaternion::operator+(Quaternion q){
  double result[4];
  for(int i = 0 ; i < 4; i++)
    result[i] = coord[i] + q.coord[i];
  return Quaternion(result);
}

Quaternion Quaternion::operator-(){
  double result[4];
  for(int i = 0; i < 4; i++)
    result[i] = -coord[i];
  return Quaternion(result);
}

Quaternion Quaternion::operator-(Quaternion q){
  double result[4];
  for(int i = 0; i < 4; i++)
    result[i] = coord[i] - q.coord[i];
  return Quaternion(result);
}

Quaternion Quaternion::operator*(Quaternion q){
  double r, x, y, z;
  r =   coord[0] * q.coord[0]
  - coord[1] * q.coord[1]
  - coord[2] * q.coord[2]
  - coord[3] * q.coord[3];
  x =   coord[0] * q.coord[1]
  + coord[2] * q.coord[3]
  - coord[3] * q.coord[2]
  + coord[1] * q.coord[0];
  y =   coord[0] * q.coord[2]
  - coord[1] * q.coord[3]
  + coord[3] * q.coord[1]
  + coord[2] * q.coord[0];
  z =   coord[0] * q.coord[3]
  + coord[1] * q.coord[2]
  - coord[2] * q.coord[1]
  + coord[3] * q.coord[0];
  return Quaternion({r, x, y, z});
}

double Quaternion::abs(){
  double squared =  coord[0] * coord[0]
  + coord[1] * coord[1]
  + coord[2] * coord[2]
  + coord[3] * coord[3];
  return sqrt(squared);
}

Quaternion Quaternion::conjugate(){
  double result[] = {coord[0], -coord[1], -coord[2], -coord[3]};
  return Quaternion(result);
}

Quaternion Quaternion::operator/(double r){
  double result[4];
  for(int i = 0; i < 4; i++)
    result[i] = coord[i]/r;
  return Quaternion(result);
}

Quaternion Quaternion::inverse(){
  double norm = (*this).abs() * (*this).abs();
  return (*this).conjugate()/norm;
}

Quaternion Quaternion::operator/(Quaternion q){
  return (*this) * q.inverse();
}

Quaternion Quaternion::clean(){
  double result[] = {0,0,0,0};
  for(int i = 0; i < 4; i++)
    if(std::abs(coord[i]) > EPS)
      result[i] = coord[i];
  return Quaternion(result);
}

bool Quaternion::operator==(Quaternion q){
  Quaternion diff = (*this) - q;
  diff = diff.clean();
  for(int i = 0; i < 4; i++){
    if(diff.coord[i] != 0)
      return false;
  }
  return true;
}

void Quaternion::print(){
  if(*this == Quaternion())
    std::cout << "0" << std::endl;
  else{
    bool first = true;
    char symbol[] = {'\0', 'i', 'j', 'k'};
    for(int i = 0; i < 4; i++){
      if(coord[i] < 0){
        if (first)
          std::cout << "-";
        else
          std::cout << " - ";
        std::cout << (-coord[i]) << symbol[i];
        first = false;
      }
      else if (coord[i] > 0) {
        if(!first)
          std::cout << " + ";
        std::cout << coord[i] << symbol[i];
        first = false;
      }
    }
    std::cout << std::endl;
  }
}
