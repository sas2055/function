"""
# Lets consider following example:
ls = ['Kajal', 'Asha', 'Rani', 'manisha', 'Jaya', 'VIDYA']
# i want new list in which all names in CAPITAL
new = []
for nm in ls:
    #print(nm.upper())
    new.append(nm.upper())
print(new)
----------------------------------------------------------------

1. List Comprehension:
    - it is used for creating new lists from other iterables like tuples, strings, arrays, lists, etc.
    - it is a short way to reduce number of lines.
    - it is best for one line solution.
---------------------------------------------------------------------------------------

Syntax:
[expression for val in sequence]
[expression for val in sequence if condition]
-----------------------------------------------------------------------------------

# the above example we can solve using this to give a small, and concise solution
ls = ['Kajal', 'Asha', 'Rani', 'manisha', 'Jaya', 'VIDYA']
print([nm.upper() for nm in ls])
----------------------------------------------------------------------------

ls = ['Kajal', 'Asha', 'Rani', 'manisha', 'Jaya', 'VIDYA']
# i want list of tuple
# [(name, len(name)]
print([(nm.upper(), len(nm)) for nm in ls])
----------------------------------------------------------------------------

ls = ['Kajal', 'Asha', 'Rani', 'manisha', 'Jaya', 'VIDYA']
# i want list of names whose length is > 4
print([nm for nm in ls if len(nm) > 4])
------------------------------------------------------------------------------

ls = ['Kajal', 'Asha', 'Rani', 'manisha', 'Jaya', 'VIDYA']
# i want list of names whose name contains 'i'
print([nm for nm in ls if 'i' in nm.lower()])
------------------------------------------------------------------------

ls = ['Kajal', 'Asha', 'Rani', 'manisha', 'Jaya', 'VIDYA']
# fetch the name whose endswith 'i'
print([nm for nm in ls if nm.endswith('i') ])
------------------------------------------------------------------------

# fetch even numbers
print([x for x in range(10) if x % 2 ==  0])
--------------------------------------------------------------------

# fetch odd numbers
print([x for x in range(10) if x % 2 !=  0])
-------------------------------------------------------------------

k = [10, 20, 30, 40, 50]
# set a constant value at each place
# take constant as 0
print([0 for i in k])
print(['Constant' for i in k])
-----------------------------------------------------------------------

k = [10, 20, 30, 40, 50]
# add 100 in each element
add = lambda i: i + 100
print([add(i) for i in k])
print([i + 100 for i in k])
----------------------------------------------------------------

# Use of ternary operator in List comprehension
ls = ['Kajal', 'Asha', 'Rani', 'manisha', 'Jaya', 'VIDYA']
# Assign Group 1 to the student whose name ends with a
# else will go to Group 2
print(['Group_1' if x.lower().endswith('a') else 'Group_2' for x in ls])
---------------------------------------------------------------

# flipkart: apply charges for purchase of below 499
# otherwise free delivery
cart = [499, 1000, 2999, 199, 154]
print(['Free delivery' if p > 499 else '+Rs.40 charges applied' for p in cart])
------------------------------------------------------------------------

# Accept only numbers lower than 5
print([x for x in range(10) if x < 5])
-------------------------------------------------------------------------

# Nested If condition
# expected output: [0, 10, 20, ..........]
print([y for y in range(100) if y % 2 == 0 if y % 5 == 0])
---------------------------------------------------------------------

# we can use the enumerate function
# The enumerate function can be used to create an iterable of tuples based on a list.
ls = ['sunil', 'shubham', 'kajal', 'sidd', 'vijay', 'ranjana']
print(list(enumerate(ls)))
====================================================================
"""
