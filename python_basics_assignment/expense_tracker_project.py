
# Assignment # 2

"Expense Tracker and Financial Health Checker"


# 1- User Profile Setup
# ask user for name & profession

user_name : str = input("Please enter your name: ")
user_profession : str = input("Please enter your profession: ")

# greeting & welcome to user

print(f"Welcome! {user_name}. Let's analyze your financial health as a {user_profession}.")
print("\n")

# 2- Income & Expense Management
# ask for user's income & expenses

user_monthly_income : int = int(input("Please enter your monthly income: "))
user_monthly_expense : int = int(input("Please enter your monthly expense: "))

# saving for the month

saved_monthly : int = user_monthly_income - user_monthly_expense
print(f"Total savings: {saved_monthly}")

# percentage of income saved.

percentage_income_saved : float = (saved_monthly / user_monthly_income) * 100
print(f"Saving percentage: {percentage_income_saved}%")

# 3- Financial Health checker
# check for saving percentage habit from "best","best" to "poor"

if percentage_income_saved >= 20:
  print(f"Great Job, {user_name}! You have a strong savings habit")
elif (percentage_income_saved >= 10) and percentage_income_saved < 20:
  print(f"Good, {user_name}, but you could save a bit more.")
elif percentage_income_saved < 10:
  print(f"Warning {user_name}: Your saving are too low! Consider cutting expenses!")
print("\n")

# 4. Categorize Expenses:
# categorize your expnese in three major areas:

essentials_expense : int = int(input("How much do you spend on Essentials: (rent,utiliies,groceries) "))
wants_expnese : int = int(input("How much do you spend on Wants: (dining out,entertainment) "))
investment_and_saving : int = int(input("How much do you save on invest: "))

# summrize expenses in percentage

print(f"""

Expense Breakdown:
Essentials: {essentials_expense / user_monthly_expense * 100}%
Wants: {wants_expnese / user_monthly_expense * 100}%
Saving/Investments: {investment_and_saving / user_monthly_expense * 100}%

""")

# 5- Custom goals
# allow user to get goal (user define)

user_goal : int = int(input("Please enter your saving goal: "))

# calculate percentage behind goal

# evaluate if they are meeting their goals
if percentage_income_saved >= user_goal:
  print(f"Congratulations, {user_name}! You 've achieved your saving goal. ")
else:
  print(f"""Your saving percentage is {percentage_income_saved}%.
   Keep working on your saving, {user_name}. You're {percentage_income_saved - user_goal}% away from your goal. """)

#6- summary of user's financial health.

print(f"""

Financial Health Summary for {user_name}:

Income: {user_monthly_income}
Expenses: {user_monthly_expense}
saving: {saved_monthly} ({percentage_income_saved}%)
Expense Breakdown:
  Essentials: {essentials_expense / user_monthly_expense * 100}%
  Wants: {wants_expnese / user_monthly_expense * 100}%
  Saving/Investments: {investment_and_saving / user_monthly_expense * 100}%
Saving Goal: {user_goal}%
Status: {percentage_income_saved - user_goal}% away from your goal

""")

""" 
Output Result:
Please enter your name: Faisal  Mehmood
Please enter your profession: Accountant
Welcome! Faisal  Mehmood. Let's analyze your financial health as a Accountant.


Please enter your monthly income: 50000
Please enter your monthly expense: 40000
Total savings: 10000
Saving percentage: 20.0%
Great Job, Faisal  Mehmood! You have a strong savings habit


How much do you spend on Essentials: (rent,utiliies,groceries) 20000
How much do you spend on Wants: (dining out,entertainment) 10000
How much do you save on invest: 10000


Expense Breakdown:
Essentials: 50.0%
Wants: 25.0%
Saving/Investments: 25.0%


Please enter your saving goal: 10
Congratulations, Faisal  Mehmood! You 've achieved your saving goal.


Financial Health Summary for Faisal  Mehmood:

Income: 50000
Expenses: 40000
saving: 10000 (20.0%)
Expense Breakdown:
  Essentials: 50.0%
  Wants: 25.0%
  Saving/Investments: 25.0%
Saving Goal: 10%
Status: 10.0% away from your goal

"""