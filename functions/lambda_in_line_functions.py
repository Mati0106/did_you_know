"""
That script including pro tips for creation of function including
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
"""


# Use function with any number of arguments
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


avg(1, 2)
# or
avg(1, 2, 3, 4, 5)


# function that only accept keyword arguments
def some_function(some_atribute, *, specified_atribiute):
    'Receives a message'
    pass


try:
    some_function(1024, True)
except TypeError:
    print(TypeError)
some_function(1024, specified_atribiute=True)

# custom sort function inside a lite
names = ['Aly Sady', 'Gru Bubo', 'Abi Luko']
sorted_names = sorted(names, key=lambda name: name.split()[-1].lower())

# use function with some default attributes but change other ones
from functools import partial


def other_function(a, b, c, d):
    print(a, b, c, d)


func_with_def_atr = partial(other_function, 1)
func_with_def_atr(2, 3, 4)


# 1, 2, 3, 4
# including metadata into function
def add(x: int or float, y: int) -> int:
    """
    Some aditional info
    :param x:
    :param y:
    :return:
    """
    return x + y


# try to use function with a string instead of int/float
try:
    add('str', 3)
except Exception as e:
    print(e)
# check how function works
help(add)

# dictionary that handle metadata
metadata_add = add.__annotations__

# in line function example
# in PEP8 standards it's recommended to use standard def add(x,y): return x+y
add = lambda x, y: x + y

# example of usage
add(2, 3)
add('Hello', 'word')

# list comprehension for inline function
my_list = [lambda val: n / 2 for n in range(6)]

# it happens like that because lambda function is done only for last argument but n-times,
for f in my_list:
    print(f(0))
# 2.5
# 2.5
# 2.5
# 2.5
# 2.5
# 2.5

# we can invoke that function w n=n
my_list = [lambda x, n=n: n / 2 for n in range(6)]

for f in my_list:
    print(f(0))
# 0.0
# 0.5
# 1.0
# 1.5
# 2.0
# 2.5


# instead of creating simple class we can create a function
import pandas as pd
def create_table(data):
    pd_data = pd.DataFrame(data)
    print(pd_data)
    def my_mean(**kwargs):
        print(pd_data.mean())
    return my_mean

my_table = create_table([1,2,3,4])
my_table(some_arg = 'some')
