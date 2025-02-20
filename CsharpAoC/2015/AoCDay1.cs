// https://adventofcode.com/2015/day/1

namespace CsharpAoC.Year2015.Day1;

public class Solution: ISolver {

    // Iterate through each item, adding or subtracting one depending on the symbol
    public string Part1(string[] input) {
        int ans = 0;
        foreach (var item in input[0]) {
            if (item == '(') {
                ans++;
            } else if (item == ')') {
                ans--;
            }
        }
        return Convert.ToString(ans);
    }

    // Iterate through each item again, this time also keeping track of the index. When the
    // floor = -1, return the index. 
    public string Part2(string[] input) {
        int ans = 0, idx = 0;
        foreach (var item in input[0]) {
            if (item == '(') {
                ans++;
            } else if (item == ')') {
                ans--;
            }
            idx++;
            if (ans == -1) return ""+idx;
        }
        return Convert.ToString(ans);
    }
}