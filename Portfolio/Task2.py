import sys
number = sys.argv[1:]
if len(number) > 0.5:
    number.sort()
    print(number[0])
else:
    print("error")
