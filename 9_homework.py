# 1. Min, Avg, Max
# Write a function get_min_avg_max (sequence) that returns a tuple with three values, the smallest, the arithmetic mean, and the largest value in the string, respectively.
# Example:
# get_min_avg_max ([0,10,1,9]) -> (0,5,10)
# the incoming sequence can be a tuple or a list with numeric values.
import statistics
values  = [int(t) for t in input("Enter values separated by whitespace").split(" ")]
#print(values, min(values), statistics.mean(values), max(values))
values=tuple(min(values), statistics.mean(values), max(values))
print(values)
#not a function..

# Write a function that returns a tuple with common elements in three sequences. Inputs can be list, tuple, string.
# get_common_elements(seq1, seq2, seq3)
# Example:
# get_common_elements("abc", ['a', 'b'], ('b', 'c')) -> ('b',) # we return a tuple with a single element 
# # remember that we can convert strings to set with set(mystring), and set to tuple with tuple(myset)
# 2. b For those with some experience 
# BONUS:  make a function that can handle an arbitrary number of input sequences
# so function which takes any number of sequences and returns a tuple with common elements
# get_common_elements(seq1, seq2, seq3, seq4, seq5, seq6, seq7) etc :), so just like print takes any number of values


def get_common_elements(s1,s2,s3):
     return tuple(set(s1).intersection(set(s2).intersection(set(s3))))

 x, y, z = input("Enter three sequences, seperated by a whitespace: ").split()
get_common_elements(x,y,z)
# 3. Is there a pangram?
# Write a function is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz')
# that returns True when the text parameter contains all the letters passed in an alphabet.
# We return False otherwise
# pangram - sentence, word string containing all letters of the alphabet - https://en.wikipedia.org/wiki/Pangram
# We ignore spaces and believe that uppercase is as valid as lowercase, i. here A and a -> a
# print(is_pangram("The five boxing wizards jump quickly")) -> True
# print(is_pangram("Not a pangram")) -> False

def is_pangram(text, alphabet="abcdefghijklmnopqrstuvwxyz"):
        return set(alphabet).issubset(set(text))

print(is_pangram("the five boxing wizards jump quickly"))