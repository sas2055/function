"""
# Que.1 SLP for to fetch name starts with 'A'
names = ['Ajit', 'Anushka', 'Amit', 'Akshara', 'shivansh', 'shital', 'snehal']
print(list(filter(lambda nm: nm.startswith('A'), names)))
==============================================================

# Que.2 SLP for to fetch name starts with 's'
names = ['Ajit', 'Anushka', 'Amit', 'Akshara', 'shivansh', 'shital', 'snehal']
print(list(filter(lambda nm: nm.startswith('s'), names)))
===============================================================

# Que.3 SLP to fetch number of given list is divisible by 5
ls = [12, 22, 30, 24, 15, 11, 90]
print(list(filter(lambda num: num % 5 == 0 , ls)))
=============================================================

# Que.4 SLP to fetch even number of given list
ls = [12, 22, 30, 24, 15, 11, 90]
print(tuple(filter(lambda num: num % 2 == 0 , ls)))
=============================================================

# Que.5 SLP to fetch odd number of given list
ls = [12, 22, 30, 24, 15, 11, 90]
print(tuple(filter(lambda num: num % 2 != 0 , ls)))
============================================================

# Que.6 SLP find the values that are common to the two lists
l1 = [1, 2, 3, 4, 5, 6]
l2 = [1, 3, 6, 7, 8, 4]
print(list(filter(lambda x: x in l1, l2)))
============================================================

# Que.7 SLP sort of vowels in the given list
ch = ['a', 't', 'e', 'y', 'r','i']
v = ['a', 'e', 'i', 'o', 'u']
print(tuple(filter(lambda x: x in v, ch)))
===============================================================

# Que.8 SLP given a list of string find all palindromes
drome = ['madam', 'dad', 'review', 'sas', 'ajit', 'nitin', 'test']
print(list(filter(lambda x: x == x[::-1], drome)))
===============================================================

# Que.9 SLP a list of string with single character without duplicates
in_ls = ['t', 'u', 't', 'o', 'r', 'a', 'i']
print(list(filter(lambda x: x != 't', in_ls)))
===============================================================

# Que.10 SLP to find anagrams of string in a list of string
from collections import Counter
ls = ['add', 'dad', 'mad', 'cut', 'dad']
str = 'dad'
print(list(filter(lambda x: (Counter(str) == Counter(x)), ls)))
=====================================================================

# Que.11 sum the length of the names of a given list of names after removing the
names that starts with a lowercase letter.
names = ['anika', 'Dada', 'ruby', 'Raj', 'pari', 'Tanika']
print(len(''.join(list(filter(lambda nm: nm[0].isupper() and nm[1:].islower(), names)))))
==========================================================================

# Que.12 SLP to calculate the sum of the positive and negative numbers of a given list of numbers
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print(sum(list(filter(lambda nums: nums < 0, nums))))
print(sum(list(filter(lambda nums: nums > 0, nums))))
=========================================================================

# Que.13 SLP to calculate the sum of the positive and negative numbers of a given list
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print(sum(list(filter(lambda nums: (nums > 0, nums < 0), nums))))
==========================================================================

# Que.14 SLP to find intersection of two given arrays
array_num1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_num2 = [1, 2, 4, 8, 9]
print(list(filter(lambda x: x in array_num1, array_num2)))
===================================================================

# Que.15 SLP to find the values of length six in a given list
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(tuple(filter(lambda day: day if len(day)==6 else '', weekdays)))
=======================================================================

# Que.16 WAP to find the numbers of a given string and store them in a list, display the numbers which
 are bigger than the length of the list in sorted form.
str1 = 'ajit 2055 shiv 143 aju 1432 jaan 43'
str_num = [i for i in str1.split(' ')]
lenght = len(str_num)
number = sorted([int(x) for x in str_num if x.isdigit()])
print(list(filter(lambda x: x > lenght, number)))
============================================================================

# Que.17 WAP to find the list with maximum and minimum length


def max_length_list(input_list):
    max_length = max(len(x) for x in input_list)
    max_list = max(input_list, key=lambda i: len(i))
    return (max_length, max_list)


def min_length_list(input_list):
    min_length = min(len(x) for x in input_list)
    min_list = min(input_list, key=lambda i: len(i))
    return (min_length, min_list)


list1 = [[0], [1, 3], [5, 7, 4, 2], [], [13, 15, 17]]
print('\nList with maximum length of lists: ')
print(max_length_list(list1))
print('\nList with minimum length of lists: ')
print(min_length_list(list1))
========================================================
"""