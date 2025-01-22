

# Part 5: Rectangle Calculator
# Problem Statement:
# Write a program that calculates and displays the area and perimeter of a rectangle:
# 1. Take the length and width of the rectangle as inputs.
# 2. Calculate the area and perimeter using basic arithmetic operators.
# Print the result in this format:
# Length: [length]
# Width: [width]
# Area: [area]
# Perimeter: [perimeter]

# get the length and width of rectangle from the user

rectangle_length = int(input("Enter length of rectangle: "))
rectangle_width = int(input("Enter width of rectangle: "))

# validate input (length and width must be positive)

if rectangle_length <= 0 or rectangle_width <= 0:
  print("Length and width must be positive numbers: ")
else:

  # calculation for area and perimeter of rectangle

  rectangle_area = rectangle_length * rectangle_width
  rectangle_perimeter = 2 * (rectangle_length + rectangle_width)

  # display result of calculation

  print(f"Length: {rectangle_length}")
  print(f"Width: {rectangle_width}")
  print(f"Area: {rectangle_area}")
  print(f"Perimeter: {rectangle_perimeter}")

