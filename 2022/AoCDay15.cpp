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

void distance_check(long dist, int x, int y);

class Sensor {
	int Beaconx, Beacony, Sensory, Sensorx;
	long distance;
	
	public:
		Sensor(int bx, int by, int sx, int sy) {
			Beacony = by;
			Beaconx = bx;
			Sensorx = sx;
			Sensory = sy;
			distance = abs(Beacony - Sensory) + abs(Beaconx - Sensorx);
		}
		long get_distance() {
			return distance;
		}
		int calculate_distance_to(int x, int y) {
			return (abs(y - Sensory) + abs(x - Sensorx));
		}
		int get_Beaconx() {
			return Beaconx;
		}
		int get_Beacony() {
			return Beacony;
		}
		int get_Sensorx() {
			return Sensorx;
		}
		int get_Sensory() {
			return Sensory;
		}
};

vector<Sensor> sensor_list;

int main() {
	string line, sensor, beacon;
	int lowest_x = 0, highest_x = 0, bx, by, sx, sy, positions = 0;
	ifstream MyReadFile("../Downloads/input15.txt");

	
	while (getline (MyReadFile, line)) {
		sensor = line.substr(0, line.find(':')+1);
		beacon = line.substr(line.find(':'));
		sx = stoi(sensor.substr(sensor.find("x=")+2, sensor.find(',')));
		sy = stoi(sensor.substr(sensor.find("y=")+2, sensor.find(':')));
		bx = stoi(beacon.substr(beacon.find("x=")+2, beacon.find(',')));
		by = stoi(beacon.substr(beacon.find("y=")+2));
		
		Sensor sensor(bx, by, sx, sy);
		sensor_list.push_back(sensor);
		
		if(sx - sensor.get_distance() < lowest_x) {
			lowest_x = sx - sensor.get_distance();
		} else if(sx + sensor.get_distance() > highest_x) {
			highest_x = sx + sensor.get_distance();
		}		
	}
	
	for(int i = lowest_x; i <= highest_x; i++) {
		for(Sensor sensor : sensor_list) {
			if(sensor.calculate_distance_to(i, 2000000) <= sensor.get_distance() && !(sensor.get_Beaconx() == i && sensor.get_Beacony() == 2000000)) {
				positions++;
				break;
			}
		}	
	}
	cout << "The part one answer is:" << positions << endl;
	
	for(Sensor sensor : sensor_list) {
		long distance = sensor.get_distance() + 1;
		distance_check(distance, sensor.get_Sensorx(), sensor.get_Sensory());
	}
}

void distance_check(long dist, int x, int y) {
	long z = 0;
	bool answer = true;
	
	for (long i = dist; i >= 0; i--) {
		for(Sensor sensor : sensor_list) {
			if(sensor.calculate_distance_to(i + x, z + y) <= sensor.get_distance() || i+x < 0 || i+x > 4000000 || z+y < 0 || z+y > 4000000) {
				answer = false;
				break;
			}
		}
		if (answer) {
			cout << "Part 2 answer is: " << (i + x)*4000000 + z + y << endl;
		}
		z++;
		answer = true;
	}
	z=0;
};
