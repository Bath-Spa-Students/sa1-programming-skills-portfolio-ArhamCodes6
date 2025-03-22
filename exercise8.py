# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Step 1: Allow the user to input the search term
search_term = input("Enter the name you want to search for: ")

# Step 2: Implement the search functionality
if search_term in names:
    print(f"{search_term} is found in the list.")
else:
    print(f"{search_term} is not found in the list.")