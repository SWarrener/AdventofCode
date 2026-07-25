// https://adventofcode.com/2015/day/12
using System.Text.RegularExpressions;

namespace CsharpAoC.Year2015.Day12;

public class Solution : ISolver
{
    public string Part1(string[] input)
    {
        int total = 0;

        // For each substring use regex to find the numbers, then sum them together
        foreach (string substr in input)
        {
            var matches = Regex.Matches(substr, "-?\\d+");
            var values = matches.Cast<Match>().Select(match => int.Parse(match.Value)).ToArray();
            total = values.Sum();
        }

        return "" + total;
    }

    public string Part2(string[] input)
    {
        int total = 0;
        string totalString = string.Empty;

        // concat all the strings into one big string
        foreach (string substr in input)
        {
            totalString += substr.Trim();
        }

        int idx = 0;

        // Walk left and right from any problematic "red", until we find its surrounding object
        // bypassing any child objects. Then remove that object.
        // Only reds immediately preceeded by a colon are problematic
        while (totalString.IndexOf(":\"red\"") != -1)
        {
            idx = totalString.IndexOf(":\"red\"");
            int Rnests = 0, Lnests = 0;
            int left = idx, right = idx;
            bool foundleft = false, foundright = false;
            while (true)
            {
                if (!foundleft) left--;
                if (!foundright) right++;
                if (totalString[right] == '{')
                    Rnests++;
                else if (totalString[right] == '}' && Rnests == 0)
                    foundright = true;
                else if (totalString[right] == '}')
                    Rnests--;
                if (totalString[left] == '}')
                    Lnests++;
                else if (totalString[left] == '{' && Lnests == 0)
                    foundleft = true;
                else if (totalString[left] == '{')
                    Lnests--;
                if (foundleft && foundright)
                    break;
            }
            totalString = totalString.Remove(left, right - left + 1);
        }

        // Use regex to find all the numbers in the remaining string and sum them
        var matches = Regex.Matches(totalString, "-?\\d+");
        var values = matches.Cast<Match>().Select(match => int.Parse(match.Value)).ToArray();
        total = values.Sum();

        return "" + total;
    }
}
