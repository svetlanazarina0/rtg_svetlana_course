# # 1. FizzBuzz 

# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 36, .... to 97, Buzz, 99, Fizz 

# So if number divided by 5 then Fizz If divided by 7 then Buzz,
#  If divided by 5 AND 7 then FizzBuzz otherwise the same number

#  Note: such a task became popular as the first task to ask to determine 
#  whether a person knows about programming at all smile


string=""
for i in range(1,101):
    string==""
    print(i)
    if i % 5 == 0 and i % 7 == 0:
        string = string + "FizzBuzz" + ","
    if i % 5 == 0:
        string = string + "Fizz" +","
        print(string)
    if i % 7 == 0:
        string = string + "Buzz" +","
   
    if i % 5 != 0 and i % 7 != 0:
        string = string + str(i)+","

        print(string)


#  2. Christmas tree 
# Ask user to enter the height of the tree 
# Then Print the tree: Ex. height == 3 
# The printout would be: 
#   * 
#  *** 
# ***** 
# Note: remember that several symbols can be printed at once, for example: print ("" * 10 + "*" * 6)

tree_height=int(input("Please enter height of the tree"))

print(tree_height)
stars=1

for i in range(1,tree_height+1):

    if i==1 : 
        print(" " * (tree_height-1) +  "*" * i)
    if i>1:
        start=start+2
        print(" " * (tree_height-i) +  "*" * stars)
 


 # 3. Primes Check if entered positive number is a prime number.

#  A prime number is a number that divides without remainder only by itself and 1.

# Hint: what numbers do we have to check?

n=int(input("Please enter positive number"))
prime=True
for i in range(2,1000):
    if (n%i) == 0 and i !=n:
        prime=False
        break

if prime==False:
    print(f"{n} is not a prime number")
else:  
    print(f"{n} is a prime number")



