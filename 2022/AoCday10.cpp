#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <tuple>
#include <cstdlib>
using namespace std; 

void IspixelVisible(int cycle, int X);
vector<char> screen;

int main() {

string line, command;
int X = 1, cycle = 0, value;// strength = 0;
//int important_cycles[6] = {20, 60, 100, 140, 180, 220};


ifstream MyReadFile("Downloads/input10.txt");


while (getline (MyReadFile, line)) {
	command = line.substr(0, line.find(' '));
	if(command == "noop") {
		IspixelVisible(cycle, X);
		cycle++;
	} else if(command == "addx") {
		value = stoi(line.substr(line.find(' ')));
		IspixelVisible(cycle, X);
		cycle++;
		IspixelVisible(cycle, X);
		X += value;
		cycle ++;
	}

/*	for(int i = 0; i < 6; i++){ Part One solution
		if(cycle == important_cycles[i]) {
			strength += (important_cycles[i]*X);
			cout << strength << endl;
		} else if(cycle == important_cycles[i] + 1 && command == "addx") {
			strength += (important_cycles[i]*(X - value));
			cout << strength << endl;
		}
	}
	
cout << "cycle: " << cycle << " and X: " << X << " with line " << line << endl;
}

cout << strength << endl;
*/ 
}

for(int i = 1; i <= screen.size(); i++) {
	cout << screen[i-1];
	if(i % 40 == 0){
		cout << endl;
	}
}

}

void IspixelVisible(int cycle, int X) {
	
	if(cycle % 40 == X % 40||cycle % 40 == (X % 40) - 1 || cycle % 40 == (X % 40) + 1){
		screen.push_back('#');
	} else {
		screen.push_back('.');
	}
}
