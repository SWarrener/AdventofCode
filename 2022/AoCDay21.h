#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <sstream>
#include <utility>
using namespace std; 



class MonkeyList {

	int m_total_sovled = 0;

	public:

		class Monkey {

			long m_num = 0;
			bool m_answer = false;
			char m_op;
			string m_op1, m_op2, m_name;

			public:
				Monkey(string name, long num, bool solved, char op, string op1, string op2, MonkeyList& list);

				bool have_answer();

				void Solve(MonkeyList& list);

				long number();

				string ret_name();

				char ret_op();

				pair<string, string> ret_operation_names();

				void Print() {
					cout << m_name << " " << m_num << " " << m_op1 << m_op << m_op2 << endl;
				}
		};	

		Monkey& FindMonkeyByname(string name);
		void append(Monkey Mon);
		void Run(MonkeyList& list);
		void IncrementSolved();
		MonkeyList::Monkey& FindMonkeybyOperationName(string name, bool& finished);
		string CreateMathsList(string initial_monkey, MonkeyList& list);
		void DoMaths(long initial);
		
	private:

		vector<Monkey> m_monkey_list;
		vector<tuple<char, long, char>> m_maths_data;
};