# EvenOddChecker.py
# This script checks whether a number is even or odd.
# Then it checks a list of numbers and prints their status.

def check_even_odd(number):
    """Check if a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Step 1: Check a single number
try:
    num = int(input("Enter a number to check if it's Even or Odd: "))
    result = check_even_odd(num)
    print(f"The number {num} is {result}.")
except ValueError:
    print("Please enter a valid integer!")

# Step 2: Check a list of numbers
print("\nChecking a list of numbers: [3, 4, 7, 10, 13, 22]")
numbers = [3, 4, 7, 10, 13, 22]

for n in numbers:
    status = check_even_odd(n)
    print(f"{n} is {status}")
 