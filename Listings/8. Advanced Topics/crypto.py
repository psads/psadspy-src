#!/usr/bin/env python
"""RSA implementation"""

# def encrypt(msg):
#     s = "abcdefghijklmnopqrstuvwxyz"
#     n = ""
#     for i in msg:
#         j = (s.find(i) + 13) % 26
#         n = n + s[j]
#     return n


# def decrypt(msg, k):
#     s = "abcdefghijklmnopqrstuvwxyz"
#     n = ""
#     for i in msg:
#         j = (s.find(i) + 26 - k) % 26
#         n = n + s[j]
#     return n


# print(encrypt("helloworld"))
# print(decrypt("uryybjbeyq", 13))


def modexp(x, n, p):
    if n == 0:
        return 1
    t = (x * x) % p
    tmp = modexp(t, n // 2, p)
    if n % 2 != 0:
        tmp = (tmp * x) % p
    return tmp


def gcd1(a, b):
    if b == 0:
        return a
    elif a < b:
        return gcd(b, a)
    return gcd(a - b, b)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def ext_gcd(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        (d, a, b) = ext_gcd(y, x % y)
        return (d, b, a - (x // y) * b)


import random


def str_to_chunks(msg, chunk_size):
    msg_bytes = bytes(msg, "utf-8")
    hex_str = "".join([f"{b:02x}" for b in msg_bytes])
    num_chunks = len(hex_str) // chunk_size
    chunk_list = []
    for i in range(
        0, num_chunks * chunk_size + 1, chunk_size
    ):
        chunk_list.append(hex_str[i : i + chunk_size])
    chunk_list = [
        eval("0x" + x) for x in chunk_list if x
    ]
    return chunk_list


def chunks_to_str(chunk_list, chunk_size):
    hex_list = []
    for chunk in chunk_list:
        hex_str = hex(chunk)[2:]
        clen = len(hex_str)
        hex_list.append(
            "0" * ((chunk_size - clen) % 2) + hex_str
        )

    hstring = "".join(hex_list)
    msg_array = bytearray.fromhex(hstring)
    return msg_array.decode("utf-8")


def gen_keys(p, q):
    n = p * q
    m = (p - 1) * (q - 1)
    e = int(random.random() * n)
    while gcd(m, e) != 1:
        e = int(random.random() * n)
    d, a, b = ext_gcd(m, e)
    if b < 0:
        d = m + b
    else:
        d = b
    return (e, d, n)


def encrypt(msg, e, n):
    chunk_size = n.bit_length() // 8
    all_chunks = str_to_chunks(msg, chunk_size)
    return [
        modexp(msg_chunk, e, n)
        for msg_chunk in all_chunks
    ]


def decrypt(cipher_chunks, d, n):
    chunk_size = n.bit_length() // 8
    plain_chunks = [
        modexp(cipher_chunk, d, n)
        for cipher_chunk in cipher_chunks
    ]
    return chunks_to_str(plain_chunks, chunk_size)


msg = "Python"
e, d, n = gen_keys(5563, 8191)
# print(e, d, n)  # 2646697 33043453 45566533
c = encrypt(msg, e, n)
# print(c)  # [22810070, 18852325, 34390906, 22805081]
m = decrypt(c, d, n)
# print(m)  # [1287, 2420, 1670, 3950]
assert m == msg
