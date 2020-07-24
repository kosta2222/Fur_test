/* 
 * File:   Complex.h
 * Author: papa
 *
 * Created on 24 июля 2020 г., 7:19
 */

#ifndef COMPLEX_H
#define	COMPLEX_H
#include <string>
#include "../Obj/Obj.h"
using namespace std;
class Complex : public Obj{
public:
	float Re;
	float Im;
	Complex(float re, float im);
	string ToString();
		
		
	
};



#endif	/* COMPLEX_H */

