"""
# Anonymous function / Nameless function / lambda function:
Syntax:
    lambda parameter/s:expression
-------------------------------------------------------
    - It is a function without name
    - used for performing one time operation
    - One time operation/use means we can supply only one Expression
    - Multiple expressions are not allowed
=========================================================

s = lambda x: x + 100
print(s(50))
# Lambda function has implicit return statement
# Normal function
def add(x):
    return x + 100
print('addition is: ', add(50))
===========================================================

#-------------------- normal function---------------------
def square(n):
    return n*n
print(square(4))
#------------------ lambda function-----------------------
sq = lambda n: n*n
print(sq(10))
===========================================================

#-------------------- normal function-------------------
def convert(s):
    return s.split(),s.upper()
    # return list of string
out = convert('Hello all batch 19')
print(out)
#------------------lambda function-----------------------
con = lambda s:s.split()
print(con('This is mentos life'))
# only single expression or operation we can perform

con = lambda s:s.split(),s.upper()
print(con('This is mentos life'))
# but more than 1 is not allowed in lambda
==========================================================

# positional arguments
info = lambda nm, age:nm + age
print(info('34', 'Pranay'))
--------------------------------------------------

# keyword arguments
info = lambda nm, age:nm + age
print(info(age = '34', nm = 'Pranay'))
--------------------------------------------------------------

add = lambda a, b, c:a+b+c
print(add(10, 1, 30, 40))
# TypeError: <lambda>() takes 3 positional arguments but 4 were given
===============================================================

# normal function:
    - in normal function return is optional
    - in  normal function we can return multiple values
-----------------------------------------------------------

def sample(name, branch = 'SBI'):
    return name, branch
print(sample('shiv'))
===============================================================

# lambda function:
    - in lambda function return is implicit/by default
    - in lambda function only single expression we can return
-----------------------------------------------------------------

sample = lambda name, branch = 'BOI':name +' '+ branch
# lambda with default argument
print(sample('prathmesh'))
print(sample('Akshara', 'IDBI'))
==============================================================

def add():
    pass
sub = lambda x:x+10

print(add)
print(sub)
# check the output
# lambda is used form short term purpose
basically used for writing a concise,simple, one linear, compact expression
=======================================================================

# WAP function to find out even odd number
def check(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
print(check(1))
--------------------------------------------------------

# to implement this logic we need ternary operator
check = lambda num: 'Even' if num %2 == 0 else 'Odd'
print('Lambda:', check(8))
--------------------------------------------------------

# WAP function to find out largest amongst 2 numbers
# return_of_if if_condition else else_return
grt = lambda x, y:'X is greater' if x>y else 'Y is greater'
print(grt(10, 30))
print(grt(1, 0))
===========================================================

# higher order function:
     - In high order function, a function can act as an instant of an object type.
     - In high order function, we can return a function as a result of another function.
     - In high order function, we can pass a function as a parameter or argument inside another function.

# Actually this lambda function is used in higher order function
as an input
-----------------------------------------------------------------

# three types of higher order functions:
 1. map
 2. filter
 3. reduce
----------------------------------------------------------------

1. map:  (func, iterable)
    the function inside a map will be applied on each element from iterable
----------------------------------------------------------------

ls = list(range(10, 21))
print(ls)
# make a square of each element
print(map(lambda num:num*num, ls))
# when we got the output in the form of object
# then to see actual values typecast the object
print(list(map(lambda num:num*num, ls)))
# this lambda function will be applied on each element of ls
--------------------------------------------------------------

nms = ['vidya', 'shiljit', 'akshara', 'raj', 'yogita', 'arti']
# name should be in reverse order
for i in nms:
    print(i[::-1], end=' ')
-----------------------------------------------------------------

nms = ['vidya', 'shiljit', 'akshara', 'raj', 'yogita', 'arti']
reverse = lambda name:name[::-1]
print(list(map(reverse, nms)))
----------------------------------------------------------------

# single line solution required
nms = ['vidya', 'shiljit', 'akshara', 'raj', 'yogita', 'arti']
print(list(map(lambda name:name[::-1], nms)))
-----------------------------------------------------------------

nms = ['vidya', 'shiljit', 'akshara', 'raj', 'yogita', 'arti']
def rev(nm):
    print(type(nm))
-----------------------------------------------------------------

nms = ['vidya', 'shiljit', 'akshara', 'raj', 'yogita', 'arti']
def rev(nm):
    for i in nm:
        print(i[::-1], end=' ')


rev(nms)
------------------------------------------------------------------

nms = ['vidya', 'shiljit', 'akshara', 'raj', 'yogita', 'arti']
def rev(nm):
    for i in nm:
        print(i[::-1], end=' ')

rev(nms)
print()
print(list(map(lambda name:name[::-1], nms)))
==================================================================

nms = ['vidya', 'shiljit', 'akshara', 'raj', 'yogita', 'arti']
print('----------------normal function---------------')

def rev(nm):
    print(nms)
    l = []
    for i in nm:
        l.append(i[::-1])
    print(l, end=' ')


rev(nms)
print('\n--------------------lambda function----------------------')
print(nms)
rev = map(lambda name:name[::-1], nms)
print(list(rev))
===================================================================
"""
