#include<cmath>
#include<vector>
#include<iostream>


class Matrix{
		std::vector<std::vector<double> > M;
		 int rows, cols;
	public:
		Matrix(){
			M = {};
			rows = 0;
			cols = 0;
		}
		Matrix(int i, int j){
			rows = i;
			cols = j;
			M = std::vector<std::vector<double> >(rows, std::vector<double>(cols));
		}
		Matrix(int i, int j, double v){
			rows = i;
			cols = j;
			M = std::vector<std::vector<double> >(rows, std::vector<double>(cols, v));
		}
		double& operator() (int i, int j){
			return M[i][j];							  // indices start at 0;
		}
		void print(){
			for (int i = 0; i < rows; i++) {
				for (int j = 0; j < cols; j++){
					std::cout << M[i][j] << "\t";
				}
				std::cout << "\n"; 
			}
		}
		
		// all of these will produce out of range errors when used improperly:
		
		Matrix operator+(Matrix b){
			Matrix c(rows,cols);     
			for (int i = 0; i < rows; i++){
				for (int j = 0; j < cols; j++){
					c(i,j) = (*this)(i,j) + b(i,j);
				}
			}
			return c;
		}
		Matrix operator*(Matrix b){
			Matrix c(rows, b.cols);
			for (int i = 0; i < rows; i++){
				for (int m = 0; m < cols; m++){
					for (int j = 0; j < b.cols; j++){
						c(i,j) += (*this)(i,m)*b(m,j);
					}
				}
			}
			return c;
		}
		Matrix operator-(Matrix b){
			Matrix c(rows,cols);     
			for (int i = 0; i < rows; i++){
				for (int j = 0; j < cols; j++){
					c(i,j) = (*this)(i,j) - b(i,j);
				}
			}
			return c;
		}
		Matrix operator-(){
			Matrix c(rows,cols);     
			for (int i = 0; i < rows; i++){
				for (int j = 0; j < cols; j++){
					c(i,j) = -(*this)(i,j);
				}
			}
			return c;
		}
		bool operator==(Matrix b){
			for (int i = 0; i < rows; i++){
				for (int j = 0; j < cols; j++){
					if (std::abs((*this)(i,j) - b(i,j)) > 1e-14) return false;
				}
			}
			return true;
		}
		void permuteRows( int i1,  int i2){ // swaps rows i1 and i2
			std::swap(M[i1],M[i2]);
		}
		void multiplyRow( int i, double l){ // multiplies row i with l
			for ( int j=0; j<cols; j++){
				M[i][j]*=l;
			}
		}
		void addRowTo(int i1,  int i2, double l) { // add l times row i1 to row i2
			for ( int j=0; j<cols; j++){
				M[i2][j]+=l*(M[i1][j]);
			}
		}
		std::vector<double> gaussSolve(std::vector<double> y){   // solve Ax=y;
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
		Matrix invert(){
			Matrix A(rows,cols);
			for(int j=0; j<cols; j++){
				std::vector<double> y(cols,0);
				y[j]=1;
				std::vector<double> x=(*this).gaussSolve(y);
				for(int i=0; i<rows; i++){
					A(i,j)=x[i];
				}
			}
			return A;
		}
		Matrix clean(){  //sets small values to 0, looks nicer when printing
			Matrix A=(*this);
			for(int i=0; i<rows; i++){
				for(int j=0; j<cols; j++){
					if(std::abs(A(i,j))<1e-14) A(i,j)=0;
				}
			}
			return A;
		}
};
