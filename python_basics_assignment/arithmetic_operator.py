

# Part 8: Arithmetic Checker
# Problem Statement:
# Write a program that:
# 1. Takes two numbers as input.
# 2. Prompts the user to input an arithmetic operator (+, -, *, /).
# Performs the operation on the numbers and prints the result.
# [Number1] [Operator] [Number2] = [Result]


# get two number from the user

first_number : int = int(input("Enter your first number: "))
second_number : int = int(input("Enter your second number: "))

# get arithmetic operator (+,-,*,/) from the user
arithmetic_operator = input("Enter arithmetic operator (+,-,*,/): ")

# calculation on given two numbers
if arithmetic_operator == "+":
  addition = first_number + second_number
  print(f"{first_number} {arithmetic_operator} {second_number} = {addition}")
elif arithmetic_operator == "-":
  subtraction = first_number - second_number
  print(f"{first_number} {arithmetic_operator} {second_number} = {subtraction}")
elif arithmetic_operator == "*":
  multiplication = first_number * second_number
  print(f"{first_number} {arithmetic_operator} {second_number} = {multiplication}")
elif arithmetic_operator == "/":
  division = first_number / second_number
  print(f"{first_number} {arithmetic_operator} {second_number} = {division}")

