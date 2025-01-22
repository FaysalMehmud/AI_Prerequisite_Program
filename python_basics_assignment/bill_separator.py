
# Part 2: Bill Splitter
# Problem Statement:
# Write a program that calculates how much each person needs to pay when splitting a bill:
# 1. Take the total bill amount as input.
# 2. Take the number of people as input.
# 3. Calculate each person’s share by dividing the total amount by the number of people.
# Print the result in this format:
# Total Bill: $[amount]
# Number of People: [people]
# Each Person Pays: $[share]

bill_amount = int(input("Plese enter total bill amount: "))
total_person = int(input("Number of person: "))

share_per_person = int(bill_amount / total_person)

print(f"Total bill Rs. {bill_amount}:")
print(f"Number of person: {total_person}")
print(f"Each person pays: {share_per_person}")

