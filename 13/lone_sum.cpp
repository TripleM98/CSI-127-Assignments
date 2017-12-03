/*
Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as another of the values, 
it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
*/
#include <iostream>

int sum(int a,int b,int c){
	if(a==b && b==c && a==c){
		return 0;
	}
	else if (a==b){
		return c;
	}
	else if (a==c){
		return b;
	}
	else if(b==c){
		return a;
	}
	else if (a!=b && b!=c && a!=c){
		return a+b+c;
	}

}

int main(){
	std::cout<<sum(1,2,3)<<std::endl;
	std::cout<<sum(3,2,3)<<std::endl;
	std::cout<<sum(3,3,3)<<std::endl;
	std::cout<<sum(2,2,4)<<std::endl;
	std::cout<<sum(3,5,5)<<std::endl;

	return 0;
}