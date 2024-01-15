#!/usr/bin/env python3
"""Snippets of code"""


def prime_factors(n: int):
    """Generate prime factors of a number"""
    if n < 1:
        raise ValueError(f"Number must be greater than 1")
    if n == 1:
        return
    i = 2
    while n % i:
        i = i + 1
    yield i
    yield from prime_factors(n / i)


# n = 12345333478658347653
# n = 111111111111111
# for f in prime_factors(n):
#     print(f, end=" ")
# print()


def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]


# print(to_str(1453, 16))


from pythonds3.basic import Stack


def to_str(n, base):
    r_stack = Stack()
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base
    res = ""
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())
    return res


# print(to_str(1453, 16))

import turtle


# def draw_spiral(my_turtle, line_len):
#     if line_len > 0:
#         my_turtle.forward(line_len)
#         my_turtle.right(90)
#         draw_spiral(my_turtle, line_len - 5)


# my_turtle = turtle.Turtle()
# my_win = turtle.Screen()
# draw_spiral(my_turtle, 100)
# my_win.getcanvas().postscript(file=f"spiral.ps")
# my_win.exitonclick()

i = 0


def tree(branch_len, t, w=None):
    global i
    i = i + 1
    if i == 7:  # book
        # if i == 5:  # site
        w.getcanvas().postscript(file=f"tree1.ps")
    # if i == 2 ** 7:  # book
    if i == 2 ** 5:  # site
        w.getcanvas().postscript(file=f"tree2.ps")
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t, w)
        t.left(40)
        tree(branch_len - 15, t, w)
        t.right(20)
        t.backward(branch_len)


def draw_tree():
    # turtle.setup(600, 600)  # book
    turtle.setup(300, 300)  # site
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.ht()
    t.left(90)
    t.up()
    # t.backward(200)  # book
    t.backward(100)  # site
    t.down()
    # t.color("black")  # book
    t.color("green")  # site
    # tree(110, t, my_win)  # book
    tree(75, t, my_win)  # site
    my_win.exitonclick()


# draw_tree()


from time import process_time
from functools import lru_cache


@lru_cache(None)
def make_change_1(coin_value_list, change):
    min_coins = change
    if change in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + make_change_1(coin_value_list, change - i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


print("Counting change 1")
start = process_time()
result = make_change_1((1, 5, 10, 25), 63)
end = process_time()
print(f"result: {result}; calculated in {end - start:2.5g} sec")


def make_change_2(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + make_change_2(
                coin_value_list, change - i, known_results,
            )
            if num_coins < min_coins:
                min_coins = num_coins
            known_results[change] = min_coins
    return min_coins


print("Counting change 2")
start = process_time()
result = make_change_2([1, 5, 10, 25], 63, [0] * 64)
end = process_time()
print(f"result: {result}; calculated in {end - start:2.5g} sec")


def make_change_3(coin_value_list, change, min_coins):
    for cents in range(change + 1):
        coin_count = cents
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
        min_coins[cents] = coin_count
    return min_coins[change]


print("Counting change 3")
start = process_time()
result = make_change_3([1, 5, 10, 25], 63, [0] * 64)
end = process_time()
print(f"result: {result}; calculated in {end - start:2.5g} sec")


def make_change_4(coin_value_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin, end=" ")
        coin = coin - this_coin
    print()


def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coins_used = [0] * (amnt + 1)
    coin_count = [0] * (amnt + 1)

    print("Making change for {}".format(amnt), end=" ")
    print(
        "requires the following {} coins: ".format(
            make_change_4(clist, amnt, coin_count, coins_used),
        ),
        end="",
    )
    print_coins(coins_used, amnt)
    print("The used list is as follows:")
    print(coins_used)


main()
