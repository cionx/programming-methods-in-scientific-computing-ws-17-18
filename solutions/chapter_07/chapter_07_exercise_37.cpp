#include<cmath>
#include<vector>
#include<iostream>

class Polynomial {
		std::vector<double> coeff;
	public:
		Polynomial(){
			coeff = {};
		}
		Polynomial(std::vector<double> coefficients){
			coeff = coefficients;
		}
		Polynomial(double c){
			coeff = {c};
		}
		Polynomial operator*(Polynomial p){
			int d1 = coeff.size();
			int d2 = p.coeff.size();
			std::vector<double> r(d1+d2-1,0);
			for(int i=0;i<d1;i++){
				for(int j=0;j<d2;j++){
					r[i+j]+=coeff[i]*p.coeff[j];
				}
			}
			return Polynomial(r);
		}
		Polynomial operator+(Polynomial p){
			int d1 = coeff.size();
			int d2 = p.coeff.size();
			std::vector<double> r(std::max(d1,d2),0);
			for(int i=0;i<d1;i++) r[i]+=coeff[i];
			for(int j=0;j<d2;j++) r[j]+=p.coeff[j];
			return Polynomial(r);
		}
		Polynomial operator-(Polynomial p){
			int d1 = coeff.size();
			int d2 = p.coeff.size();
			std::vector<double> r(std::max(d1,d2),0);
			for(int i=0;i<d1;i++) r[i]+=coeff[i];
			for(int j=0;j<d2;j++) r[j]-=p.coeff[j];
			return Polynomial(r);
		}
		Polynomial operator-(){
			int d = coeff.size();
			std::vector<double> r;
			for(int i=0;i<d;i++) r.push_back(-coeff[i]);
			return Polynomial(r);
		}
		double operator()(double x){
			double r=0;
			int d=coeff.size();
			for(int i=0;i<d;i++) r+=coeff[i]*pow(x,i);
			return r;
		}
		void print(){
			int i = coeff.size()-1;
			if(i<0) std::cout << 0 << '\n';
			else{
				for(;i>1;i--){
					std::cout << coeff[i] << "x^" << i << " + ";
				}
				if(i>0) std::cout << coeff[1] << 'x' << " + ";	
				std::cout << coeff[0] << '\n';
			}
		}
		Polynomial clean(){  //sets small values to 0, looks nicer when printing
			int i = coeff.size()-1;
			for(;(i >= 0) && (std::abs(coeff[i]) < 1e-14);i--);
			if(i<0) return Polynomial();
			std::vector<double> r(i+1,0);
			for(;i>=0;i--){
				if(std::abs(coeff[i]) > 1e-14) r[i]=coeff[i];
			}
			return Polynomial(r);
		}
		bool operator==(Polynomial p){
			return ((*this - p).clean().coeff.size() == 0);
		}
};
