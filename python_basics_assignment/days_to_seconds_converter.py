
# Part 7: Days to Seconds Converter
# Problem Statement:
# Write a program that:
# 1. Takes the number of days as input.
# 2. Converts the input into seconds using this formula:
# Seconds=Days×24×60×60
# Prints the result using string formatting:
# [Days] days are equal to [Seconds] seconds.

# get value of days from the user
user_days : int = int(input("Enter the number of days(convert days to seconds:"))

# validate days (days cannot be negative)
if user_days <= 0:
  print("Error: Number of days cannot be zero or negative, please enter a valid value: ")
else:

  # convert days to seconds
  converted_seconds = user_days * 24 * 60 * 60

  # display the result
  print(f"{user_days}: days are equal to {converted_seconds} seconds. ")

# Method Two:
# days to seconds converter through while loop

while True:
  # get value of days from the user
  user_days : int = int(input("Enter the number of days (convert days to second:) "))

  # validate days (days cannot be negative)
  if user_days > 0:
    #convert days to seconds
    converted_seconds = user_days * 24 * 60 * 60
    # display the result
    print(f"{user_days} day(s) is equal to  {converted_seconds} seconds.")
    break
  else:
    print(f"Error: Number of days cannot be zero or negative, please enter a valid value: ")

