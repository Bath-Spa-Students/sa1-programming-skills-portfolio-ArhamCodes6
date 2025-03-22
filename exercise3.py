# Description: This program asks the user for their first name, last name, age, and hometown. It then prints out the user's information.
# The user's first name is stored in the variable first_name.
first_name = str(input("Enter your first name: "))
# The user's last name is stored in the variable last_name.
last_name = str(input("Enter your last name: "))
# The user's age is stored in the variable age.
age = int(input("Enter your age: "))
# The user's hometown is stored in the variable hometown.
hometown = str(input("Enter your hometown: "))
print(first_name)
print(last_name)
print(age)
print(hometown)
print("Hello, my name is " + first_name + " " + last_name + " and I am " + str(age) + " years old. I come from " + hometown + ".")