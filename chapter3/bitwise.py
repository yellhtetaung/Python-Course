x = 2
y = 3

print(" bin(2) ", bin(2))  # 0b10
print(" bin(3) ", bin(3))  # 0b11
print(" bin(2) & bin(3) ", 2 & 3)  # 2
print("True & False ", True & False)  # False


# print("'True' & False ", 'True' & False)

def get_true():
    print("Get True")
    return True


def get_false():
    print("Get False")
    return False


print("get_false() & get_true() ", get_false() & get_true())  # False
print("get_false() | get_true() ", get_false() | get_true())  # True
