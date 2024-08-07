#include <iostream>
#include <fstream>
#include <string>
using namespace std; 

bool CalcSame(string line);

int main() {
	
string line;
int counter = 0;

ifstream MyReadFile("Downloads/input4.txt");

while (getline (MyReadFile, line)) {
	if(CalcSame(line) == true){
		counter++;
	}
}

cout << counter << endl;

MyReadFile.close();

return 0;
}

bool CalcSame(string line) {
	
string front, back, A, B, C, D;
int a, b, c, d, found;

cout << line << endl;

found = line.find(',');
front = line.substr(0, found);
back = line.substr(found);

found = front.find('-');
A = front.substr(0, found);
B = front.substr(found+1);

found = back.find('-');
C = back.substr(1, found);
D = back.substr(found+1);

cout << A << " " << B << " " << C << " " << D << endl;

a = stoi(A);
b = stoi(B);
c = stoi(C);
d = stoi(D);

if(c > b || d < a ) {
//if((a > c && b > d) || (c > a && d > b) ) {
	return false;
}

return true;
}
