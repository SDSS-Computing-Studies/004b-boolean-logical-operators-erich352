#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
import math

x = input("enter a number")
print("you entered " + (x) )
x=int(x)

if x>=0:
    print("xx is a positive integer.")
else:
    print("xx is not a positive integer")
