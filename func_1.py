"""
# function:
        a function is block of code which only runs and returns data as a result.
use a strategy: write once and use multiple times
    advantage: code Re-usability
syntax:
    def function_name():
        statement
        ........
-----------------------------------------------------

in function we have to follow two process:
1. declaring the function
    def simple():
        print('hello')

2. calling the function
    simple()
===========================================================

# in python we have two types of function:
1. built-in function:
        present in python default,
    such as print(), id(), type(), bin(), list(), tuple(), range()
---------------------------------------------------------------

2. user defined function:
        will be created by user as per requirement

# declaration
def simple():
    print('data_scientist')
# calling to get output then calling is important
simple()
for i in range(5):
    simple()
==============================================================

# syntax:
        def function_name(parameters):
            .....
            .....
function_name(parameters)
        If in declaration we have parameters then
    we must need to supply values to it.
---------------------------------------------------------

# a, b are positional arguments
def sum(a,b):
    print(a+b)
sum(20,40)
sum(100,200)
sum(-10,-40)
sum(1) # this will raise exception bcz b value is not given
sum() # this will give error bcz a,b values but given
-------------------------------------------------------------

# a, b are positional arguments
def sum(a,b):
    print(a+b)
sum(20,40,50,60)
# raise TypeError: sum() takes 2 positional arguments but 4 were given
--------------------------------------------------------------

# a, b are positional arguments
def sum(a,b,c,d):
    print(a+b+c+d)
sum(10,20)
# raise TypeError: sum() takes 2 positional arguments but 4 were given
# Rule: if u have 4 parameters in declaration
# u must have to pass 4 values/arguments at the time of calling
==============================================================================
"""