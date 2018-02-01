#include <vector>

#define EPS 1.E-14


class Matrix{
    std::vector<std::vector<double>> mat;
    int rows, cols;
    
  public:
    
    Matrix();
    Matrix(int m, int n);
    Matrix(int m, int n, double v);
    
    // informations about the matrix
    double& operator() (int i, int j);
    int width();
    int height();
    
    
    // matrix operations
    Matrix operator-();
    Matrix operator+(Matrix B);
    Matrix operator-(Matrix B);
    Matrix operator*(Matrix B);
    
    //  elementary row operations
    void permuteRows(int i,  int j);
    void multiplyRow(int i, double c);
    void addRowToFrom(int i,  int j, double c);
    
//  comparing and printing
    Matrix clean();
    bool operator==(Matrix B);
    void print();
};

// solving Ax = y
std::vector<double> gaussSolve(Matrix A, std::vector<double> y);
