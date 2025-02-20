// https://adventofcode.com/2015/day/2

namespace CsharpAoC.Year2015.Day2;

public class Solution: ISolver {

    // For each line of input split the string and then perform the maths as specified in the puzzle
    public string Part1(string[] input) {
        int ans = 0;
        foreach (var line in input) {
            int[] dimensions = line.Split('x').Select(i => Convert.ToInt32(i)).ToArray();
            int[] areas = [];
            for (int i = 0; i < dimensions.Length; i++) {
                areas = areas.Append(2 * dimensions[i] * dimensions[(i+1) % dimensions.Length]).ToArray();
            }
            ans += areas.Sum() + areas.Min()/2;
        }
        return ""+ans;
    }

    // Similar to above, but order the dimensions to make it easier to find lowest and second lowest sides
    public string Part2(string[] input) {
        int ans = 0;
        foreach (var line in input) {
            int[] dim = line.Split('x').Select(i => Convert.ToInt32(i)).Order().ToArray();
            ans += dim[0]*2 + dim[1]*2 + dim[0]*dim[1]*dim[2];
        }
        return ""+ans;
    }
}