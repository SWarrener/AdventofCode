#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
using namespace std; 

bool CalcMessage(string line, int pos);

int main() {
	
string line;

ifstream MyReadFile("Downloads/input6.txt");

while (getline (MyReadFile, line)) {
	for(int i=14; i < line.length(); i++) {
		if(CalcMessage(line, i) == true) {
			cout << i+1 << endl;
			break;
		}
	}

MyReadFile.close();

return 0;
}

}

bool CalcMessage(string line, int pos) {
	string previous = line.substr(pos-13, 14);
	int samecounter = 0;
	for (string::iterator it=previous.begin(); it!=previous.end(); it++){
		for (string::iterator jt=previous.begin(); jt!=previous.end(); jt++){
			if(*it==*jt && samecounter == 0) {
				samecounter++;
			} else if (*it==*jt && samecounter > 0) {
				return false;
			}
		}
		samecounter = 0;
	}
return true;
}
