#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <tuple>
#include <cstdlib>
#include <sstream>
#include <utility>
using namespace std; 

class Area {
	
	void Propogate(vector<tuple<int, int, int>> Border) {
		vector<tuple<int, int, int>> NewBorder;
		for (tuple<int, int, int> coords : Border) {
			int x = get<0>(coords), y = get<1>(coords), z = get<2>(coords);
			if (area[x+1][y][z] == '0' && x+1 < 25) {
				area[x+1][y][z] = '2';
				NewBorder.push_back(make_tuple(x+1, y, z));
			}
			if (area[x-1][y][z] == '0' && x-1 > -1) {
				area[x-1][y][z] = '2';
				NewBorder.push_back(make_tuple(x-1, y, z));
			}
			if (area[x][y+1][z] == '0' && y+1 < 25) {
				area[x][y+1][z] = '2';
				NewBorder.push_back(make_tuple(x, y+1, z));
			}
			if (area[x][y-1][z] == '0' && y-1 > -1) {
				area[x][y-1][z] = '2';
				NewBorder.push_back(make_tuple(x, y-1, z));
			}
			if (area[x][y][z+1] == '0' && z+1 < 25) {
				area[x][y][z+1] = '2';
				NewBorder.push_back(make_tuple(x, y, z+1));
			}
			if (area[x][y][z-1] == '0' && z-1 > -1) {
				area[x][y][z-1] = '2';
				NewBorder.push_back(make_tuple(x, y, z-1));
			}
		}
		if (NewBorder.size() > 0) {
			Propogate(NewBorder);
			return;
		}
		return;
	}
	
	public:
		char area[25][25][25];
		
		Area() {
			for (int i = 0; i < 25; i++) {
				for (int j = 0;  j < 25; j++) {
					for (int k = 0;  k < 25; k++) {
						area[i][j][k] = '0';
					}	
				}
			}
		}
		
		void InsertPoint(int x, int y, int z) {
			area[x][y][z] = '1';
		}
		
		int CalcSurfaceArea(bool part2) {
			int result = 0;
			for (int i = 0; i < 25; i++) {
				for (int j = 0; j < 25; j++) {
					for (int k = 0; k < 25; k++) {
						if (area[i][j][k] == '1' && !part2) {
							result += CheckEmptyNeighbours(i, j, k, '0');
						} else if (area[i][j][k] == '1') {
							result += CheckEmptyNeighbours(i, j, k, '2');
						}
					}	
				}
			}
			return result;
		}
		
		int CheckEmptyNeighbours(int x, int y, int z, char ans) {
			int result = 0;
			if (area[x+1][y][z] == ans || x+1 > 25) {
				result++;
			}
			if (area[x-1][y][z] == ans || x-1 < 0) {
				result++;
			}
			if (area[x][y+1][z] == ans || y+1 > 25) {
				result++;
			}
			if (area[x][y-1][z] == ans || y-1 < 0) {
				result++;
			}
			if (area[x][y][z+1] == ans || z+1 > 25) {
				result++;
			}
			if (area[x][y][z-1] == ans || z-1 < 0) {
				result++;
			}
			return result;
		}
		
		void PreparePart2() {
			area[24][24][24] = '2';
			tuple<int, int, int> coord = make_tuple(24, 24, 24);
			vector<tuple<int, int, int>> Border;
			Border.push_back(coord);
			Propogate(Border);
		}
};

int main() {
	string line;
	ifstream MyReadFile("../Downloads/input18.txt");
	int x, y, z;
	
	Area area;
	
	while (getline (MyReadFile, line)) {
		x = stoi(line.substr(0, line.find(',')));
		y = stoi(line.substr(line.find(',')+1, line.rfind(',')));
		z = stoi(line.substr(line.rfind(',')+1));
		area.InsertPoint(x, y, z);
	}
	
	cout << "Part 1 answer: " << area.CalcSurfaceArea(false) << endl;
	area.PreparePart2();
	cout << "Part 2 answer: " << area.CalcSurfaceArea(true) << endl;
}
