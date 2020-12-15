#!/usr/bin/env dotnet-script

using System.Diagnostics;

 var text = System.IO.File.ReadLines("input").First();

public int run(int turns) {
    var sw = Stopwatch.StartNew();
    var p = Process.GetCurrentProcess();
    var pStart = p.UserProcessorTime.TotalMilliseconds;

    var digits = new Dictionary<int, int>();
    var index = 0;
    int nextValue = 0;

    foreach(var digit in text.Split(',').ToList()) {
        var num = int.Parse(digit);

        nextValue = digits.ContainsKey(num) ? index - digits[num] : 0;

        digits[num] = index++;
    }

    while(index < turns - 1) {
        int value = nextValue;
        nextValue = index - digits.GetValueOrDefault(nextValue, index);
        digits[value] = index++;
    }

    sw.Stop();
    Console.WriteLine(sw.Elapsed.TotalSeconds);

    Console.WriteLine(p.UserProcessorTime.TotalMilliseconds - pStart);

    return nextValue;
}

Console.WriteLine(run(2020));

Console.WriteLine(run(30000000));
