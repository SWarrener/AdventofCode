#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <tuple>
#include <cstdlib>
#include <sstream>
using namespace std; 

struct item {
	long worry_level;
};

class Monkey {
	public:
		int true_target, false_target, items_inspected, number;
		string operation_number;
		char operation_symbol;
		vector<item> item_list;
		long divisor;
		
		Monkey(int a, string b, char c, vector<item> d, int e, int f, int g) {
			divisor = a;
			operation_number = b;
			operation_symbol = c;
			item_list = d;
			true_target = e;
			false_target = f;
			items_inspected = 0;
			number = g;
		}
		
		void Throw_Items(int mod);
		
		Monkey& MonkeyFinder(int number);
		
};

vector<Monkey> monkey_list;

void Monkey::Throw_Items(int mod) {
		if(item_list.empty() != true) {	
			for(int i = 0; i < item_list.size(); i++) {
				long worry = item_list[i].worry_level;
				switch(operation_symbol){
					case '+':
						worry += stoi(operation_number);
						break;
					case '*':
						if(operation_number == " old") { 
							worry *= worry;
						} else {
							worry*= stoi(operation_number);
						}
						break;
					default:
						break;
				}
				worry = worry % mod;
				item_list[i].worry_level = worry;
				items_inspected++;
				if(worry % divisor == 0) {
					Monkey &tar_monkey = MonkeyFinder(true_target);
					tar_monkey.item_list.push_back(item_list[i]);
				} else {
					Monkey &tar_monkey = MonkeyFinder(false_target);
					tar_monkey.item_list.push_back(item_list[i]);
				}
			}
			item_list.clear();
		}
};

Monkey& Monkey::MonkeyFinder(int number) {
	for(int i = 0; i < monkey_list.size(); i++) {
		if (monkey_list[i].number == number) {
			Monkey &reference = monkey_list[i];
			return reference;
		}
	}
	cout << "something has gone wrong" << endl;
};

int main() {
	string line, operation_number, item_string, cur_monkey_name, cur_item_name;
	int monkey_number = 0, item_number = 10, divisor, true_target, false_target, char_target, mod_all = 1;
	long high1 = 0, high2 = 0, mb;
	char operation_symbol, string_delimeter=',';
	size_t pos = 0;

	ifstream MyReadFile("../Downloads/input11.txt");
	vector<item> starting_items;
	
	
	while (getline (MyReadFile, line)) {
		//All the stuff necessary to get information and create the Monkey and item objects
		if(line.empty() == true) {
			cur_monkey_name = to_string(monkey_number);
			Monkey cur_monkey_name(divisor, operation_number, operation_symbol, starting_items, true_target, false_target, monkey_number);
			monkey_list.push_back(cur_monkey_name);
			monkey_number++;
			starting_items.clear();
		}else if(line[2] == 'O') {
			operation_number = line.substr(line.find_last_of(' '));
			char_target = line.find("old") + 4;
			operation_symbol = line[char_target];
		}else if(line[2] == 'T'){
			divisor = stoi(line.substr(line.find_last_of(' ')));
		}else if(line[8] == 'r'){
			true_target = stoi(line.substr(line.find_last_of(' ')));
		}else if(line[7] == 'f') {
			false_target = stoi(line.substr(line.find_last_of(' ')));
		}else if(line[2] == 'S') {
			item_string = line.substr(line.find(':'));
			item_string.erase(0, 1);
			while ((pos = item_string.find(string_delimeter)) != string::npos) {
				cur_item_name = to_string(item_number);
				item cur_item_name;
				cur_item_name.worry_level = stoi(item_string.substr(0, pos));
				starting_items.push_back(cur_item_name);
				item_string.erase(0, pos+1);
				item_number++;
			}
			pos = 0;
		}
	}
	
	for(int i = 0; i < monkey_list.size(); i++) {
		mod_all *= monkey_list[i].divisor;
	}
	
	for(int i = 0; i < 10000; i++) {
		for(int j = 0; j < monkey_list.size(); j++) {
			monkey_list[j].Throw_Items(mod_all);
		}
	}
	
	for(int i = 0; i < monkey_list.size(); i++) {
		if(monkey_list[i].items_inspected > high1) {
			high2 = high1;
			high1 = monkey_list[i].items_inspected; 
		} else if (monkey_list[i].items_inspected > high2) {
			high2 = monkey_list[i].items_inspected; 
		}
	}
	mb = high1*high2;
	
	cout << mb << endl;
}

