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
using namespace std; 

class Grid{
	unordered_map<string, pair<int, int>> keys;
	
	public:
		vector<vector<char>> grid; //This will work in reverse to how it is visualised. Stuff will 'fall' upwards.
		Grid();
		class Shape{
			public: 
				vector<pair<long, long>> Coords;
				Shape(long counter, long start_y, Grid& grid);
				void ApplytoGrid(vector<pair<long, long>> Coords, Grid& grid);
		};	

		void AddLines(int num);
		bool MoveShape(Shape& shape, char command);
		bool CanMove(vector<pair<long, long>> Coords, char command);
		long CalculateHighestPoint();
		void printGrid();
		pair<long, int> FindLoop(int command_index, int height, int counter, bool& finished);
};

