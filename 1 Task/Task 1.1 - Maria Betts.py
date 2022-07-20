# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 19:30:42 2022

@author: Maria Betts

Task #1 : Create a function that accepts three parameters: n - text,
a - text with positive characters, b - text with negative characters.
Positive characters are worth 1, negative characters are -1, and characters
that are not in either a or b are worth 0. The function calculates a text score and returns it.
"""

n = (input("Input the first string: "))
a = (input("Input the positive characters: "))
b = (input("Input the negative characters: "))

positive_chars = len(a) ## converts the characters from a string to an int
negative_chars = len(b)

if len(a) >= len(b): ## if a is greater or equal to B it'll be positive
    print("1")
    
elif len(a) << len(b): ## if a is less than, it'll be negative
    print("-1")
    




     
     
     
     
    


    