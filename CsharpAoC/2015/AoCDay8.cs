// https://adventofcode.com/2015/day/8
using System.Text.RegularExpressions;

namespace CsharpAoC.Year2015.Day8;

public partial class Solution: ISolver {
    // Add 2 for the start and end '"', and then add the number of matches for the other escape sequences.
    public string Part1(string[] input) {
        int difference = 0;
        for (int i =0; i < input.Length; i++ ) {
            string line = input[i][1..^1];
            int hex = RegexPattern().Matches(line).Count, quotemark = line.CountSubstring("\\\""), slash = line.CountSubstring("\\\\");
            difference += hex*3 + quotemark + slash + 2;
        }
        return ""+difference;
    }

    // Add 4 for the new start and end, and then the number of new characters for the other escape sequences.
    public string Part2(string[] input) {
        int increase = 0;
        for (int i =0; i < input.Length; i++ ) {
            string line = input[i][1..^1];
            int hex = RegexPattern().Matches(line).Count, quotemark = line.CountSubstring("\\\""), slash = line.CountSubstring("\\\\");
            increase += hex + quotemark * 2 + slash * 2 + 4;
        }
        return ""+increase;
    }

    [GeneratedRegex(@"\\x[0-9A-Fa-f]{2}")]
    private static partial Regex RegexPattern();

}
