#include<cmath>
#include<vector>
#include<iostream>

#include "matrix.cpp"

int main(){
	//first ODE (EXC 35):
	double u0=0;
	double u4=exp(2)-exp(-2);
	Matrix A(3,3,0);
	// double h=.25;
	double c=2.25;  // = (4*h*h)+2; //auxiliary constant
	//the matrix:
	
	A(0,0)= c; 	A(0,1)=-1; 
	A(1,0)=-1;	A(1,1)= c;	A(1,2)=-1;
				A(2,1)=-1;	A(2,2)= c;
	
	std::vector<double> u(3),y(3);
	
	//the vector:

	y[0]= u0;
	y[1]= 0;
	y[2]= u4;
	
	//solving:
	u=A.gaussSolve(y);
	//print and compare to exact solution:
	std::cout << "Exc. 35:\nvalues of u(x) for x = 0, 0.25, ..., 1:" << "\n";
	std::cout << u0 << " | ";
	for (int i=0; i<3; i++) std::cout << u[i] << " | ";
	std::cout << u4 << " | \n";
	std::cout << "exact solution:" << "\n";
	for (int i=0; i<5; i++) std::cout << (exp(.5*i)-exp(-.5*i)) << " | ";
	std::cout << "\n";
}
