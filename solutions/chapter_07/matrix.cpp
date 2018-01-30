#include "matrix.hpp"
#include <cmath>
#include <vector>
#include <iostream>

#define EPS 1.E-14



Matrix::Matrix(){
  mat = {};
  rows = 0;
  cols = 0;
}

Matrix::Matrix(int i, int j){
  rows = i;
  cols = j;
  mat = std::vector<std::vector<double>>(rows, std::vector<double>(cols,0));
}

Matrix::Matrix(int i, int j, double v){
  rows = i;
  cols = j;
  mat = std::vector<std::vector<double>>(rows, std::vector<double>(cols, v));
}

double& operator() (int i, int j){  // indices start at 0
  return mat[i][j];
}

// matrix operations

Matrix Matrix::operator-(){
  Matrix C(rows,cols);     
  for (int i = 0; i < rows; i++)
    for (int j = 0; j < cols; j++)
      C(i,j) = -(*this)(i,j);
    return C;
}

Matrix Matrix::operator+(Matrix B){
  Matrix C(rows,cols);     
  for (int i = 0; i < rows; i++)
    for (int j = 0; j < cols; j++)
      C(i,j) = (*this)(i,j) + B(i,j);
  return C;
}

Matrix Matrix::operator-(Matrix B){
  Matrix C(rows,cols);     
  for (int i = 0; i < rows; i++)
    for (int j = 0; j < cols; j++)
      C(i,j) = (*this)(i,j) - B(i,j);
    return C;
}

Matrix Matrix::operator*(Matrix B){
  Matrix C(rows, B.cols);
  for (int i = 0; i < rows; i++)
    for (int k = 0; k < cols; k++)
      for (int j = 0; j < B.cols; j++)
        C(i,j) += (*this)(i,k)*B(k,j);
  return C;
}

//  elementary row operations

void Matrix::permuteRows(int i,  int j){ // swap rows i <-> j
  std::swap(mat[i],mat[j]);
}

void Matrix::multiplyRow(int i, double c){ // multipliy row i -> c*i
  for(int j = 0; j < cols; j++)
    mat[i][j] *= c;
}

void Matrix::addRowTo(int i,  int j, double c) { // add row i -> i + c*j
  for (int k = 0; k < cols; k++)
    mat[i][k] += c * mat[j][k];
}

std::vector<double> Matrix::gaussSolve(std::vector<double> y){   // solve Ax=y;
  Matrix A = (*this);
  for ( int j=0; j<cols; j++){
    int k=j;
    for ( int i=j; i<rows; i++){
      if (std::abs(A(i,j))>std::abs(A(k,j))) k=i;
    }
    A.permuteRows(j,k);
    std::swap(y[j],y[k]);
    y[j]*=1/(A(j,j));
    A.multiplyRow(j,1/(A(j,j)));
    for(int i=j+1; i<rows; i++){
      y[i]-=y[j]*A(i,j);
      A.addRowTo(j,i,-A(i,j));
    }
  }
  std::vector<double> x(cols);
  for (int i=rows-1; i>=0; i--){
    x[i]=y[i];
    for (int j=i+1; j<cols; j++){
      x[i]-=A(i,j)*x[j];
    }
  }
  return x;
}

//  comparing and printing

Matrix Matrix::clean(){
  Matrix B = Matrix(rows, cols);
  for(int i = 0; i < rows; i++)
    for(int j = 0; j < cols; j++)
      if(std::abs((*this)(i,j)) > EPS)
        B(i,j) = (*this)(i,j);
  return B;
}

bool Matrix::operator==(Matrix B){
  Matrix D = (*this) - B;
  D = D.clean();
  for (int i = 0; i < rows; i++)
    for (int j = 0; j < cols; j++)
      if (D(i,j) != 0)
        return false;
      return true;
}

void Matrix::print(){
  Matrix B = (*this).clean();
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++)
      std::cout << B(i,j) << "\t";
    std::cout << std::endl; 
  }
}
