

# Part 3: Custom Message Formatter
# Problem Statement:
# Write a program that takes the following inputs:
# ● A name
# ● A favorite color
# ● A favorite number
# Use string formatting to display the result:

# [Name] loves the color [Color] and their favorite number is [Number].

your_name = input("Please enter your name: ")
favorite_color = input("What is your favorite color: ")
favorite_number = int(input("What is your favorite number: "))

print(f"{your_name} loves the color {favorite_color} and his favorite number is {favorite_number}.")

