// https://adventofcode.com/2015/day/9

namespace CsharpAoC.Year2015.Day9;

public class Solution: ISolver {
    public string Part1(string[] input) {
        (List<string> location_names, List<Tuple<string, int, string>> connections) = ProcessInput(input);
        int p1_ans = int.MaxValue;
        foreach (string name in location_names) {
            p1_ans = int.Min(p1_ans, Pathfind(name, connections, location_names.Count));
        }
        return ""+p1_ans;
    }

    public string Part2(string[] input) {
        (List<string> location_names, List<Tuple<string, int, string>> connections) = ProcessInput(input);
        int p2_ans = int.MinValue;
        foreach (string name in location_names) {
            p2_ans = int.Max(p2_ans, Pathfind(name, connections, location_names.Count, true));
        }
        return ""+p2_ans;
    }

    class Path(string location, HashSet<string> closed_list, int score = 0) {
        public int Score => score;
        public string Location => location;
        public HashSet<string> Closed_List => closed_list;

        public void AddToCL(string loc) {
            this.Closed_List.Add(loc);
        }

        public bool CheckCL(string loc) {
            return this.Closed_List.Contains(loc);
        }

        public int CLLength() {
            return this.Closed_List.Count;
        }
    }

    private (List<string>, List<Tuple<string, int, string>>) ProcessInput(string[] input) {
        List<string> locations = [];
        List<Tuple<string, int, string>> connections = [];
        foreach (var line in input) {
            int distance = Convert.ToInt32(line[line.LastIndexOf(' ')..]);
            var places = line[..line.IndexOf(" =")].Split(" to ");
            foreach (var place in places) {
                if (!locations.Contains(place)) {
                    locations.Add(place);
                }
            }
            connections.Add(new (places[0], distance, places[1]));
            connections.Add(new (places[1], distance, places[0]));
        }
        return (locations, connections);
    }

    static private int Pathfind(string start, List<Tuple<string, int, string>> connections, int locations, bool p2 = false) {
        PriorityQueue<Path, int> open_list = p2 ? new(new IntMaxCompare()) : new();
        open_list.Enqueue(new Path(start, []), 0);
        while (true) {
            var current = open_list.Dequeue();
            current.AddToCL(current.Location);
            if (current.CLLength() >= locations) {
                return current.Score;
            }
            foreach (var connection in connections.Where(x => x.Item1 == current.Location)) {
                if (!current.CheckCL(connection.Item3)) {
                    int score = current.Score + connection.Item2;
                    open_list.Enqueue(new Path(connection.Item3, new(current.Closed_List), score), score);
                }
            }
        }
    }

    private class IntMaxCompare : IComparer<int> {
        public int Compare(int x, int y) => y.CompareTo(x);
    }
}
