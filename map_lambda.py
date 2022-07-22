"""
# SLP - Single Line Program : using map and lambda
# Que.1 SLP to find out square of each element of list
ls = [12, 22, 30, 24, 15]
print(list(map(lambda num: num*num, ls)))
===================================================

# Que.2 SLP to find out sum of each element of list
ls = [11, 13, 16, 17, 18, 10, 20]
print(list(map(lambda num: num + num, ls)))
======================================================

# Que.3 SLP to find out subtract of 5 to each element of list
ls = [11, 23, 34, 12, 45, 20]
print(list(map(lambda num: num - 5, ls)))
=====================================================

# Que.4 SLP for upper case of each name of the list
names = ['Ajit', 'Anushka', 'Amit', 'Akshara', 'shivansh', 'shital', 'snehal']
print(list(map(lambda nm: nm.upper(), names)))
=======================================================

# Que.5 SLP for lower case of each name of the list
nms = ['AJIT', 'ANUSHKA', 'AMIT', 'AKSHARA', 'SHIVANSH', 'SHITAL', 'SNEHAL']
print(list(map(lambda nm: nm.lower(), nms)))
=======================================================

# Que.6 SLP to add three given lists
l1 = [12, 34, 2, 54, 7]
l2 = [23, 45, 6, 16, 9]
l3 = [1, 14, 6, 67, 48]
print(list(map(lambda x, y, z: x + y + z, l1, l2, l3)))
=========================================================

# Que.7 SLP to triple all numbers of given list of integer
ls = [1, 3, 4, 6, 4]
print(list(map(lambda a: a*3, ls)))

or
ls = [1, 3, 4, 6, 4]
print(list(map(lambda a: a + a + a, ls)))
=============================================================

# Que.6 SLP to difference between three given lists
l1 = [12, 34, 2, 54, 7]
l2 = [23, 45, 6, 16, 9]
l3 = [1, 14, 6, 67, 48]
print(list(map(lambda x, y, z: x - y - z, l1, l2, l3)))
===========================================================

# Que.7 SLP to convert all the characters in uppercase and lowercase
char = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print(list(map(lambda s:(s.upper(), s.lower()), char)))
===================================================================

# Que.8 SlP to add two given lists and find the difference between lists.
n1 = [6, 5, 3, 9]
n2 = [0, 1, 7, 7]
print(list(map(lambda x, y:(x+y, x-y), n1, n2)))
==================================================================

# Que.9 SLP to convert a given list of integers to list of strings.
nums_list = [1, 2, 3, 4]
print(list(map(lambda s:str(s), nums_list)))
=========================================================

# Que.10 SLP to convert a given list of tuples to a list of strings
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(list(map(lambda s:' '.join(s), colors)))
===============================================================

# Que.11 SLP to sort a list of tuples
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 82)]
print(list(map(lambda x: (x[0], x[1]), subject_marks)))
=====================================================================

# Que.12 SLP to find anagrams of string in a list of string
from collections import Counter
l1 = ['bat', 'mat', 'dad', 'bad', 'tset', 'rate']
l2 = ['tab', 'cut', 'dad', 'dab', 'test', 'great']
print(list(map(lambda x, y: (x, y, Counter(x) == Counter(y)), l1, l2)))
========================================================================

# Que.13 WAP to create a new list taking specific elements from a tuple
and convert a string value to integer.
data  = [('Ajit shelar', '8/12/1995', '50kg'), ('vijay shelar', '22/10/2002', '37kg')]
print(list(map(lambda x: x[0], data)))
print(list(map(lambda x: x[1], data)))
print(list(map(lambda x: int(x[2][:-2]), data)))
==================================================================

# Que.14 WAP to compute the square of first N Fibonacci numbers and generate a list of the numbers.
import itertools
n = 10
def fibonacci_nums(x=0, y=1):
  yield x
  while True:
    yield y
    x, y = y, x + y


print('First 10 Fibonacci numbers: ')
result = list(itertools.islice(fibonacci_nums(), n))
print(result)
print('\nAfter squaring fibonacci number list are: ')
print(list(map(lambda x: x * x, result)))
================================================================
"""
