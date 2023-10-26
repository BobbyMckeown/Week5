import sys

values = sys.argv[1:]
total = 0
for n in values:
    total += float(n)

print("The average is", total / len(values))
