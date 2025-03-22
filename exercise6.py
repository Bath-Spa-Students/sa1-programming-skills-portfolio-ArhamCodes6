# Step 1: Define the correct password
correct_password = "12345"
max_attempts = 5
attempts = 0

# Step 2: Use a while loop to repeatedly ask for the password
while attempts < max_attempts:
    user_input = input("Enter the password: ")
    
    # Check if the entered password is correct
    if user_input == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Incorrect password. You have {remaining_attempts} attempts remaining.")
        
# Step 3: Inform the user if maximum attempts are reached
if attempts == max_attempts:
    print("Maximum attempts reached. Authorities have been alerted.")