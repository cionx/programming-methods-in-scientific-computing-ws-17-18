#include <vector>



class Polynomial {
  std::vector<double> coeff;
  
public:
  Polynomial();
  Polynomial(std::vector<double> coefficients);
  Polynomial(double c);
  
  Polynomial operator-();
  Polynomial operator+(Polynomial p);
  Polynomial operator-(Polynomial p);
  Polynomial operator*(Polynomial p);

  double operator()(double x);
  
  Polynomial clean();
  bool operator==(Polynomial p);
  void print();
};
