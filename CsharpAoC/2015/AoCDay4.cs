// https://adventofcode.com/2015/day/4
using System.Security.Cryptography;
using System.Text;

namespace CsharpAoC.Year2015.Day4;

public class Solution: ISolver {
    public string Part1(string[] input) {
        return ""+FindLowest(input[0], "00000");
    }

    public string Part2(string[] input) {
        return ""+FindLowest(input[0], "000000");
    }

    // Quite simple making use of imports, simply test all possibilities until we find one
    // that matches. Surprisingly takes less than a second even for part 2.
    private static int FindLowest(string key, string zeroes) {
        string hash;
        
        int i = 0;
        do {
            i++;
            var bytes = Encoding.ASCII.GetBytes(key+i);
            hash = Convert.ToHexString(MD5.HashData(bytes));
        } while (!hash.StartsWith(zeroes));
        
        return i;
    }
}
