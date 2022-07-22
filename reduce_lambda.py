"""
# Que.1 SLP to find out sum of total element of list
from functools import reduce
ls = [12, 22, 30, 24, 15]
print(reduce(lambda x, y: x + y , ls))
====================================================

# Que.2 SLP to find out multiply of total element of list
from functools import reduce
ls = [12, 22, 3, 2, 15]
print(reduce(lambda x, y: x * y , ls))
=====================================================

# Que.3 SLP to find out greater number of given list
from functools import reduce
ls = [12, 22, 30, 24, 15, 11, 90]
print(reduce(lambda x, y: x if x > y else y, ls))
======================================================

# Que.4 SLP to find out smaller number of given list
from functools import reduce
ls = [12, 22, 30, 24, 15, 11, 90]
print(reduce(lambda x, y: x if x < y else y, ls))
=====================================================
"""
