number = input("Enter a number: ")  # Asking the user for a number
number = int(number)  # Converts the string to an int
print("The numbered entered was", number)  # Printing out the number entered
if (number % 10) == 0:  # checks if it can be divisible by 10
    print("The number you entered is divisible by 10")
    if (number % 2) == 0:  # Checking if the number is divisible by two
        print("That was an evan number")  # if it is then its evan
else:
    print("That is an odd number and not divisible by 10")  # if not it is odd
