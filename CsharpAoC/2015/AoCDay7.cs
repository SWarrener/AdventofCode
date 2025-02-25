// https://adventofcode.com/2015/day/7

namespace CsharpAoC.Year2015.Day7;

public class Solution: ISolver {

    // Go through all the operations until a has been assigned, and then return that
    public string Part1(string[] input) {
        var wires = new Dictionary<string, int> {{"NULL", 1}};
        List<Junction> operations = [];
        ExtractData(ref wires, ref operations, input);
        while (wires["a"] == -1) {
            foreach (var junc in operations) {
                if (junc.OperationPossible(ref wires) & !junc.CheckDone()) {
                    junc.DoOperation(ref wires);
                    junc.MarkDone();
                }
            }
        }
        return ""+wires["a"];
    }

    // get the part1 answer, edit wire b and then repeat what we did for part 1.
    public string Part2(string[] input) {
        int b_value = Convert.ToInt32(Part1(input));
        var wires = new Dictionary<string, int> {{"NULL", 1}};
        List<Junction> operations = [];
        ExtractData(ref wires, ref operations, input);

        for (int i = 0; i < operations.Count; i++) {
            if (operations[i].GetTarget() == "b") {
                operations[i].SetInput(b_value);
            }
        }

        while (wires["a"] == -1) {
            foreach (var junc in operations) {
                if (junc.OperationPossible(ref wires) & !junc.CheckDone()) {
                    junc.DoOperation(ref wires);
                    junc.MarkDone();
                }
            }
        }
        return ""+wires["a"];
    }

    // Class for each operation. 
    private class Junction {
        
        private readonly string op, target, a, b;
        private int shift, input;
        private bool done = false;

        public Junction(string op, string target, string a, string b, int shift, int input) {
            this.op = op;
            this.target = target;
            this.a = a;
            this.b = b;
            this.shift = shift;
            this.input = input;
        }

        public void MarkDone() {
            this.done = true;
        }

        public bool CheckDone() {
            return this.done;
        }

        public void SetInput(int input) {
            this.input = input;
        }

        public string GetTarget() {
            return this.target;
        }

        // Checks if the inputs of an operation are valid, if they aren't we can't do it yet
        public bool OperationPossible(ref Dictionary<string, int> wires) {
            if (wires[a] != -1 & wires[b] != -1 | wires[a] != -1 & shift != -1 | wires[b] != -1 & input != -1) {
                return true;
            } else if (op == "NONE" & (wires[a] != -1 | input != -1)) {
                return true;
            }
            return false;
        }

        // Actually performs the operation according the the specification in the instructions.
        public void DoOperation(ref Dictionary<string, int> wires) {
            switch (op) {
                case "AND":
                    if (input == -1) {
                        wires[target] = wires[a] & wires[b];
                    } else {
                        wires[target] = input & wires[b];
                    }
                    break;
                case "OR":
                    wires[target] = wires[a] | wires[b];
                    break;
                case "LSHIFT":
                    wires[target] = wires[a] << shift;
                    break;
                case "RSHIFT":
                    wires[target] = wires[a] >> shift;
                    break;
                case "NOT":
                    wires[target] = ~wires[a];
                    break;
                case "NONE":
                    if (input == -1) {
                        wires[target] = wires[a];
                    } else {
                        wires[target] = input;
                    }
                    break;
            }
        }
    }

    // This horrific mess extracts the data out of the input file, and assigns default values as necessary.
    private static void ExtractData(ref Dictionary<string, int> wires, ref List<Junction> operations, string[] input) {
        foreach (string line in input) {
            string target, a, b = "NULL", op = "NULL";
            int shift = -1, inputnum = -1;
            target = line.Substring(line.LastIndexOf(' ')+1);
            if (line.Contains("NOT")) {
                op = "NOT";
                a = line.Substring(line.IndexOf(' ')+1, 2);
            } else if (line.Contains("AND")) {
                op = "AND";
                a = line[..line.IndexOf(' ')];
                b = line.Substring(line.IndexOf(' ', line.IndexOf(' ')+1)+1, 2);
            } else if (line.Contains("OR")) {
                op = "OR";
                a = line[..line.IndexOf(' ')];
                b = line.Substring(line.IndexOf(' ', line.IndexOf(' ')+1), 3);
            } else if (line.Contains("RSHIFT")) {
                op = "RSHIFT";
                a = line[..line.IndexOf(' ')];
                shift = Convert.ToInt32(line.Substring(line.IndexOf(' ', line.IndexOf(' ')+1)+1,2));
            } else if (line.Contains("LSHIFT")) {
                op = "LSHIFT";
                a = line[..line.IndexOf(' ')];
                shift = Convert.ToInt32(line.Substring(line.IndexOf(' ', line.IndexOf(' ')+1)+1,2));
            } else {
                op = "NONE";
                a = line[..line.IndexOf(' ')];
            }
            a = a.Trim();
            b = b.Trim();
            var numeric = int.TryParse(a, out inputnum);
            if (numeric) a = "NULL";
            if (!numeric) inputnum = -1;
            if (inputnum == -1) wires[a] = -1;
            if (b != "NULL") wires[b] = -1;
            wires[target] = -1;
            operations.Add(new (op, target, a, b, shift, inputnum));
        }
    }

}

