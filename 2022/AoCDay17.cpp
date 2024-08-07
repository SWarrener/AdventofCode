#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <tuple>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <unordered_map>
#include "AoCday17.h"
using namespace std; 

Grid::Grid() {
	vector<char> floor(9, '@');
	grid.push_back(floor);
}

bool Grid::MoveShape(Shape& shape, char command){
	vector<pair<long, long>> new_Coords;
	
	switch(command){
		case '<':
			if(CanMove(shape.Coords, command)){
				for (pair<long, long> p : shape.Coords) {
					grid[p.second][p.first] = '.';
					grid[p.second][p.first-1] = '#';
					new_Coords.push_back(make_pair(p.first-1, p.second));
				}
			} else {
				new_Coords = shape.Coords;
			}
			break;
		case '>':
			if(CanMove(shape.Coords, command)){
				for (pair<long, long> p : shape.Coords) {
					grid[p.second][p.first] = '.';
					grid[p.second][p.first+1] = '#';
					new_Coords.push_back(make_pair(p.first+1, p.second));
				}
			} else {
				new_Coords = shape.Coords;
			}
			break;
		case 'd':
			if(CanMove(shape.Coords, command)){
				for (pair<long, long> p : shape.Coords) {
					grid[p.second][p.first] = '.';
					grid[p.second-1][p.first] = '#';
					new_Coords.push_back(make_pair(p.first, p.second-1));
				}
			} else {
				for (pair<long, long> p : shape.Coords) {
					grid[p.second][p.first] = 'R';
				}
				return false;
			}
			break;
	}
	shape.Coords = new_Coords;
	return true;
}

bool Grid::CanMove(vector<pair<long, long>> Coords, char command){
	switch(command){
		case '<':
			for (pair<long, long> p : Coords) {
				if(grid[p.second][p.first-1] == '@' || grid[p.second][p.first-1] == 'R'){
					return false;
				}
			}
			break;
		case '>':
			for (pair<long, long> p : Coords) {
				if(grid[p.second][p.first+1] == '@' || grid[p.second][p.first+1] == 'R'){
					return false;
				}
			}
			break;
		case 'd':
			for (pair<long, long> p : Coords) {
				if(grid[p.second-1][p.first] == '@' || grid[p.second-1][p.first] == 'R'){
					return false;
				}
			}
			break;
	}
	return true;
}

void Grid::AddLines(int num) {
	vector<char> line {'@','.','.','.','.','.','.','.','@'};
	for(int i = 0; i <= num; i++){
		grid.push_back(line);
	}
}

long Grid::CalculateHighestPoint() {
	for(long i = grid.size()-1; i >= 0; i--) {
		for(int j = 0; j < grid[i].size(); j++){
			if(grid[i][j] == 'R') {
				return i;
			}
		}
	}
	cout << "failed to find highest point" << endl;
	return 0;
}

void Grid::printGrid(){
	for(long i = grid.size()-1; i >= 0; i--) {
		for(int j = 0; j < grid[i].size(); j++){
			cout << grid[i][j];
		}
		cout << endl;
	}
}

pair<long, int> Grid::FindLoop(int command_index, int height, int counter, bool& finished){
	string key = to_string(command_index) + "_";
	for(int i = height-1; i >= height-20; i--){
		for(int j = 0; j < grid[i].size(); j++) {
			key.push_back(grid[i][j]);
		}
	}
	if(keys.find(key) == keys.end()) {
		keys.insert({key, {height, counter}});
	} else {
		int old_height = keys.find(key)->second.first;
		int old_counter = keys.find(key)->second.second;
		cout << old_height << " " << height << " " << counter << " " <<  old_counter << endl;
		int modulo = (1000000000001 - old_counter ) % (counter-old_counter);
		finished = true;
		return {(height-old_height) * ((1000000000001-counter-modulo)/(counter-old_counter)), modulo};
	}
	return {0,0};
}

Grid::Shape::Shape(long counter, long start_y, Grid& grid) {
	long start_x = 3;
	start_y += 4;
	int num;
	long grid_size = grid.grid.size();
	switch(counter % 5){
		case 1:
			//horizontal;
			num = (grid_size >= start_y) ? 0 : start_y - grid_size;
			grid.AddLines(num);
			Coords = {{start_x, start_y}, {start_x+1, start_y}, {start_x+2, start_y}, {start_x+3, start_y}};
			ApplytoGrid(Coords, grid);
			break;
		case 2:
			//plus;
			num = (grid_size >= start_y+2) ? 0 : start_y+2 - grid_size;
			grid.AddLines(num);
			Coords = {{start_x, start_y+1}, {start_x+1, start_y}, {start_x+2, start_y+1}, {start_x+1, start_y+1}, {start_x+1, start_y+2}};
			ApplytoGrid(Coords, grid);
			break;
		case 3:
			//corner;
			num = (grid_size >= start_y+2) ? 0 : start_y+2 - grid_size;
			grid.AddLines(num);
			Coords = {{start_x, start_y}, {start_x+1, start_y}, {start_x+2, start_y}, {start_x+2, start_y+1}, {start_x+2, start_y+2}}; 
			ApplytoGrid(Coords, grid);
			break;
		case 4: 
			//vertical;
			num = (grid_size >= start_y+3) ? 0 : start_y+3 - grid_size;
			grid.AddLines(num);
			Coords = {{start_x, start_y}, {start_x, start_y+1}, {start_x, start_y+2}, {start_x, start_y+3}};
			ApplytoGrid(Coords, grid);
			break;
		case 0:
			//square;
			num = (grid_size >= start_y+1) ? 0 : start_y+1 - grid_size;
			grid.AddLines(num);
			Coords = {{start_x, start_y}, {start_x+1, start_y}, {start_x, start_y+1}, {start_x+1, start_y+1}};
			ApplytoGrid(Coords, grid);
			break;
	}
}

void Grid::Shape::ApplytoGrid(vector<pair<long, long>> Coords, Grid& grid) {
	for (pair<long, long> p : Coords) {
		grid.grid[p.second][p.first] = '#';
	}
}
		
int main() {
	string line, commands;
	long counter = 1, command_no = 0, highest_y = 0, calc_height = 0;
	pair<long, int> info;
	ifstream MyReadFile("../Downloads/input17.txt");
	bool activate_shape = true, finished = false;
	
	while (getline (MyReadFile, line)) {
		commands = line;
	}
	
	Grid grid;

	while (counter < 1000000000001) {
		Grid::Shape shape(counter, highest_y, grid);
		while (activate_shape) {
			char command = commands[command_no % commands.size()];
			activate_shape = grid.MoveShape(shape, command);
			if(!grid.MoveShape(shape, 'd')) {
				counter++;
				activate_shape = false;
			}
			command_no++;
		}
		highest_y = grid.CalculateHighestPoint();
		activate_shape = true;
		if (highest_y > 20 && !finished){
			info = grid.FindLoop(command_no % commands.size(), highest_y, counter, finished);
			if (finished == true){
				calc_height = info.first;
				counter = 1000000000001 - info.second;
			}
		}
	}
	cout << "Part 1 answer is " << highest_y+calc_height << endl;
}
