import sys


def average(values):
    """ Calculates the average of the given list. """
    total = 0
    for n in values:  # total the given values
        total += float(n)
    return total / len(values)  # return calculated average


# initialisation statement
if __name__ == "__main__":
    TotalAll = 0
    values = sys.argv[1:]
    try:
        if len(values) > 0.5:
            for n in values:
                TotalAll += float(n)
        else:
            print("No agreements were taken")
        print("The average is", TotalAll / len(values))
    except ZeroDivisionError:
        pass
