#include<cmath>
#include<vector>
#include<iostream>

class Quaternion {
		double coords[4];
	public:
		Quaternion(){
			coords[0] = 0;
			coords[1] = 0;
			coords[2] = 0;
			coords[3] = 0;
		}
		Quaternion(double x, double i, double j,double k){
			coords[0] = x;
			coords[1] = i;
			coords[2] = j;
			coords[3] = k;
		}
		Quaternion(double q[4]){
			for(int i=0;i<4;i++) coords[i] = q[i];
		}
		Quaternion(double x){
			coords[0] = x;
			coords[1] = 0;
			coords[2] = 0;
			coords[3] = 0;
		}
		Quaternion operator+(Quaternion q){
			double r[4];
			for(int i=0;i<4;i++) r[i]=coords[i]+q.coords[i];
			return Quaternion(r);
		}
		Quaternion operator-(){
			double r[4];
			for(int i=0;i<4;i++) r[i]=-coords[i];
			return Quaternion(r);
		}
		Quaternion operator-(Quaternion q){
			double r[4];
			for(int i=0;i<4;i++) r[i]=coords[i]-q.coords[i];
			return Quaternion(r);
		}
		Quaternion operator*(Quaternion q){
			double r[4]={coords[0]*q.coords[0] - coords[1]*q.coords[1] - coords[2]*q.coords[2] - coords[3]*q.coords[3],
						coords[0]*q.coords[1] + coords[2]*q.coords[3] - coords[3]*q.coords[2] + coords[1]*q.coords[0],
						coords[0]*q.coords[2] - coords[1]*q.coords[3] + coords[3]*q.coords[1] + coords[2]*q.coords[0],
						coords[0]*q.coords[3] + coords[1]*q.coords[2] - coords[2]*q.coords[1] + coords[3]*q.coords[0]};
			return Quaternion(r);
		}
		double abs(){
			return sqrt(coords[0]*coords[0]+coords[1]*coords[1]+coords[2]*coords[2]+coords[3]*coords[3]);
		}
		Quaternion inverse(){
			double norm = coords[0]*coords[0]+coords[1]*coords[1]+coords[2]*coords[2]+coords[3]*coords[3];
			double r[4] = {	coords[0]/norm,
							-coords[1]/norm,
							-coords[2]/norm,
							-coords[3]/norm };
			return Quaternion(r);
		}
		Quaternion operator/(Quaternion q){
			return (*this)*q.inverse();
		}
		Quaternion clean(){
			double r[4]={0};
			for(int i=0;i<4;i++){
				if(std::abs(coords[i])>1e-14) r[i]=coords[i];
			}
		return Quaternion(r);
		}
		bool operator==(Quaternion q){
			for(int i=0;i<4;i++){
				if(std::abs(coords[i]-q.coords[i])>1e-14) return false;
			}
			return true;
		}
		void print(){
			std::cout << coords[0] << " + " << coords[1] << "i + " << coords[2] << "j + " << coords[3] << "k\n";
		}
};


int main(){
	Quaternion q1(1,2,3,4), q2(2,3,4,5), q3, q4(1);
	q1.print();
	q3.print();
	q4.print();
	(q1*q2).print();
	(q2*q1).print();
}