

# Part 4: Two-Number Relationship
# Problem Statement:
# Write a program that:
# 1. Takes two numbers as input.
# 2. Checks and displays their relationship using these conditions:
# 3. Whether the first number is greater than, less than, or equal to the second number.
# 4. Whether both numbers are even or odd.

# Print the results in this format:
# Number 1: [num1]
# Number 2: [num2]
# Relationship: [Greater than/Less than/Equal]
# Both numbers are [Even/Odd/Mixed].


# get input from user

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

# to display user provided numbers

print(f"Number 1: {first_number}")
print(f"Number 2: {second_number}")

# display the relationship between numbers

if first_number == second_number:
  print(f"Relationship: both {first_number} and {second_number} are equal")
elif first_number > second_number:
  print(f"Relationship: {first_number} is greater than {second_number}")
else:
  print(f"Relationship: {first_number} is less than {second_number}")

# check if numbers are even or odd

if first_number %2 == 0 and second_number %2 == 0:
  print(f"both numbers are even")
elif first_number % 2!= 0 and second_number % 2!= 0:
  print(f"both numbers are odd")
else:
  print(f"both numbers are mixed (one is even, one is odd)")

