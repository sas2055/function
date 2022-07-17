"""
# Que.1 WAP given string covert to upper case
s = 'today is a cool and warmest day'
con = lambda s:s.upper()
print(con(s))
=================================================

# Que.2 WAP given string convert to list
s = 'today is a cool and warmest day'
ls = lambda s:s.split()
print(ls(s))
==================================================

# Que.3 WAP first character capital of each word of the given string
s = 'today is a cool and warmest day'
ls = lambda s:s.title()
print(ls(s))
=====================================================

# Que.4 WAP first character capital of the given string
s = 'today is a cool and warmest day'
ls = lambda s:s.capitalize()
print(ls(s))
========================================================

# Que.5 SLP to sort a list of dictionaries
models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Redmi', 'model': 2003 , 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Oppo', 'model': 37 , 'color': 'silver'}]
print(sorted(models, key = lambda x: x['color']))
=============================================================

# Que.6 WAP to find whether a given string starts with a given character
startswith = lambda x: True if x.startswith('P') else False
print(startswith('Python'))
startswith = lambda x: True if x.startswith('P') else False
print(startswith('java'))
===================================================================

# Que.7 WAP to extract year, month, date and time
import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time()
print(year(now), month(now), day(now))
print(time(now))
====================================================================

# Que.8 WAP to create Fibonacci series up to n
from functools import reduce
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                              range(n - 2), [0, 1])
print(fib_series(10))
print(fib_series(7))
===================================================================

# Que.9 SLP to sort each sublist of strings in a given list of lists
color = [['red', 'black'], ['yellow', 'brown'], ['pink', 'orange', 'green']]
print(tuple(sorted(x, key = lambda x:x[0]) for x in color))
===================================================================

# Que.10 SLP to sort a given list of lists by length and values
list1 = [[2], [0], [1, 3], [0, 4, 3, 7], [9, 11], [13, 15, 17]]
print(tuple(sorted(list1, key = lambda l: (len(l), l))))
==================================================================

# Que. 11 SLP to find the maximum value in a given heterogeneous list
list_val = ['Python', 3, 2, 4, 5, 'version']
print(max(list_val, key = lambda i: (isinstance(i, int), i)))
===================================================================

# Que.12 SLP to sort a given matrix in ascending order according to the sum of its rows
m1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(tuple(sorted(m1, key = lambda matrix_row: sum(matrix_row))))
=====================================================================

"""