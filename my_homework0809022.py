
# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: Let the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). year


import datetime
from datetime import date

username = input("What is your name?")
age= input(print(f"How old are you, {username}?"))
# print(username,age, sep=",")
current_year=date.today().year
# print(current_year)
age=int(age)
display_year=current_year+100-age
# print(display_year)
print(f"You will be 100 years old in year {display_year}")