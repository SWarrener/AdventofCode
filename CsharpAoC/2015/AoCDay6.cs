// https://adventofcode.com/2015/day/6
using System.Text.RegularExpressions;

namespace CsharpAoC.Year2015.Day6;

public partial class Solution: ISolver {
    public string Part1(string[] input) {
        
        Dictionary<(int, int), bool> lights = [];
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++){
                lights.Add((i,j), false);
            }
        }

        var instructions = DecodeInstructions(input);
        
        foreach (var instruction in instructions) {
            ProcessPart(instruction, ref lights);
        }
        return ""+lights.Count(x => x.Value);
    }

    public string Part2(string[] input) {
        Dictionary<(int, int), int> lights = [];
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++){
                lights.Add((i,j), 0);
            }
        }

        var instructions = DecodeInstructions(input);
        
        foreach (var instruction in instructions) {
            ProcessPart(instruction, ref lights);
        }
        return ""+lights.Select(x => x.Value).Sum();
    }
    
    // Use regex to extract the useful stuff out of the instructions.
    private static Tuple<int, int, int, int, string>[] DecodeInstructions(string[] input) {
        Tuple<int, int, int, int, string>[] instructions = [];
        foreach (var line in input) {
            var match = RegexPattern().Match(line);
            instructions = instructions.Append(new (int.Parse(match.Groups[2].Value),
                                                    int.Parse(match.Groups[4].Value), 
                                                    int.Parse(match.Groups[3].Value), 
                                                    int.Parse(match.Groups[5].Value), 
                                                    match.Groups[1].Value)).ToArray();
            
        }
        return instructions;
    }

    // Go through each instruction in the list and edit the grid of lights accordingly.
    private static void ProcessPart(Tuple<int, int, int, int, string> inst, ref Dictionary<(int, int), bool> lights) {
        for (var i = inst.Item1; i <= inst.Item2; i++) {
            for (var j = inst.Item3; j <= inst.Item4; j++) {
                lights[(i,j)] = inst.Item5 switch {
                    "turn on" => true,
                    "turn off" => false,
                    "toggle" => !lights.GetValueOrDefault((i,j), false),
                    _ => lights[(i,j)]
                };
            }
        }
    }

    // Go through each instruction, adjusting the brightness levels accordingly.
    private static void ProcessPart(Tuple<int, int, int, int, string> inst, ref Dictionary<(int, int), int> lights) {
        for (var i = inst.Item1; i <= inst.Item2; i++) {
            for (var j = inst.Item3; j <= inst.Item4; j++) {
                lights[(i,j)] = inst.Item5 switch {
                    "turn on" => lights[(i,j)] + 1,
                    "turn off" => int.Max(0, lights[(i,j)] - 1),
                    "toggle" => lights[(i,j)] + 2,
                    _ => lights[(i,j)]
                };
            }
        }
    }

    [GeneratedRegex(@"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")]
     private static partial Regex RegexPattern();
}
