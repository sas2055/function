"""
# using python map
# Que.1 SLP to listify the list of given strings individually
# to convert a given list of strings into list of lists
l = ['red', 'yellow', 'green', 'pink', 'orange', 'blue']
print(list(map(list, l)))
===========================================================

# Que.2 SLP to create a list containing the power of number in bases corresponding the index
num = [10, 20, 30, 40, 50]
index = [1, 2, 3, 4, 5]
print(list(map(pow, num, index)))

or
s = [10, 20, 30, 40]
print(list(map(pow, s, range(1, len(s) + 1))))
===========================================================

# Que.3 WAP to square the elements of a list
def square_num(n):
  return n * n


nums = [4, 5, 2, 9, 3]
print(list(map(square_num, nums)))
===========================================================

# Que.4 WAP to convert all the characters in uppercase and lowercase
and eliminate duplicate letters from a given sequence.
def change_cases(s):
    return str(s).upper(), str(s).lower()


char = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print(list(map(change_cases, char)))
=============================================================

# Que.5 WAP to add two given lists and find the difference between lists.
def addition_subtraction(x, y):
    return x + y, x - y


n1 = [6, 5, 3, 9]
n2 = [0, 1, 7, 7]
print(list(map(addition_subtraction, n1, n2)))
===================================================================

# Que.6 SLP to convert a given list of integers to list of strings.
nums_list = [1, 2, 3, 4]
print(list(map(str, nums_list)))
=================================================================

# Que.7 SLP to convert a given tuple of integers to list of strings.
nums_tuple = (0, 1, 2, 3)
print(tuple(map(str, nums_tuple)))
=================================================================

# Que.8 SLP to convert a given list of tuples to a list of strings
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(list(map(' '.join, colors)))
=================================================================

# Que.9 SLP to find circle areas of round and range function
circle_areas = [6.5, 9.5, 4, 56, 9, 32]
print(list(map(round, circle_areas, range(1, 5))))
================================================================

# Que.10 SLP to count the same pair in two given lists.
from operator import eq
num1 = [1, 2, 3, 4, 5, 6, 7, 8]
num2 = [2, 2, 3, 1, 2, 6, 7, 9]
print(sum(map(eq, num1, num2)))
======================================================================

# Que.11 WAP to the sum of elements of a given array of integers
from array import array


def array_sum(num_array):
    total = 0
    for i in num_array:
        total += i
    return total


num = array('i', [1, 2, 3, 4, 5, -4, -3])
print(array_sum(list(map(int, num))))
====================================================================

# Que.12 WAP to find the ration of positive numbers, negative numbers and zeroes in an array of integers.
from array import array


def plus_minus(num):
    n = len(num)
    n1 = n2 = n3 = 0
    for x in num:
        if x > 0:
            n1 += 1
        elif x < 0:
            n2 += 1
        else:
            n3 += 1
    return round(n1 / n, 2), round(n2 / n, 2), round(n3 / n, 2)


nums = array('i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
print(plus_minus(list(map(int, nums))))
================================================================

# Que.13 WAP to split a given dictionary of lists into list of dictionaries
def list_of_dict(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(list_of_dict(marks))
======================================================================

# Que.15 WAP to interleave two given list into another list randomly
import random


def randomly_interleave(num1, num2):
    result =  list(map(next, random.sample([iter(num1)]*len(num1) + [iter(num2)]*len(num2), len(num1)+len(num2))))
    return result


num1 = [1, 2, 7, 8, 3, 2]
num2 = [4, 9, 5, 6, 10, 4]
print(randomly_interleave(num1, num2))

or
import random
num1 = [1, 2, 7, 8, 3, 2]
num2 = [4, 9, 5, 6, 10, 4]
print(list(map(next, random.sample([iter(num1)]*len(num1) + [iter(num2)]*len(num2), len(num1)+len(num2)))))
===================================================================================
"""
