#include <iostream>
#include <string>
using std::cout;
using std::string;
using std::endl;

string line (int l, string c){
  string s= "";
	for(int i = 0; i < l; i++){
    s+= c;
  }
  return s;
}

 string rect (int w, int h){
 	string value="";
 	for(int n=0;n<w; n++){
 		for(int x=0; x<h; x++){
 			value+="*";
 		}
 		value+="\n";
 	}
 	return value;
 }

  string tri1(int h){
  	string result="";
 	for(int a=0; a<h;++a){
 		for (int j=0;j<a+1;++j){
 			result+="*";
 		}
 		result+="\n";
 	}
 	return result;
 }
  string tri2(int h){
  	string str="";
  	h+=1;
  	int b=0;
  	while(b<h){  	
  	int s=(b*2)-1;
  	while(s>0){
  		str+="*";
  		s-=1;
  	}
  	str+="\n";
  	b+=1;

  	}
  	return str;
  }
  string tri3(int h){
  	string result="";
  	for(int d = 0; d < h; d++)
	{
		for(int j = 0; j < (d+1); ++j)
		{
			result+="*";
		}
	result+="\n";
	}
	return result;
  }
  string piglatin(word){

  }

 	

int main(){
	
	cout<<line(10, "#")<<endl;
	cout<<rect(10,9)<<endl;
	cout<<tri1(5)<<endl;
	cout<<tri2(6)<<endl;
	cout<<tri3(5)<<endl;
	return 0;

}