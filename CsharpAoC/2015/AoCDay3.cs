// https://adventofcode.com/2015/day/3

namespace CsharpAoC.Year2015.Day3;

public class Solution: ISolver {
    public string Part1(string[] input) {
        return ""+Solve(input[0], 1);
    }

    public string Part2(string[] input) {
        return ""+Solve(input[0], 2);
    }

    // Iterate through the line, for part 2 switch between each santa every other character.
    private static int Solve(string input, int santas = 1) {
        HashSet<Tuple<int, int>> locations = new() {new (0,0)};
        int x = 0, y = 0, rx = 0, ry = 0, idx = -1;
        foreach (var c in input) {
            idx++;
            if (idx % santas == 0) {
                Move(c, ref x,  ref y);
                locations.Add(new (x,y));
            } else if (idx % santas == 1) {
                Move(c, ref rx, ref ry);
                locations.Add(new (rx,ry));
            }
        }
        return locations.Count;
    }

    // Move the relevant santa according the instructions, coords are passed by reference.
    private static void Move(char c, ref int x, ref int y) {
        switch (c) {
            case '^':
                y++;
                break;
            case '>':
                x++;
                break;
            case '<':
                x--;
                break;
            case 'v':
                y--;
                break;
        }
    }
}
