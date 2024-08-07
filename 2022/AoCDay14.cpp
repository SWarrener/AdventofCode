#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <tuple>
#include <cstdlib>
#include <sstream>
#include <utility>
using namespace std; 

vector<string> split(string s, string delimiter);
constexpr int grid_size() {
		return 1000;
	}

class Grid {
	int lowest_rock_y = 0, sand_count = 0, floor;
	char grid[grid_size()][grid_size()];
	bool finished = false;
	pair<int, int> Sand = {500, 0};
	
	void MakeRocks(pair<int, int> prev, pair<int, int> cur) {
		int xdifference = (prev.first > cur.first) ? prev.first - cur.first : cur.first - prev.first;
		int ydifference = (prev.second > cur.second) ? prev.second - cur.second : cur.second - prev.second;
		for (int i = 0; i <= xdifference; i++) {
			for (int j = 0; j <= ydifference; j++) {
				int x = (prev.first > cur.first) ? cur.first + i : prev.first + i;
				int y = (prev.second > cur.second) ? cur.second + j : prev.second + j;
				grid[y][x] = '#';
			};
		};
	};
	
	void MoveSand() {
		//if(Sand.second > lowest_rock_y){
		if(grid[0][500] == 'o') {
			finished = true;
			cout << "The answer is: " << sand_count << endl;
			return;
		}		
		if(grid[Sand.second+1][Sand.first] == '.'){
			Sand.second++;
		}else if(grid[Sand.second+1][Sand.first-1] == '.'){
			Sand.second++;
			Sand.first--;
		}else if(grid[Sand.second+1][Sand.first+1] == '.'){
			Sand.second++;
			Sand.first++;
		}else{
			grid[Sand.second][Sand.first] = 'o';
			sand_count++;
			return;
		}
		MoveSand();
		return;
	}
	
	public:
		Grid(string filepath) {
			string line;
			int x, y;
			vector<string> temp_coords;
			vector<pair<int, int>> coords;
			ifstream MyReadFile(filepath);
			
			for(int i=0; i < grid_size(); i++) {
				for(int j=0; j < grid_size(); j++) {
					grid[i][j] = '.';
				};
			};
	
			while (getline (MyReadFile, line)) {
				//Use pairs for co-ordinates and draw the walls of the grid
				temp_coords = split(line, " -> ");
				for (auto it : temp_coords) {
					x = stoi(it.substr(0, it.find(',')));
					y = stoi(it.substr(it.find(',')+1));
					coords.push_back(make_pair(x, y));
					if (y > lowest_rock_y) {
						lowest_rock_y = y;
					};
				};
				for(int i = 1; i < coords.size(); i++) {
					MakeRocks(coords[i-1], coords[i]);
				};
				temp_coords.clear();
				coords.clear();
			};
			floor = lowest_rock_y + 2;
			for(int i = 0; i < grid_size(); i++) {
				grid[floor][i] = '#';
			}
		};
		//Start generating sand, once sand falls below the lowest rock y we stop and count the sand.
		void sand() {
			while(!finished) {
				MoveSand();
				Sand = {500, 0};
			};
		};
		void printGrid() {
			for(int i=0; i < grid_size(); i++) {
				for(int j=0; j < grid_size(); j++) {
					cout << grid[i][j];
				};
				cout << endl;
			}; 
		};
};


int main() {
	Grid grid("../Downloads/input14.txt");
	cout << "running sand" << endl;
	grid.sand();
}

vector<string> split(string s, string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    string token;
    vector<string> res;

    while ((pos_end = s.find(delimiter, pos_start)) != string::npos) {
        token = s.substr(pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back(token);
    }

    res.push_back(s.substr(pos_start));
    return res;
}
