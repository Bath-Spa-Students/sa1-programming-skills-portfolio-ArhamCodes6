def check_even_odd(number):
    """Function to determine if a number is even or odd."""
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

def main():
    # Ask the user for a number
    user_input = int(input("Enter a number: "))
    
    # Call the function and store the result
    result = check_even_odd(user_input)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()