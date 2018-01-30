#include <vector>

#define EPS 1.E-14


class Matrix{
    std::vector<std::vector<double>> mat;
    int rows, cols;
    
  public:
    
    Matrix();
    Matrix(int i, int j);
    Matrix(int i, int j, double v);
    
    // matrix operations
    double& operator() (int i, int j);
    Matrix operator-();
    Matrix operator+(Matrix B);
    Matrix operator-(Matrix B);
    Matrix operator*(Matrix B);
    
    //  elementary row operations
    void permuteRows(int i,  int j);
    void multiplyRow(int i, double c);
    void addRowTo(int i,  int j, double c);
    std::vector<double> gaussSolve(std::vector<double> y);
    
//  comparing and printing
    
    Matrix clean();
    bool operator==(Matrix B);
    void print();
};
