// https://adventofcode.com/2015/day/11

namespace CsharpAoC.Year2015.Day11;

public class Solution: ISolver {
    // Iterate the password, checking each one
    public string Part1(string[] input) {
        string line = input[0];
        while (line != "zzzzzzzz") {
            line = IncrementString(line);
            if (ValidContains(line) & ValidPairs(line) & ValidStraight(line)) {
                return line;
            }
        }
        return "ERROR";
    }

    // Iterate the password, checking each one, and return the second correct result
    public string Part2(string[] input) {
        string line = input[0];
        int count = 0;
        while (line != "zzzzzzzz") {
            line = IncrementString(line);
            if (ValidContains(line) & ValidPairs(line) & ValidStraight(line)) {
                count++;
                if (count > 1) return line;
            }
        }
        return "ERROR";
    }

    //Increment the password, recursively going backwards through the letter in the string if we must
    private string IncrementString(string s) {
        char final = s[^1];
        if (final == 'z') {
            return IncrementString(s[..^1]) + 'a';
        }
        final++;
        return s[..^1] + final;
    }

    //Check if the string contains any bad characters
    private bool ValidContains(string s) {
        if (s.Contains('i') || s.Contains('o') || s.Contains('l')) {
            return false;
        }
        return true;
    }

    //Check for a valid straight
    private bool ValidStraight(string s) {
        for (int i = 0; i < s.Length - 2; i++) {
            if (s[i] + 1 == s[i+1] & s[i] + 2 == s[i+2]) {
                return true;
            }
        }
        return false;
    }

    //Check to see if there are two valid pairs.
    private bool ValidPairs(string s) {
        int pairs = 0;
        for (int i = 0; i < s.Length - 1; i++) {
            if (s[i] == s[i+1]) {
                pairs++;
                i++;
            }
        }
        return pairs >= 2;
    }
}
