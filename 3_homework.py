

user_temperature= input("Please enter your temperature ")
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





 
salary = float(input("What is your montly salary? "))
years = float(input("Please enter number of years you have worked "))
bonus_perc = 0.15
if years < 2:
    print("No bonus yet")
else:
    print("Your bonus is " + str(salary * bonus_perc * (years-2)))