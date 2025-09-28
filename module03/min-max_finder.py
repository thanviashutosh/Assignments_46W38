# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a=[] # empty list

n=input("enter number of items in the list=") # input from user - number of items in the list

for i in range(int(n)):  # input all the numbers in the list
    b=input("number")
    a.append(b)     # appending all the numbers in the list
#a.sort()            # sorting the list
print("The list of number is:", a)   # printing the list

# max=a[int(n)-1]     #max number is the last number in the list
# min=a[0]            # min number is first number in the list


max= a[0]

for val in a:
    if val > max:
        max = val
        
        
min = a[0]

for val in a:
    if val < min:
        min =val
        
print("The minimal number is ",min) # printing the min number
print("The maximum number is ",max) # printing the max number
        
