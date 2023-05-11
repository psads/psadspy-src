print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 10)
print(6 / 3)
print(7 / 3)
print(7 // 3)
print(7 % 3)
print(3 / 6)
print(3 // 6)
print(3 % 6)
print(2 ** 100)

my_list = [1, 2, 3, 4]
big_list = [my_list] * 3
print(big_list)
my_list[2] = 45
print(big_list)

capitals = {"Iowa": "Des Moines", "Wisconsin": "Madison"}
print(capitals["Iowa"])
capitals["Utah"] = "Salt Lake City"
capitals["California"] = "Sacramento"
print(capitals)
print(len(capitals))
for k in capitals:
    print(capitals[k], "is the capital of", k)
