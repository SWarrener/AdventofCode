// https://adventofcode.com/2015/day/10

using System.Text.RegularExpressions;

namespace CsharpAoC.Year2015.Day10;

public class Solution: ISolver {
    public string Part1(string[] input) {
        return ""+CalcResult(40, input[0]);
    }

    public string Part2(string[] input) {
        return ""+CalcResult(50, input[0]);
    }

    // Run the loop the specified number of iterations. We simply run calculate the next step stage
    // by stage. No fancy time saving logic
    private static int CalcResult(int iterations, string input) { 
        for (int i = 0; i < iterations; i++) {
            input = StringAttacher(StringSplitter(input));
        }
        return input.Length;
    }

    // This splits the string on each change in character so 1122113 becomes [11,22,11,3]
    private static string[] StringSplitter(string line) {
        var matches = Regex.Matches(line, "(.)\\1*");
        return matches.Cast<Match>().Select(match => match.Value).ToArray();
    }

    // This performs the look-and-say step turning 11,444,2 into 21,34,12 and then combines that all
    // into a single string.
    private static string StringAttacher(string[] data) {
        return string.Join("", data.Select(part => Convert.ToString(part.Length) + part[0]));
    }

}

