// https://adventofcode.com/2015/day/13
namespace CsharpAoC.Year2015.Day13;

public class Solution: ISolver 
{
    List<List<string>> permutations = new();
    Dictionary<string, Dictionary<string, int>> scores = new();

    public string Part1(string[] input) 
    {
        ProcessInput(input);
        return ""+Solve();
    }

    public string Part2(string[] input) 
    {
        permutations.Clear();
        // Add me to their scores
        foreach (var kvp in scores)
        {
            kvp.Value.Add("Z", 0);
        }
        // Add my scores of them
        scores.Add("Z", new());
        foreach (string name in scores.Keys)
        {
            if (name == "Z") continue;
            scores["Z"].Add(name, 0);
        }

        return ""+Solve();
    }

    // Take the puzzle string and turn it into a dictionary
    private void ProcessInput(string[] input)
    {
        foreach (string substr in input)
        {
            int score = substr.Contains("gain") ? int.Parse(substr[substr.IndexOf(" ", substr.IndexOf("gain"))..substr.IndexOf("hap")]) :
                                                  int.Parse(substr[substr.IndexOf(" ", substr.IndexOf("lose"))..substr.IndexOf("hap")]) * -1;
            
            string name1 = substr[..substr.IndexOf(" ")];
            
            if (!scores.ContainsKey(name1))
            {
                scores.Add(name1, new());
            }
            scores[name1].Add(substr[substr.LastIndexOf(" ")..^1].Trim(), score);
        }
    }

    // Create all possible permutations and find the score for them.
    private int Solve()
    {
        Perm(scores.Keys.ToList(), scores.Keys.Count, 0);
        
        int max = 0;
        foreach (var x in permutations)
        {
            max = Math.Max(max, FindScore(x));
        }
        return max;
    }

    // Recursively get all seating permutations and add them to the list
    private void Perm(List<string> s, int n, int i)
    {
        if (i >= n - 1)
        {
            List<string> x = new();
            x.AddRange(s);
            permutations.Add(x);
        }

        else 
        {
            Perm(s, n, i+1);
            for (int j = i+1; j<n; j++){
                (s[i], s[j]) = (s[j], s[i]);
                Perm(s, n, i+1);
                (s[i], s[j]) = (s[j], s[i]);
            }
        }
    }

    // Go through the list and work out the score of this particular seating arrangement
    private int FindScore(List<string> places)
    {
        int result = 0;
        for (int i = 0; i < places.Count; i++)
        {
            result += scores[places[i]][places[(i+1) % places.Count]];
            result += scores[places[(i+1) % places.Count]][places[i]];
        }
        return result;
    }

}
