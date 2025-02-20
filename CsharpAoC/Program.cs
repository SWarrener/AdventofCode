using Microsoft.Extensions.Configuration;

using CsharpAoC;

var config = new ConfigurationBuilder().AddCommandLine(args).Build();

var day = Convert.ToInt32(config["day"]);
var year = Convert.ToInt32(config["year"]);
var test = Convert.ToBoolean(Convert.ToInt32(config["test"]));

static void RunDay(int day, int year, bool test = true) {
    var path = year + "/AoCDay" + day + ".cs";
    if (!File.Exists(path)) {
        Console.Write($"That combination of year {year} and day {day} does not exist. Quitting.\n");
        Environment.Exit(1);
    }
    var module = "CsharpAoC.Year" + year + ".Day" + day + ".Solution";
    var type = Type.GetType(module);
    if (type == null) Environment.Exit(1);
    if (Activator.CreateInstance(type) is not ISolver solver) return;
    string[] input;
    if (test) {
        input = File.ReadAllLines(year + "/inputtest.txt");
    } else {
        input = File.ReadAllLines(year + "/input" + day + ".txt");
    }
    Console.WriteLine($"The answer to part 1 is: {solver.Part1(input)}");
    Console.WriteLine($"The answer to part 2 is: {solver.Part2(input)}");
}

RunDay(day, year, test);