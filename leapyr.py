# Ask the user for a year and determine if it's a leap year.

# This is my code that i was going to create 
# which is a totally wrong approach
# but with the help of ChatGpt i now know how to solve this

# import datetime

# datetime.datetime
# yr = int(input("Check if year is a leap year: "))


def check_leap_year(year):
    # Check if the year is divisible by 400 (leap year if true)
    if year % 400 == 0:
        return f"The year {year} is a leap year."
    
    # If the year is divisible by 100 but not by 400, it's not a leap year
    elif year % 100 == 0:
        return f"The year {year} is not a leap year."
    
    # If the year is divisible by 4 and not divisible by 100, it's a leap year
    elif year % 4 == 0:
        return f"The year {year} is a leap year."
    
    # Otherwise, it's not a leap year
    else:
        return f"The year {year} is not a leap year."

# Example usage
year = 2024
print(check_leap_year(year))
