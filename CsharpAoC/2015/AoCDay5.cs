// https://adventofcode.com/2015/day/5

namespace CsharpAoC.Year2015.Day5;

public class Solution: ISolver {
    public string Part1(string[] input) {
        int total = input.Select(IsNiceOne).Sum();
        return ""+total;
    }

    public string Part2(string[] input) {
        int total = input.Select(IsNiceTwo).Sum();
        return ""+total;
    }

    // Check for each of the three rules specified. 
    private static int IsNiceOne(string str) {
        int vowel_count = 0;
        char[] vowels = ['a','e','i','o','u'];
        
        foreach (char character in str) {
            if (vowels.Contains(character)) {
                vowel_count++;
            }
        }
        if (vowel_count < 3) {
            return 0;
        }

        string[] forbidden = ["ab", "cd", "pq", "xy"];
        foreach (var compare in forbidden) {
            if (str.Contains(compare)) {
                return 0;
            }
        }

        for (int i = 0; i < str.Length-1; i++) {
            if (str[i] == str[i+1]) {
                return 1;
            }
        }
        return 0;
    }

    // Check for the two rules specified, if both are true return 1 else return 0.
    private static int IsNiceTwo(string str) {
        bool rule_1 = false, rule_2 = false;

        for (int i = 0; i < str.Length-2; i++) {
            if (str[i] == str[i+2]) {
                rule_1 = true;
                break;
            }
        }

        for (int i = 0; i < str.Length-1; i++) {
            string pair = str.Substring(i,2), removed = str.Remove(0,i).Remove(0,2);
            if (removed.Contains(pair)) {
                rule_2 = true;
                break;
            }
        }

        if (rule_1 & rule_2){
            return 1;
        }
        return 0;
    }
}
