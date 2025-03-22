# Step 1: Create a Dictionary
days_in_month = {
    1: 31,  # January
    2: 28,  # February (default)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Step 2: Input Handling
month = int(input("Enter the month number (1-12): "))

# Step 3: Check and Output
if month in days_in_month:
    if month == 2:  # Check for February
        year = int(input("Enter the year: "))
        # Leap Year Adjustment
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("February has 29 days in the year", year)
        else:
            print("February has 28 days in the year", year)
    else:
        print(f"The month {month} has {days_in_month[month]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
