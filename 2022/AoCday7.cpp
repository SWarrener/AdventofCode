#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
using namespace std; 

bool CalcMessage(string line, int pos);

int main() {

struct Directory {
	int size;
	int level;
	string name;
	string parent;
	bool active;
};	
string line, curdir, curdirname, arg, parent;
int cur_size, level = 0, dir_count = 1, totalsize = 0, cur_lowest = 100000000, unused, min_deletion;
vector<Directory> directories;
stack<string> filestruct;

filestruct.push("source");

ifstream MyReadFile("Downloads/input7.txt");

while (getline (MyReadFile, line)) {
	if(line[0] == '$'){ //a command
		if (line[2] == 'c') { //a cd command, so we are interested in it
			arg = line.substr(line.rfind(' ')+1);
			cout << arg << endl;
			if (arg == "..") {
				curdir = filestruct.top();
				filestruct.pop();
				for (int i = 0; i < directories.size(); i++) {
					if (level == directories[i].level && directories[i].name == curdir && directories[i].parent == filestruct.top() && directories[i].active == true) {
						directories[i].active = false;
						cout << "test1" << endl;
					}
				}
				level--;
			} else {
				parent = filestruct.top();
				filestruct.push(arg);
				level++;
				curdirname = to_string(dir_count);
				Directory curdirname;
				curdirname.size = 0;
				curdirname.level = level;
				curdirname.name = arg;
				curdirname.active = true;
				curdirname.parent = parent;
				directories.push_back(curdirname);
				dir_count++;				
			}
		}	
	} else if (line[0] != 'd') { //a file
		cur_size = stoi(line.substr(0, line.find(' ')));	
		for (int i = 0; i < directories.size(); i++) {
			if (directories[i].active == true) {
			directories[i].size += cur_size;
			}
		}
	}

}
MyReadFile.close();

for (int i = 0; i < directories.size(); i++) { //part 1 solution
	if (directories[i].size <= 100000) {
		totalsize += directories[i].size;
	}
}

cout << "The part one answer is: " << totalsize << endl;


unused = 70000000 - directories[0].size;
min_deletion = 30000000 - unused;

for (int i = 0; i < directories.size(); i++) {
	if (directories[i].size >= min_deletion) {
		if (directories[i].size < cur_lowest) {
			cur_lowest = directories[i].size;
		}
	}
}

cout << cur_lowest << endl;
return 0;
}


bool CalcMessage(string line, int pos) {

return true;
}


