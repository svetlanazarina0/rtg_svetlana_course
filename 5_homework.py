name="Svetlana"

print(name[:])



# The user enters a name.

# You print user name in reverse (should begin with capital letter)
#  then extra text: ",a thorough mess is it not ", then the first name of the user name then "?"

# Example:

# Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?
#without built in
name=str.lower(input("Please enter your name"))
new_name=""
for i in range(1,len(name)+1):
    new_name=new_name+name[-i]
    print(name[-i])

name_formatted= str.upper(new_name[0])+str.lower(new_name[1:])
first_letter=str.upper(name[0])
print(f"{name_formatted}, a thorough mess is it not, {first_letter} ?")




# 2. Almost Hangman

# Write a program to recognize a text symbol
# The user (first player) enters the text.
# Only asterisks instead of letters are output.
# Assume that there are no numbers, but there may be spaces.
# The user (i.e. the other player) enters the symbol.
# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.
# Example:
# First input: Kartupeļu lauks -> ********* *****

# Second input: a -> *a****** *a***
# In principle, this is a good start to the game of hangman.
# https://en.wikipedia.org/wiki/Hangman_(game)

text=input("First player, please enter a text")

space = " "
asterisk="*"
new_text=""

for i in range(0,len(text)):
    if text[i]==space:
        new_text=new_text+ space  
    else: 
        new_text=new_text+ asterisk  


while new_text.find('*')>0:
    letter=input("Second player, please enter a letter")
   # letter="a"
    for i in range(0,len(text)):
        if text[i] == letter:
           new_text=new_text[:i]+letter+new_text[i+1:]

print(new_text)
 




