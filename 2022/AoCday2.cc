#include <iostream>
#include <fstream>
#include <string>
using namespace std; 

int CalcScore(char P, char R);

int main() {
	
string line;
int totalscore;
char played, response;

ifstream MyReadFile("Downloads/input2.txt");

while (getline (MyReadFile, line)) {
	
	played = line[0]; 
	response = line [2];
	
	totalscore += CalcScore(played, response);
}

cout << totalscore << endl;

MyReadFile.close();

return 0;
}

int CalcScore(char P, char R)
{	int score = 0;
	score = 0;
/*	if(P == 'A' && R == 'Y' || P == 'B' && R == 'Z' || P == 'C' && R == 'X'){
		score = 6;
	} else if(P == 'A' && R == 'X' || P == 'B' && R == 'Y' || P == 'C' && R == 'Z'){
		score = 3;
	} else {
		score = 0;
	}
	if(R=='X'){
		score += 1;
	} else if(R=='Y'){
		score += 2;
	} else {
		score += 3;
	}
	*/
	if(R=='X'){ //Winning or losing
		score += 0;
	} else if(R=='Y'){
		score += 3;
	} else {
		score += 6;
	}
	
	if(R=='Y'){
		switch(P){
			case 'A':
			score += 1;
			break;
			case 'B':
			score += 2;
			break;
			case 'C':
			score += 3;
			break;
			default:
			return -1;
		}
	} else if (R=='X'){
		switch(P){
			case 'A':
			score += 3;
			break;
			case 'B':
			score += 1;
			break;
			case 'C':
			score += 2;
			break;
			default:
			return -1;
		}
	} else {
		switch(P){
			case 'A':
			score += 2;
			break;
			case 'B':
			score += 3;
			break;
			case 'C':
			score += 1;
			break;
			default:
			return -1;
		}
	} 
	cout << score << endl;
	return score;
}	
