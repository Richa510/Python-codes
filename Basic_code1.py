# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 19:35:15 2021

@author: Richa Singh
"""

#to print the multiplication table

num = int(input("Enter the number to get the multiplication table:"))
print("the multiplication table of",num)
i = 1
while i <= 10:
    n=num*i
    print(num,"X",i,"=",n)
    i = i + 1
    
#%%
#accept a sentence and split it into words
line = input("Enter the sentence:")   
word = line.split()
print(word)


#%%
#accept a string and print its length
String = input("The string is:")
length = len(String)
print(length)


#convert to uppercase
print(String.upper())

#count the character
counter = String.count('h')
print(counter)

#reverse the string
def reverse(String):
    String = String[::-1]
    return String
  
print ("The reversed string is : ",end="")
print (reverse(String))
#%%

#accept and print roots of a quadratic equation
import cmath
print ("Quadratic Equation: ax^2 + bx + c")
a=int(input("Enter the value for a:"))
b=int(input("Enter the value for b:"))
c=int(input("Enter the value for c:"))

d=b**2-4*a*c
d1=d**0.5
root1=(-b+d1)/2*a
root2=(-b-d1)/2*a
print("the first root is:",root1)
print("the second root is:",root2)
