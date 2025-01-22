

# Part 6: Age Difference Calculator
# Problem Statement:
# Write a program that:
# 1. Takes the ages of two people as input.
# 2. Calculates the difference in their ages using subtraction.
# Prints the result using string formatting:
# The age difference between [Person1] and [Person2] is: [Difference] years.


# get age of two person through user input
first_age = int(input("Enter first person's age: "))
second_age = int(input("Enter second person's age: "))

# validate ages (age cannot be negative or zero)
if first_age <= 0 or second_age <= 0:
  print("age cannot be negative, please proivde correct age: ")
else:

  # calulate the age differences
  result = first_age - second_age

  # display result
  print(f"The age difference between first person and second person is {result} years.")

