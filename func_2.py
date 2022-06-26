"""
# parameter:
    A parameter is the variable listed inside the parentheses in the function definition.
------------------------------------------------------------------------

# arguments:
    An argument is the value that are sent to the function.
-------------------------------------------------------------------

# Types of arguments:
        there are 4 types of arguments.

1. Positional argument:
        - sequence/order of values matter.
        - it is not followed by an equal sign (=) and default value.

Example:
def info(name, age):
    print('your name is: ', name)
    print('Your age is: ', age)
info('Shital', 27)
info(27, 'Ajit')
# bcz its positional hence
# 27 will be given to name and Ajit will be age
==========================================================

2. Keyword arguments:
        - sequence/order of values does not matter.
        - it is followed by an equal sign and an expression that gives its default value.

Example:
def info(name,age):
    print('your name is: ', name)
    print('Your age is: ', age)
info('Shital', 27)
info(age = 27, name = 'Ajit')

# keyword map values to its exact parameter
# so, order does not matters in this case
------------------------------------------------------------

def display(roll_no, name, per,):
    print('Roll number: ',roll_no, 'name: ', name, 'percentage: ', per)
display(name = 'shivansh', roll_no = 3, per = 88)
display(name = 'shital', roll_no = 11, 96)

# Rule: positional argument should not follow keyword argument
-----------------------------------------------------------

# we can specify/give a positional argument
# ONLY before Keyword argument

def display(roll_no,name,per,):
    print('Roll number: ', roll_no, 'name: ', name, 'percentage: ', per)

# display(22, per = 88, name = 'komal')
# this is allowed because positional argument
# follow keyword argument
display(name = 'nityansh', roll_no = 12, name = 99)
-------------------------------------------------------------

def sample(a,b,c):
    pass
sample(a = 10, b = 10, c = 10)
------------------------------------------------------

def sample(a,b,c):
    print(a,b,c)
sample('10', '20', '30')
# if i expect first 2 int, last float
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = float(input('Enter c: '))
sample(a,b,c)
==========================================================

3. Default arguments:
       - Default argument we can supply in declaration only
       - We can provide a default value to an argument by using the assignment operator (=).
-----------------------------------------------------------------------

def bank(name, branch, IFSC = 'SBI7700'):       # here IFSC is a default argument.
    print(name, branch, IFSC)
bank('Shital', 'Karad')
bank('Ajit', 'Kothrud', 'BOI87234')
bank('Sujit', 'Masur', 'BOM783645')
-----------------------------------------------------------

def operating_sys(name, account = 'Guest'):
    print('Hello', name, 'welcome to',  account, 'account')
operating_sys('Akshara')
operating_sys('Sanika', 'Star')
============================================================
"""
