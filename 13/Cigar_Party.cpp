/*
When squirrels get together for a party, they like to have cigars. 
A squirrel party is successful when the number of cigars is between 40 and 60,
inclusive. Unless it is the weekend, 
in which case there is no upper bound on the number of cigars.
Return True if the party with the given values is successful, or False otherwise.


cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
*/

#include <iostream>

int cigar_party(int cigars, bool is_weekend){
	if (cigars>=40 && cigars<=60 && is_weekend==false){
		return true;
	}
	else if (cigars>=40 && is_weekend==true){
		return true;
	}
	else{
		return false;
	}
}

int main(){
	std::cout<<cigar_party(30, false)<<std::endl;
	std::cout<<cigar_party(50, false)<<std::endl;
	std::cout<<cigar_party(70, true)<<std::endl;


	return 0;
}