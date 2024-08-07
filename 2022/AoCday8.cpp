#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
using namespace std; 

int checkScore(int x, int y, int value);
vector<vector<int>> grid;
bool CheckVisible(int x, int y, int value);

int main() {

	string line;
	int counter = 0, scenic_counter = 0, highest_scenic_counter = 0, visible_counter = -4;
	vector<int> tempV;

	ifstream MyReadFile("Downloads/input8.txt");

	while (getline (MyReadFile, line)) {
		for(int i=0; i < line.length(); i++) {
			int num = line[i] - '0';
			tempV.push_back(num);
		}
		grid.push_back(tempV);
		tempV.clear();
		counter++;
	}


	for(int i=1; i < grid[0].size()-1; i++) {
		for(int j=1; j < grid.size()-1; j++) {
			scenic_counter = checkScore(j, i, grid[i][j]);
			if(scenic_counter > highest_scenic_counter) {
				highest_scenic_counter = scenic_counter;
			}
			if(CheckVisible(j, i, grid[i][j]) == true) {
				visible_counter++;
			}
		
		}
	}

	visible_counter += grid[0].size()*2;
	visible_counter += grid.size()*2;

	cout << "Part One answer: " << visible_counter << endl;

	cout << "Part Two answer: " << highest_scenic_counter << endl;

}


int checkScore(int x, int y, int value) {

	int score, counter;
	score = 1;
	counter = 0;

		for(int i=x-1; i >= 0; i--) { //left
			counter ++;
			if(grid[y][i] >= value || i == 0){
				score *= counter;
				break;
			}
		}

	counter = 0;

		for(int i=y-1; i >= 0; i--) { //up
			counter++;
			if(grid[i][x] >= value || i == 0){
				score *= counter;
				break;
			}
		}

	counter = 0;

		for(int i=x+1; i < grid[0].size(); i++) { //right
			counter++;
			if(grid[y][i] >= value || i == (grid[0].size()-1)){
				score *= counter;
				break;
			}
		}

	counter = 0;

		for(int i=y+1; i < grid.size(); i++) { //down
			counter++;
			if(grid[i][x] >= value || i == (grid.size()-1)){
				score *= counter;
				break;
			}
		}

	return score;
}

bool CheckVisible(int x, int y, int value){

	bool visible[4];

	for(int i = 0; i < 4; i++){
		visible[i] = true;
	}

		for(int i=x-1; i >= 0; i--) { //left
			if(grid[y][i] >= value){
				visible[0] = false;
				break;
			}
		}

		for(int i=y-1; i >= 0; i--) { //up
			if(grid[i][x] >= value){
				visible[1] = false;
				break;
			}
		}

		for(int i=x+1; i < grid[0].size(); i++) { //right
			if(grid[y][i] >= value){
				visible[2] = false;
				break;
			}
		}

		for(int i=y+1; i < grid.size(); i++) { //down
			if(grid[i][x] >= value){
				visible[3] = false;
				break;
			}
		}

	for(int i = 0; i < 4; i++){
		if(visible[i] == true){
			return true;
		}
	}

	return false;
}
