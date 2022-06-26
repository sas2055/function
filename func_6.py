"""
# Types of Variable:
        there are three types of variables
        1. Global variable
        2. Local variable
        3. Nonlocal variable
-------------------------------------------------------------------------
1. Global Variable:
        The variable which is available anywhere throughout the program,
and we declare this variable outside the function at the same indent level.
---------------------------------------------------------------------------

x = 200
def test():
    # access x inside a function
    print('Inside: ', x)

# access x outside a function
print('Outside: ', x)
test()
======================================================================

2. Local Variable:
       - the variable which is declared inside a function called as Local variable.
       - This variable will not be accessible outside the function
       - Local variable is having a restricted scope means it will be accessible only to
        that function or within the function
       - it is outside we can not access.
-------------------------------------------------------------------------

def test():
    # local var. to test
    x = 'python inside'
    print(x)
test()
print(x)  # want be accessible
-----------------------------------------------------------

# local x directly not available
# but we want to access it outside
# solution 1 is to use: return
def test():
    # local var. to test
    x = 'python inside'
    print(x)
    return x
x = test()
print(x)
-----------------------------------------------------------

# Solution 2 is to use: global keyword
y = 70
def test():
    # local var. now set as a global
    global x
    x = 'python inside'
    print(x, y)
test()
print(x, y)
---------------------------------------------------------

x = 100     #global
def test():
    print(x)
test()
---------------------------------------------------------

x = 100     #global
def test():
    global x
    x = x + 200
    print(x)
    x = 80
    x = x + 50
    print(x)
test()
-----------------------------------------------------------

x = 100     #global
def test():
    # lets try to modify x
    global x
    x += 2
    print(x)
test()
----------------------------------------------------------

x = 100     #global
def test():
    # lets try to modify x
    global x
    x = 80
    x += 2
    print(x)
test()
----------------------------------------------------------

cm = 'Udhhav Thackrey'
def politics():
    print(cm)
politics()
----------------------------------------------------------



def outer():
    # local to outer
    x = 200

    def inner():

        global x
        x = 400
        print('Inner: ', x)
    inner()
    print('Outer: ', x)


outer()
print(x)
-------------------------------------------------------

# temporary change
cm = 'Udhhav Thackrey'
def politics():
    print(cm.replace('Udhhav Thackrey','Devendra Fadanvis'))
politics()
-----------------------------------------------------------

# permanent change
cm = 'Udhhav Thackrey'
def politics():
    # in local scope changing the cm is not possible
    global cm
    cm = cm.replace('Udhhav Thackrey', 'Devendra Fadanvis')
    print(cm)
politics()
------------------------------------------------------------

cm = 'Udhhav Thackrey'
def politics():
    # in local scope changing the cm is not possible
    global cm
    cm = cm.replace('Udhhav Thackrey','Devendra Fadanvis')
    print(cm)
politics()
print(cm)
=====================================================================

Nonlocal variable:
        - it is related to nested function
        - inner local are presented by outer local then use nonlocal
        - outside not use nonlocal
---------------------------------------------------------------


def outer():
    # local to outer
    x = 200
    def inner():

        x = 400
        print('Inner: ', x)
    inner()
    print('Outer: ', x)
outer()
print()
------------------------------------------------------



def outer():
    # local to outer
    x = 200

    def inner():

        nonlocal x
        x = 400
        print('Inner: ', x)
    inner()
    print('Outer: ', x)


outer()
print()
---------------------------------------------------


def sample_1():
    val1 = 'local_1'

    def sample_2():

        val1 = 'local_2'
        print('Sample2: ', val1)
    sample_2()
    print('Sample1: ', val1)


sample_1()
----------------------------------------------------------


def sample_1():
    val1 = 'local_1'

    def sample_2():
        nonlocal val1
        val1 = 'local_2'
        print('Sample2: ', val1)

        def test():
            print(val1)
        test()

    def sample_3():
        print('Sample3: ', val1)

    sample_2()
    sample_3()
    print('Sample1: ', val1)


sample_1()
----------------------------------------------------


def sample_1():
    val1 = 'local_1'

    def sample_2():
        nonlocal val1
        val1 = 'local_2'
        print('Sample2: ', val1)

        def test():
            print(val1)
        test()

    def sample_3():
        print('Sample3: ', val1)

    sample_3()
    sample_2()
    print('Sample1: ', val1)


sample_1()
=====================================================
"""
