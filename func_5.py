"""
2. filter:  (func, iterable)
       - it used to filter out the values based on condition given inside a function.
       - it will return results for only True instances.
       - filter will give an original sequence or may be sub-sequence'
---------------------------------------------------------------------

k = [12, 45, 3, 67, 89, 90, 1, 23, 44, 68, 22]
# filter out even number from above sequence
even = lambda no : no % 2 == 0
# filter will check this condition and selects values
# from sequence where it returns True
print(even(9))
print(filter(even, k))
# typecast the filter object
print(list(filter(even, k)))
--------------------------------------------------------------------

k = [12, 45, 3, 67, 89, 90, 1, 23, 44, 68, 22]
# filter out numbers divisible by 5
print(tuple(filter(lambda num: num % 5 == 0, k)))
===================================================================

# WAP single line solution: for to fetch name end with 't'
names = ['Ajit', 'Vijay', 'sujit', 'suraj', 'shivansh', 'raj']
print(list(filter(lambda nm: nm.endswith('t'),names)))
-------------------------------------------------------------------

# WAP single line solution: for to fetch name end with 'j'
names = ['Ajit', 'Vijay', 'sujit', 'suraj', 'shivansh', 'raj']
print(list(filter(lambda nm: nm.endswith('j'),names)))
=====================================================================

3. Reduce:      (func, sequence)
     - it used to reduce the sequence into single object
     - Reduce is not directly present like map and filter
     - it is present in functools module
--------------------------------------------------------------------

so we need to import reduce
Syntax:
reduce(function, sequence)
-----------------------------------------------------------------

from functools import reduce
k = [12, 45, 3, 67, 89, 90, 1, 23, 44, 68, 22]
# addition of all numbers
print(reduce(lambda x, y: x + y, k))    # performs cumulative addition
# in case of reduce we need not to typecast
------------------------------------------------------------------

from functools import reduce
k = [12, 45, 3, 67, 89, 90, 1, 23, 44, 68, 22]
# find out the largest number
print(reduce(lambda x, y: x if x > y else y, k))
====================================================================

# Nested functions:
        function inside another function is nested function
--------------------------------------------------------------------

def outer():
    print('This is outer function')
    def inner():
        print('Inner function')
    inner()
outer()
=====================================================================

# function referencing
# using outer we are referring to inner
def outer():
    print('This is outer function')
    def inner():
        print('Inner function')
    return inner
o = outer()
print(o)
# o in an instance of inner
o()
o()
====================================================================

def central_gov():
    print('Central')

    def state_gov():
        print('State')
    return state_gov


ref = central_gov()
print(ref)
# this ref will use to access state_gov
ref()
-----------------------------------------------------------------------

def central_gov():
    print('Central')

    def state_gov():
        print('State')
    return central_gov,state_gov


ref1, ref2 = central_gov()
print(ref1, ref2)
# this ref will use to access state_gov
ref1()
ref2()
---------------------------------------------------------

def outer():
    x = 100

    def inner():
        print(x)
    inner()
outer()
===============================================================

# Function aliasing:
      - it is giving a second name or short name to existing function.
      - Aliasing happens when the value of one variable is assigned to another variable
      - because variables are just names that store references to actual value.
---------------------------------------------------------------

def prerajulization():
    print('Operations')


p = prerajulization
p()
p()
--------------------------------------------------------------------

def factorial():
    print('factors')


f = factorial
f()
f()
==========================================================
"""