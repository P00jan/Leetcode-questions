"""
Anagram check questions

"""
from collections import Counter 
input1 = input("Enter 1st keyword:")
input2 = input("Enter 2nd keyword:")

if Counter(input1) == Counter(input2):
    print(True)
else:
    print(False)
    