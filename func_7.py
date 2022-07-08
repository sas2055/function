"""
# function:
       - A function is a block of code which only runs.
       - You can pass data, known as parameters.
       - A function can return data as a result.
-------------------------------------------------------------------

1. Iterators
    - iterator is an object that contains a countable number of values.
    - iterator is an object that can be iterated upon through all the values.
    - iterator is an object which implements the iterator protocol,
    - which consist of the methods __iter__() and __next__().
----------------------------------------------------------------------

# Iterator vs Iterable
       - Lists, tuples, dictionaries, and sets are all iterable objects.
       - They are iterable containers which you can get an iterator from.
------------------------------------------------------------------------

# Que. Return an iterator from a tuple, and print each value
t = ('apple', 'banana', 'cherry')
it = iter(t)
print(next(it))
print(next(it))
print(next(it))
====================================================================

# for loop to iterate through an iterable object
t = ('apple', 'banana', 'cherry')
for x in t:
  print(x)
====================================================================

# Que. Create an iterator that returns numbers, starting with 1, and each sequence will increase by one.


class my_numbers:

  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

my_class = my_numbers()
i = iter(my_class)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
=============================================================

# Que. Create an iterator that returns numbers, starting with 1, and each sequence will increase by one.


class my_numbers:

  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

my_class = my_numbers()
i = iter(my_class)
for x in i:
    print(x)
=========================================================

# Que. Class to implement an iterator of powers of two


class Pow_2:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


numbers = Pow_2(3)
i = iter(numbers)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
===================================================================

2. generator:
       - it is a simple way of creating iterators.
       - All the work are automatically handled by generators.
       - it is a function that returns an object (iterator) which we can iterate one value at a time.
----------------------------------------------------------------------------

    There are two terms involved when we discuss generators.
1. generator function:
    - It is defined like a normal function, but whenever it needs to generate a value,
    - it does so with the yield keyword rather than return.
    - If the body of a def contains yield, the function automatically becomes a generator function.
---------------------------------------------------------------------------

# yield for 1 , 2, 3


def simple_generator_fun():
    yield 1
    yield 2
    yield 3


for value in simple_generator_fun():
    print(value)
===========================================================================

2. generator object:
        - Generator functions return a generator object.
        - Generator objects are used either by calling the next method
        on the generator object or using the generator object in a for in loop
--------------------------------------------------------------------------------

# demonstrate use of generator object with next()


# A generator function
def simple_generator_fun():
    yield 1
    yield 2
    yield 3


# x is a generator object
x = simple_generator_fun()
# Iterating over the generator object using next
print(x.__next__())
print(x.__next__())
print(x.__next__())
----------------------------------------------------------------

# A simple generator for Fibonacci Numbers


def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(x. __next__())
print(x. __next__())
print(x. __next__())
print(x. __next__())
print(x. __next__())


# Iterating over the generator object using for in loop.
print('\nUsing for in loop: ')
for i in fib(10):
    print(i, end=' ')
================================================================

3. decorator:
    - The decorator a particular form of a function that takes functions
    as input and returns a new function as output.
    - This is also called meta-programming because a part of the
    program tries to modify another part of the program at compile time.
---------------------------------------------------------------------

# addition of each tuple


def decorator_list(func):
    def inner(list_of_tuples):
        return [func(val[0], val[1]) for val in list_of_tuples]
    return inner


@decorator_list
def add_together(a, b):
    return a + b


print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))
------------------------------------------------------------------

# multiplication of each tuple


def decorator_list(func):
    def inner(list_of_tuples):
        return [func(val[0], val[1]) for val in list_of_tuples]
    return inner


@decorator_list
def add_together(a, b):
    return a * b


print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))
------------------------------------------------------------------

# square of each tuple


def meta_decorator(power):
    def decorator_list(func):
        def inner(list_of_tuples):
            return [(func(val[0], val[1])) ** power for val in list_of_tuples]
        return inner
    return decorator_list


@meta_decorator(2)
def add_together(a, b):
    return a + b


print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))
======================================================================

4. closure:
    - A closure is a nested function which has access to a free variable
    from an enclosing function that has finished its execution.
-----------------------------------------------------------------------

    Three characteristics of a Python closure are:
    - it is a nested function
    - it has access to a free variable in outer scope
    - it is returned from the enclosing function
--------------------------------------------------------------------------



def outer(name):
    # this is the enclosing function
    def inner():
        # this is the enclosed function
        # the inner function accessing the outer function's variable 'name'
        print(name)
    return inner


# call the enclosing function
my_function = outer('Data_Scientist')
my_function()
--------------------------------------------------------------------------

# eval() function:
        - it is used for evaluate to the expression
        - it is used to given data is original format
--------------------------------------------------------------------------

print(12+45 / 5*4)
# take input from user
op = eval(input('Enter expression: '))
print(op)
print(type(op))
-------------------------------------------------------------

# take a list as an input from user
ls = eval(input('Enter a list'))
print(ls)
print(type(ls))
===========================================================================
"""
