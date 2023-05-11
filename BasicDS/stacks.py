#!/usr/bin/env python3
"""Anagram Detection Example"""
from pythonds3.basic import Stack


def rev_string(my_str):
    s = Stack()
    for c in my_str:
        s.push(c)
    result = []
    while not s.is_empty():
        result.append(s.pop())

    return "".join(result)


assert rev_string("apple") == "elppa"
assert rev_string("x") == "x"
assert rev_string("1234567890") == "0987654321"


def par_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()

    return s.is_empty()


assert par_checker("((()))") == True
assert par_checker("((()()))") == True
assert par_checker("(()") == False
assert par_checker(")(") == False


def balance_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), symbol):
                    return False

    return s.is_empty()


def matches(sym_left, sym_right):
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)


assert balance_checker("{({([][])}())}") == True
assert balance_checker("[{()]") == False


def divide_by_2(decimal_num):
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % 2
        rem_stack.push(rem)
        decimal_num = decimal_num // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


assert divide_by_2(42) == "101010"
assert divide_by_2(31) == "11111"


def base_converter(decimal_num, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num = decimal_num // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string


assert base_converter(25, 2) == "11001"
assert base_converter(25, 16) == "19"


def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (
                prec[op_stack.peek()] >= prec[token]
            ):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)


assert infix_to_postfix("A * B + C * D") == "A B * C D * +"
assert (
    infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )")
    == "A B + C * D E - F G + * -"
)
assert infix_to_postfix("( A + B ) * ( C + D )") == "A B + C D + *"
assert infix_to_postfix("( A + B ) * C") == "A B + C *"
assert infix_to_postfix("A + B * C") == "A B C * +"


def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


assert postfix_eval("7 8 + 3 2 + /") == 3

