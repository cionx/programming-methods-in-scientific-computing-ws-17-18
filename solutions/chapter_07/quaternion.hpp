#include<vector>

#define EPS 1.E-14

class Quaternion {
  std::vector<double> coord;
  
public:
  
  Quaternion();
  Quaternion(double x, double i, double j,double k);
  Quaternion(double q[4]);
  Quaternion(double x);
  
  double abs();
  Quaternion operator-();
  Quaternion conjugate();
  Quaternion inverse();
  Quaternion clean();
  
  Quaternion operator+(Quaternion q);
  Quaternion operator-(Quaternion q);
  Quaternion operator*(Quaternion q);
  Quaternion operator/(double r);
  Quaternion operator/(Quaternion q);

  bool operator==(Quaternion q);
  
  void print();
};
