#include "Complex.h"
#include <string>
#include <iostream>
using namespace std;

Complex::Complex (float re, float im) {
	this->Re=re;
	this->Im=im;
}

string Complex::ToString(){
char buf[100];
int res = snprintf(buf, sizeof(buf), "%f+%fj", this->Re, this->Im);
std::string str = "error!";
if (res >= 0 && res < sizeof(buf))
    str = buf;
	return string(str);
}	



