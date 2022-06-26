"""
4. variable length argument:
        it is defined as arguments that can also accept an unlimited amount of data as input.
-----------------------------------------------------------------------------

# there are two types of follows
1. variable length positional arguments:   (*args)
        when we supply variable length positional arguments then it returns tuple always.
----------------------------------------------------------

syntax:
    def function(parameters):
        ...
            ..
            ..
        return
# Parameters and return are optional
=========================================================

# Que. WAP to do the addition of variable numbers
def add(a,b):
    print(a+b)


add(10,20)
add()
add(1,2,3)
add(10,20,30,40)
--------------------------------------------------
# We cant pass multiple values in above case as declaration only
contains 2 parameters (a,b)
So above issue we can solve using variable length arguments.
=====================================================================

# Que. WAP to do the addition of variable numbers
def add(*args):         # instead of args we can use any other valid identifier
    print(args)


add(10,20)
add()
add(1,2,3)
add(10,20,30,40)
-------------------------------------------------------------
# when we supply variable length Positional arguments
# then it returns Tuple always
============================================================

# Que. supply following inputs to a function func
and get the addition of elements
func(10,20)
func(1,2,3,-5)
func()
func(1,2,3,4,5,6)

def func(*n):
    print(sum(n))


func(10,20)
func(1,2,3,-5)
func()
func(1,2,3,4,5,6)
========================================================

# Que. WAP to fetch only characters from function calling
def func(*n):
    for i in n:
        if str(i).isalpha():
            print(i, end=' ')


func('X',10,'A')
func(1,'V',3,'N')

or
def func(*n):
    for i in n:
        if str(i).isalpha():
            print(i, end=' ')
    print()


func('X',10,'A')
func(1,'V',3,'N')
================================================================

2. Variable length keyword arguments:
        (**kwargs) = key-value pair
    when we supply variable length keyword arguments then it returns dict always.
------------------------------------------------------------------------

def func(**kwargs):
    print(kwargs)


func()
func(name = 'Python', age = 23)
func(roll_no = 12, name = 'Ajit', marks = 80)
# kwargs gives a dict always
func(a = 10, b = 20, c = 30)
------------------------------------------------------------------

# Que. fetch only values in function calling
def func(**kwargs):
    print(kwargs.values())
func()
func(name = 'Python', age = 23)
func(roll_no = 12, name = 'Ajit', marks = 80)
func(a = 10, b = 20, c = 30)
---------------------------------------------------------------------

# Que. fetch only keys in function calling
def func(**kwargs):
    print(kwargs.key())


func()
func(name = 'Python', age = 23)
func(roll_no = 12, name = 'Ajit', marks = 80)
func(a = 10, b = 20, c = 30)
----------------------------------------------------------------------

# Que. fetch items in function calling
def func(**kwargs):
    print(kwargs.items())


func()
func(name = 'Python', age = 23)
func(roll_no = 12, name = 'Ajit', marks = 80)
func(a = 10, b = 20, c = 30)
=====================================================================

Return statement:
        return is a keyword
-------------------------------------------------------------

# a function without return
def add():
    print(100+200)


result = add()
print(result)

# When ur function does nt return anything
# then it returns ==> None means nothing
----------------------------------------------------------------

def add():
    #print(100+200)
    return 100 + 200


result = add()
print(result)
-----------------------------------------------------------------

def kharacha(paise):
    paise -= 500        # purchased 500 rs T-shirt
    return paise
rem = kharacha(1000)
print(rem)
======================================================================

# Que. How many values we can return
->  n number of value return.
==========================================================

def sample(a,b):
    return a, b, a+b
    # return brings the value outside
    # only single return is allowed
print(sample(20,40))        # packing is performed here
x,y,z = sample(1,2)         # unpacking
p = sample(1,2)
print(p)
print(x,y,z , end = '  ')
---------------------------------------------------------------

# this function using typecasting
def sample(a,b):
    return a, b, a+b


print(list(sample(20,40)))        # typecast of list
p = sample(1,2)
print(set(p))                   # typecast of set
----------------------------------------------------------------

# this function using indexing
def sample(a,b):
    return a, b, a+b


print(sample(20,40)[1])
x,y,z = sample(1,2)
p = sample(1,2)
print(p[2])
----------------------------------------------------------------

# slicing then using reverse
def sample(a, b):
    return a, b, a+b


print(sample(10, 20)[::-1])
x, y, z = sample(1, 2)
p = sample(1, 2)
print(p[::-1])
-------------------------------------------------------------

def test(fever):
    if fever > 96:
        return 'positive'
    else:
        return 'negative'
result = test(70)
if result == 'positive':
    print('14 days isolation')
else:
    print('Take medicine and rest + Home isolation')
===================================================================
"""
