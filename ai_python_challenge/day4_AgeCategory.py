# AgeCategory.py
# This script determines if someone is a child, teenager, adult, or senior based on their age.

def get_age_category(age):
    """Return age category based on the input age."""
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

# Ask user for age input
try:
    age = int(input("Enter your age: "))
    category = get_age_category(age)
    print(f"You are classified as: {category}")
except ValueError:
    print("Please enter a valid number for age!")
