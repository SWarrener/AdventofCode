#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <tuple>
#include <cstdlib>
using namespace std; 

vector<tuple<int, int>> positions_visited;
void CheckPositionVisited(int x, int y);
tuple<int, int> TailMovingNeeded(tuple<int, int> head, tuple<int, int> tail);
tuple<int, int> MoveHead(tuple<int, int> head, char dir);
int difference;							    

int main() {

string line;
int distance;
char direction;
vector<tuple<int, int>> rope_positions;
tuple<int, int> temp_position;

ifstream MyReadFile("Downloads/input9.txt");
positions_visited.push_back(make_tuple(0, 0));

for(int i = 0; i < 10; i++) {
	rope_positions.push_back(make_tuple(0,0));
}

while (getline (MyReadFile, line)) {
	direction = line[0];
	distance = stoi(line.substr(line.find(' ')));
	for(int i=0; i < distance; i++) {
	//Move head one tile
		rope_positions[0] = MoveHead(rope_positions[0], direction);
		for(int j =1; j < 10; j++){	
			//Check if tail needs moving
			temp_position = TailMovingNeeded(rope_positions[j-1], rope_positions[j]);
			if(temp_position != rope_positions[j]) {
				//Move tail
				rope_positions[j] = temp_position;
				//Check if the tail has already been to its current position
				if(j==9){
					CheckPositionVisited(get<0>(rope_positions[j]), get<1>(rope_positions[j]));
				}
			} else {
			break;
			}
		}
	}
}

cout << positions_visited.size() << endl;
return 0;
}

tuple<int, int> TailMovingNeeded(tuple<int, int> head, tuple<int, int> tail){
	
if(get<0>(head) - get<0>(tail) > 1 && get<1>(head) - get<1>(tail) > 1) {
	get<0>(tail) = get<0>(head)-1;
	get<1>(tail) = get<1>(head)-1;
}else if(get<0>(head) - get<0>(tail) < -1 && get<1>(head) - get<1>(tail) > 1){
	get<0>(tail) = get<0>(head)+1;
	get<1>(tail) = get<1>(head)-1;
}else if(get<0>(head) - get<0>(tail) > 1 && get<1>(head) - get<1>(tail) < -1){
	get<0>(tail) = get<0>(head)-1;
	get<1>(tail) = get<1>(head)+1;
}else if(get<0>(head) - get<0>(tail) < -1 && get<1>(head) - get<1>(tail) < -1){
	get<0>(tail) = get<0>(head)+1;
	get<1>(tail) = get<1>(head)+1;
}else if(get<0>(head) - get<0>(tail) > 1){ //above 
	get<0>(tail) = get<0>(head)-1;
	get<1>(tail) = get<1>(head);
}else if(get<0>(head) - get<0>(tail) < -1){ //below 
	get<0>(tail) = get<0>(head)+1;
	get<1>(tail) = get<1>(head);
}else if(get<1>(head) - get<1>(tail) < -1){ //left 
	get<1>(tail) = get<1>(head)+1;
	get<0>(tail) = get<0>(head);
}else if(get<1>(head) - get<1>(tail) > 1){ //right 
	get<1>(tail) = get<1>(head)-1;
	get<0>(tail) = get<0>(head);
}
	
return tail;	
}

void CheckPositionVisited(int x, int y) {
	
	for(int i = 0; i < positions_visited.size(); i ++) {
		if(x == get<0>(positions_visited[i]) && y == get<1>(positions_visited[i])) {
			return;
		}
	}
positions_visited.push_back(make_tuple(x, y));

}

tuple<int, int> MoveHead(tuple<int, int> head, char dir) {

switch(dir){
	case 'R':
	get<0>(head) += 1; 
	break;
	case 'L':
	get<0>(head) -= 1; 
	break;
	case 'D':
	get<1>(head) -= 1; 
	break;
	case 'U':
	get<1>(head) += 1; 
	break;
	default:
	break;
}

return head;
}
