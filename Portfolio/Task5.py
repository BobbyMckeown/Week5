import sys, statistics

TempReadings = sys.argv[1:]
if len(TempReadings) > 0.5:
    print(min(TempReadings), "This is the lowest number")
    print(max(TempReadings), "This is the biggest number")

