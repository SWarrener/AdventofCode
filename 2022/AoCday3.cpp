#include <iostream>
#include <fstream>
#include <string>
using namespace std; 

char CalcSame(string lines[3]);

char CalcSame_1(string line);

int main() {
	
	string items, line;
	string lines[3];
	int totalscore = 0, score = 0, i=0, totalscore_1=0;
	char item, item_1;

	ifstream MyReadFile("Downloads/input3.txt");

	while (getline (MyReadFile, line)) {
		i++;
		if (i%3 == 0) {
			lines[2] = line;
			item = CalcSame(lines);
			if (isupper(item)) {
				score = int(item) - 38;
			} else {
				score = int(item) - 96;
			}
			totalscore += score;
		} else if (i%3 == 1) {
			lines[0] = line;
		} else {
			lines[1] = line;
		}
		
		item_1 = CalcSame_1(line);	
		if (isupper(item_1)) {
			score = int(item_1) - 38;
			} else {
				score = int(item_1) - 96;
			}
			totalscore_1 += score;
	}

	cout << "part 1 answer: " << totalscore_1 << endl;

	cout << "part 2 answer: " << totalscore << endl;

	MyReadFile.close();

}

char CalcSame(string lines[3]) {
	
	for (const char &c : lines[0]) {
		for (const char &d : lines[1]) {
			for (const char &e : lines[2]) {
				if (c == d && c == e) {
					return c;
					break;
					break;
					break;
				}
			}
		}
	}
	return 0;
}

char CalcSame_1(string line) {
	string part1 = line.substr(0, line.length()/2), part2 = line.substr(line.length()/2);
	for (const char &c : part1) {
		for (const char &d : part2) {
			if (c == d) {
				return c;
				break;
				break;
			}
		}
	}
	return 0;
}
