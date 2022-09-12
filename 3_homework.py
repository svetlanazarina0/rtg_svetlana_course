
#ex1
 
user_temperature= input("Please enter your temperature ")

try:
    float(user_temperature)
except ValueError:
    print("Please enter valid number. Decimals should be seperated with .")
  

user_temperature= float(user_temperature)
type(user_temperature)
print(user_temperature)

if user_temperature<35:
    print("not too cold")
elif 35>= user_temperature <=37:
    print("all right")
elif user_temperature>37:
    print("possible fever")
else :
    print("error")





 #ex2
 # 2. Xmas Bonus
# The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of 
# service over 2 years.
# Task. Ask the user for the amount of the monthly salary and the number of years worked.
# Calculate the bonus.
# Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.
# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0)

salary = float(input("What is your montly salary? "))
years = float(input("Please enter number of years you have worked "))
bonus_perc = 0.15
if years < 2:
    print("No bonus yet")
else:
    print("Your bonus is " + str(salary * bonus_perc * (years-2)))