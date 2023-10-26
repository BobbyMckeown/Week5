import sys

totalAll = 0
values = sys.argv[1:]
try:
    if len(values) > 0.5:
        for n in values:
            totalAll += float(n)
    else:
        print("No agreements were taken")
    print("The average is", totalAll / len(values))
except ZeroDivisionError:
    pass



