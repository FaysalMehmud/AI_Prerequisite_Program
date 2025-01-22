

# Part 1: Temperature Comparison
# Problem Statement:
# Write a program that:
# ● Takes input for the temperatures of two cities in Celsius.
# ● Compares the temperatures using relational operators (>, <, ==, !=).
# Prints a message like:
# City A is hotter than City B.

# to get temperature as user input for two cities.

islamabad_temp : int = int(input("Please enter Islamabad's temperature in celsius: "))
lahore_temp : int = int(input("Please enter Lahore's temperature in celsius: "))

if (islamabad_temp > 0) and (islamabad_temp > lahore_temp):
  print("Islamabad is hotter than Lahore")

elif (lahore_temp > 0) and (lahore_temp > islamabad_temp):
  print("Lahore is hotter than Islamabad")
else:
  print("Both cities tempreture is same")

