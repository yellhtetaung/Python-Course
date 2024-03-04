x = 2
y = 3

print(" bin(2) ", bin(2))  # 0b10
print(" bin(3) ", bin(3))  # 0b11
print(" bin(2) & bin(3) ", 2 & 3)  # 2
print("True & False ", True & False)  # False


# print("'True' & False ", "True" & False)


def getTrue():
    print("Get True")
    return True


def getFalse():
    print("Get False")
    return False


print("getFalse() & getTrue() ", getFalse() & getTrue())  # False
print("getFalse() | getTrue() ", getFalse() | getTrue())  # True

print(" 2 ^ 3 ", 2 ^ 3)  # 1

print(bin(2), ~2)  # 0b10 -3

print(bin(2), " ", bin(2 << 1), " ", 2 << 1)  # 0b10 0b100 4
print(bin(2), " ", bin(2 << 2), " ", 2 << 2)  # 0b10 0b100 8

print(bin(2), " ", bin(8 >> 2), " ", 8 >> 2)  # 0b10 0b10 2
