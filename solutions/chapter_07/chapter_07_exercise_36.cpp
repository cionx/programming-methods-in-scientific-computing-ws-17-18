#include<cmath>
#include<vector>
#include<iostream>

#include "matrix.cpp"

int main(){
  Matrix B(5,5,0);
  //the matrix:
  
  B(0,0)=-8;B(0,1)=-4; 
  B(1,0)= 16;	B(1,1)=-8;B(1,2)=-4;
  B(2,1)= 16;	B(2,2)=-8;B(2,3)=-4;
  B(3,2)= 16;	B(3,3)=-8;B(3,4)=-4;
  B(4,3)=1;	B(4,4)=-1;
  
  std::vector<double> v(5),z(5);
  
  //the vector:
  z[0]= .125;
  z[1]= .25;
  z[2]= 9.0/16.0;
  z[3]= 1;
  z[4]= 0;
  
  //solving
  v=B.gaussSolve(z);
  //print:
  std::cout << "Exc. 36:\nvalues of u(x) for x = 0, 0.25, ..., 1:" << "\n";
  std::cout << "0 | ";
  for (int i=0; i<4; i++) std::cout << v[i] << " | ";
  std::cout << "\n";
}
