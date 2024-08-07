#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
using namespace std; 

bool CalcSame(string line);

int main() {
	
string line;
int num, start, dest;
deque<char> moving;
vector<char> grid[10] = {
	{},
	{'N', 'D', 'M', 'Q', 'B', 'P', 'Z'},
	{'C', 'L', 'Z', 'Q', 'M', 'D', 'H', 'V'},
	{'Q', 'H', 'R', 'D', 'V', 'F', 'Z', 'G'},
	{'H', 'G', 'D', 'F', 'N'}, 
	{'N', 'F', 'Q'},
	{'D', 'Q', 'V', 'Z', 'F', 'B', 'T'},
	{'Q', 'M', 'T', 'Z', 'D', 'V', 'S', 'H'},
	{'M', 'G', 'F', 'P', 'N', 'Q'},
	{'B', 'W', 'R', 'M'}
	};

ifstream MyReadFile("Downloads/input5.txt");

while (getline (MyReadFile, line)) {
	if(line[0] == 'm') { //ignore the first few lines
		num = stoi(line.substr(4,3));
		start = stoi(line.substr(line.find("from")+5,1));	
		dest = stoi(line.substr(line.find("to")+3,1));
		cout << num << " " << start << " " << dest << endl;
		
		for (int i = 0; i < num; i++) {
			char moved = grid[start].back();
			moving.push_front(moved);
			grid[start].pop_back();
		}
		
		for (int i = 0; i < num; i++) {
			char moved = moving.front();
			grid[dest].push_back(moved);
			moving.pop_front();
		}
	}
}

for(int i = 1; i < 10; i++)
	cout << grid[i].back() << endl;

MyReadFile.close();

return 0;
}

bool CalcSame(string line) {

return true;
}
