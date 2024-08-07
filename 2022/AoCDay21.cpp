#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <bits/stdc++.h>
#include <math.h>
#include "AoCDay21.h"
using namespace std; 

MonkeyList::Monkey::Monkey(string name, long num, bool solved, char op, string op1, string op2, MonkeyList& list) {
	m_name = name;
	if (solved) {
		m_num = num;
		m_answer = true;
		list.IncrementSolved();
	} else {
		m_op = op;
		m_op1 = op1;
		m_op2 = op2;
	}
}

bool MonkeyList::Monkey::have_answer(){
	return m_answer;
}

void MonkeyList::Monkey::Solve(MonkeyList& list){
	MonkeyList::Monkey& Mon1 = list.FindMonkeyByname(m_op1), Mon2 = list.FindMonkeyByname(m_op2);
	if (Mon1.have_answer() && Mon2.have_answer()) {
		switch(m_op){
			case '/':
				m_num = Mon1.number() / Mon2.number();
				m_answer = true;
				list.IncrementSolved();
				break;
			case '*':
				m_num = Mon1.number() * Mon2.number();
				m_answer = true;
				list.IncrementSolved();
				break;
			case '+':
				m_num = Mon1.number() + Mon2.number();
				m_answer = true;
				list.IncrementSolved();
				break;
			case '-':
				m_num = Mon1.number() - Mon2.number();
				m_answer = true;
				list.IncrementSolved();
				break;
			default:
				cout << m_op << endl;
				return;
		}
	}
}

long MonkeyList::Monkey::number() {
	return m_num;
}

string MonkeyList::Monkey::ret_name() {
	return m_name;
}

pair<string, string> MonkeyList::Monkey::ret_operation_names(){
	return make_pair(m_op1, m_op2);
}

char MonkeyList::Monkey::ret_op() {
	return m_op;
}

MonkeyList::Monkey& MonkeyList::FindMonkeyByname(string name) {
	for (Monkey& Mon : m_monkey_list) {
		if (Mon.ret_name() == name) {
			return Mon;
		}
	}
}

void MonkeyList::append(Monkey Mon) {
	m_monkey_list.push_back(Mon);
}

void MonkeyList::Run(MonkeyList& list) {
	while(m_total_sovled < m_monkey_list.size()) {
		for (MonkeyList::Monkey& Mon : m_monkey_list) {
			//Mon.Print();
			if (!Mon.have_answer()) {
				Mon.Solve(list);
			}
		}
	}
}
		
void MonkeyList::IncrementSolved() {
	++m_total_sovled;
}

MonkeyList::Monkey& MonkeyList::FindMonkeybyOperationName(string name, bool& finished) {
	for (Monkey& Mon : m_monkey_list) {
		pair<string, string> p = Mon.ret_operation_names();
		if (p.first == name || p.second == name) {
			if (Mon.ret_name() == "root") {
				finished = true;
			}
			return Mon;
		}
	}
}

string MonkeyList::CreateMathsList(string initial_monkey, MonkeyList& list) {
	bool finished = false;
	string name = initial_monkey;
	pair<string, string> p;
	long num;
	char pos;
	Monkey& Mon = list.FindMonkeybyOperationName(name, finished);
	while (!finished) {
		p = Mon.ret_operation_names();
		if (p.second == name) {
			num = list.FindMonkeyByname(p.first).number();
			pos = 'L';
		} else if (p.first == name){
			num = list.FindMonkeyByname(p.second).number();
			pos = 'R';
		} else {
			cout << "names don't match when creating maths list" << endl;
			throw;
		}
		m_maths_data.push_back(make_tuple(Mon.ret_op(), num, pos));
		name = Mon.ret_name();
		Mon = list.FindMonkeybyOperationName(name, finished);
	}
	return name;
}

void MonkeyList::DoMaths(long initial) {
	long number = initial;
	for (auto it = m_maths_data.rbegin(); it != m_maths_data.rend(); ++it){
		auto p = *it;
		cout << number << " " << get<0>(p) << " " << get<1>(p) << endl;
		if (get<2>(p) == 'R') {
			switch(get<0>(p)) {
				case '/':
					number = number * get<1>(p);
					break;
				case '*':
					number = number / get<1>(p);
					break;
				case '+':
					number = number - get<1>(p);
					break;
				case '-':
					number = number + get<1>(p);
					break;
				default:
					break;
			}
		} else {
			switch(get<0>(p)) {
				case '/':
					number = get<1>(p) / number;
					break;
				case '*':
					number = number / get<1>(p);
					break;
				case '+':
					number = number - get<1>(p);
					break;
				case '-':
					number = get<1>(p) - number;
					break;
				default:
					break;
			}
		}
	}
	cout << "The answer to Part 2 is: " << number << endl;
}

int main() {
	string line, name, name1, name2;
	char op;
	long num, num_to_equal;
	MonkeyList list;
	ifstream MyReadFile("../Downloads/input21.txt");
	
	while (getline (MyReadFile, line)) {
		bool solved = true;
		name = line.substr(0, 4);
		try {
			num = stoi(line.substr(6));
		}
		catch(invalid_argument){
			name1 = line.substr(6, 4);
			name2 = line.substr(13);
			op = line[11];
			solved = false;
		}
		list.append(MonkeyList::Monkey(name, num, solved, op, name1, name2, list));
	}
	list.Run(list);
	cout << "The answer to part 1 is: " << list.FindMonkeyByname("root").number() << endl;

	string top_of_human_chain = list.CreateMathsList("humn", list);
	pair<string, string> p = list.FindMonkeyByname("root").ret_operation_names();
	if (p.first == top_of_human_chain) {
		num_to_equal = list.FindMonkeyByname(p.second).number();
	} else if (p.second == top_of_human_chain) {
		num_to_equal = list.FindMonkeyByname(p.first).number();
	} else {
		cout << "top of chain does not match operations of root. Something has gone wrong" << endl;
		throw;
	}
	list.DoMaths(num_to_equal);
}