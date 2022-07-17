"""
# Lets consider following example:
square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num * num
print(square_dict)
-------------------------------------------------------------------

2. Dict comprehension:
     - it is data types in Python which allows us to store data in key/value pair.
     - it is an elegant and concise way to create dictionaries.
------------------------------------------------------------------------------------
syntax:
    {expression(key:value) for i in sequence}
---------------------------------------------------------------

ls = ['Kajal', 'Asha', 'Rani', 'manisha', 'Jaya', 'VIDYA']
# Expected output:{'Kajal': 5.....}
print({len(i): i for i in ls})      # duplicate keys can not be allowed
print({i: len(i) for i in ls})
-------------------------------------------------------------------

ls = ['Kajal', 'Asha', 'Rani', 'manisha', 'Jaya', 'VIDYA']
# Expected output:{'Kajal': 'name'.....}
print({i: 'name' for i in ls})
------------------------------------------------------------------

# square of number 1 to 10
square_dict = {num: num * num for num in range(1, 11)}
print(square_dict)
-------------------------------------------------------------------

#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
print({item: value * dollar_to_pound for (item, value) in old_price.items()})
-----------------------------------------------------------------------------

# If Conditional Dictionary Comprehension
original_dict = {'mary': 38, 'michael': 48, 'prince': 57, 'john': 33}
print({k: v for (k, v) in original_dict.items() if v % 2 == 0})
--------------------------------------------------------------------------

# Multiple if Conditional Dictionary Comprehension
original_dict = {'mary': 38, 'michael': 48, 'prince': 57, 'john': 33}
print({k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40})
---------------------------------------------------------------------------

# if - else Conditional
original_dict = {'jennifer': 38, 'michael': 48, 'johnny': 50, 'john': 33}
print({k: ('old' if v > 40 else 'young') for (k, v) in original_dict.items()})
-----------------------------------------------------------------------------

# Nested Dictionary with Two Dict
dict = {k1: {k2: k1 * k2 for k2 in range(1, 5)} for k1 in range(2, 5)}
print(dict)
---------------------------------------------------------------------------

# we can use the enumerate function
# The enumerate function can be used to create an iterable of tuples based on a list.
ls = ['sunil', 'shubham', 'kajal', 'sidd', 'vijay', 'ranjana']
print({i: len(j) for i, j in enumerate(ls)})
print(dict(enumerate(ls)))
-------------------------------------------------------------------------

a = [1, 2, 3]
b = [5, 6, 7]
print({(i, j): i * j for i in a for j in b})
-----------------------------------------------------------------------

ls = ['Kajal', 'Asha', 'Ranjeet', 'manisha', 'Jaya', 'VIDYA']
print({i: len(i) if len(i) > 4 else 'short' for i in ls})
------------------------------------------------------------------------
"""

