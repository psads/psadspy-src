#!/usr/bin/env python3
"""Snippets of code"""

def sum_of_n(n):
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    return the_sum


print(sum_of_n(10))


def foo(tom):
    fred = 0
    for bill in range(1, tom + 1):
        barney = bill
        fred = fred + barney

    return fred


print(foo(10))


import time


def sum_of_n_2(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    end = time.time()

    return the_sum, end - start


for i in range(5):
    print("Sum is %d required %10.7f seconds" % sum_of_n_2(1000000))


def sum_of_n_3(n):
    return (n * (n + 1)) / 2


print(sum_of_n_3(10))

n = 10
a = 5
b = 6
c = 10
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j
for k in range(n):
    w = a * k + 45
    v = b * b
d = 33
