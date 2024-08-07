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

class Valve {
	
	vector<string> leads_to;
	string name;
		
	public:
		int flow;
		bool open = false, searched = false;
		
		Valve(int a, string b, vector<string> c) {
			flow = a;
			name = b;
			leads_to = c;
		}
		
		string get_name() {
			return name;
		}
};		

vector<Valve> Valvelist, PressureValves;
vector<string> split(string s, string delimiter);
Valve& find_valve_by_name(string name);

int main() {
	string line, name, tunnels;
	ifstream MyReadFile("../Downloads/input16.txt");
	int flow, total = 0, turns = 30;
	
	while (getline (MyReadFile, line)) {
		flow = stoi(line.substr(line.find('=')+1, line.find(';')));
		name = line.substr(line.find(' ') + 1, line.find("has")-7);
		tunnels = line.substr(line.find("valves ")+7);
		Valve valve(flow, name, split(tunnels, ", "));
		Valvelist.push_back(valve);
		if (flow > 0) {
			PressureValves.push_back(valve);
		}
	}
	
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

Valve& find_valve_by_name(string name){
	for(int i = 0; i < Valvelist.size(); i++) {
		if (Valvelist[i].get_name() == name) {
			Valve &ref = Valvelist[i];
			return ref;
		}
	}
}
