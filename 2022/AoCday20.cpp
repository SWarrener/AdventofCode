#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <bits/stdc++.h>
#include <math.h> 
using namespace std; 

class NumberList{
	
	vector<pair<long, long>> Modified;
	
	int FindZero() {
		for (auto p : Modified) {
			if (p.first == 0) {
				auto it = find(Modified.begin(), Modified.end(), p);
				int index = it - Modified.begin();
				return index;
			}
		}
	}
	
	public:
				
		void AddToBoth(int num, int index) {
			Modified.push_back(make_pair(num, index));
			if (num == 0) {
				cout << "zero added at " << index << endl;
			}
		}
		
		void ProcessList() {
			int size = Modified.size();
			
			for (int i = 0; i < size; i++) {
				long num, pos, new_pos;
				for (auto p : Modified) {
					if (p.second == i) {
						num = p.first;
						auto it = find(Modified.begin(), Modified.end(), p);
						pos = it - Modified.begin();
					}
				}	
				
				new_pos = pos + num;
				if (new_pos >= size) {
					new_pos = new_pos % (size-1);
				}
				
				if (new_pos < 0) {
					new_pos += (floor(abs(new_pos/(size-1)))) * (size-1);
					new_pos = new_pos + (size-1);
				}
				
				Modified.erase(next(Modified.begin(), pos));
				Modified.insert(next(Modified.begin(), new_pos), make_pair(num, i));
			}
		}
		
		void Answer() {
			int size = Modified.size();
			int pos = FindZero();
			long answer = 0;
			cout << "zero at " << pos << endl;
			answer += Modified.at((pos+1000) % size).first;
			answer += Modified.at((pos+2000) % size).first;
			answer += Modified.at((pos+3000) % size).first;
			cout << "The answer to Part 1 is: " << answer << endl;
		}
		
		void ApplyKey(long key) {
			for (int i =0; i < Modified.size(); i++) {
				Modified[i].first *= key;
			}
		}
};

int main() {
	string line;
	ifstream MyReadFile("../Downloads/input20.txt");
	long key = 811589153;
	int counter = 0;
	
	NumberList List;
	
	while (getline (MyReadFile, line)) {
		List.AddToBoth(stoi(line), counter);
		counter++;
	}
	List.ApplyKey(key);
	for (int i = 0; i < 10; i++) {
		List.ProcessList();
	}
	List.Answer();
}
