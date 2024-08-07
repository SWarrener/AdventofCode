#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <tuple>
#include <cstdlib>
#include <sstream>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std; 

class Path {
	public:
		int length, cur_x, cur_y;
		
};

struct Tile {
	bool visited = false;
	int height;
	int x, y;
};

class Grid {
	private:
		vector<vector<Tile>> grid;
		vector<Tile> temp;
		string line, name;
		int counter = 0, start_x, start_y, end_x, end_y, length = 0;
		bool finished = false;
		Tile Start, End;
		bool in_bounds(Tile tile, int x, int y) const {
			return 0 <= tile.x + x  && tile.x + x < grid[0].size()
				&& 0 <= tile.y + y && tile.y + y < grid.size();
		};
		bool passable(Tile cur, Tile next) const {
			if (cur.height + 1 >= next.height) {
				cout << "passable" << endl;
				return true;
			}
			return false;
		};
		vector<Tile> neighbours(Tile cur) const {
			vector<Tile> results;
			if(in_bounds(cur, 1, 0)){
				cout << "test1" << endl;
				if (passable(cur, grid[cur.y][cur.x+1])){
				results.push_back(grid[cur.y][cur.x+1]);
				}
			}
			if(in_bounds(cur, -1, 0)){
				cout << "test2" << endl;
				if (passable(cur, grid[cur.y][cur.x-1])){
				results.push_back(grid[cur.y][cur.x-1]);
				}
			}
			if(in_bounds(cur, 0, 1)){
				cout << "test3" << endl;
				if (passable(cur, grid[cur.y+1][cur.x])){
				results.push_back(grid[cur.y+1][cur.x]);
				}
			}
			if(in_bounds(cur, 0, -1)){
				cout << "test4" << endl;
				if (passable(cur, grid[cur.y-1][cur.x])){
				results.push_back(grid[cur.y-1][cur.x]);
				}
			}
			if ((cur.x + cur.y) % 2 == 0) {
				std::reverse(results.begin(), results.end());
			}
			cout << cur.x << " " << cur.y << " Passable Neighbours: " << results.size() << endl;
			return results;
		};
		bool PossibleStarts(Tile cur) {
			if (cur.height == 97) {
				if(in_bounds(cur, 1, 0)){
					if (grid[cur.y][cur.x+1].height == 98){
					return true;
					}
				}
				if(in_bounds(cur, -1, 0)){
					if (grid[cur.y][cur.x-1].height == 98){
					return true;
					}
				}
				if(in_bounds(cur, 0, 1)){
					if (grid[cur.y+1][cur.x].height == 98){
					return true;
					}
				}
				if(in_bounds(cur, 0, -1)){
					if (grid[cur.y-1][cur.x].height == 98){
					return true;
					}
				}
			}
			return false;
		};
	public:
		Grid(string filepath) {
			ifstream MyReadFile(filepath);
	
			while (getline (MyReadFile, line)) {
				for (int i=0; i<line.length(); i++) {
					name = to_string(i) + "," + to_string(counter);
					Tile name;
					name.height = int(line[i]) - 0;
					name.x = i;
					name.y = counter;
					if (name.height == 83) {
						start_x = i;
						start_y = counter;
						name.height = 97;
						name.visited = true;
						Start = name;
					} else if (name.height == 69){
						end_x = i;
						end_y = counter;
						name.height = 122;
						End = name;
					};
					temp.push_back(name);
				}		 
				grid.push_back(temp);
				temp.clear();
				counter++;
			}
		};
		void Search() {
			vector<Tile> frontier, frontier_move;
			frontier.push_back(Start);
			for (int i = 0; i < grid.size(); i++) {
				for (Tile Current: grid[i]) {
					if(PossibleStarts(Current)) {
						Current.visited = true;
						frontier.push_back(Current);
					}
				}
			}
			while (!finished) {
				for (Tile Current: frontier){
					if(Current.x == End.x && Current.y == End.y) {
						cout << "The answer is: " << length << endl;
						finished = true;
						break;
					};
					for (Tile Next : neighbours(Current)) {
						if (Next.visited == false) {
							grid[Next.y][Next.x].visited = true;
							frontier_move.push_back(Next);
							cout << "Unvisited Neighbour found: x " << Next.x << " y " << Next.y << endl;
						} else {
							cout << "Visited Neighbour found: x " << Next.x << " y " << Next.y << endl;
						}
					};
				cout << "Finishing current Frontier Tile. New frontier size " << frontier_move.size() << endl;
				};
				frontier.clear();
				frontier = move(frontier_move);
				length++;
			};
		};
};


int main() {
	
	Grid Grid_info("../Downloads/input12.txt");
	cout << "grid created" << endl;
	Grid_info.Search();

}
