def get_true():
    print("Get True")
    return True


def get_false():
    print("Get False")
    return False


# print("get_true and get_true", get_true() and get_true())
# print("get_false and get_true", get_false() and get_true())

# print("get_true or get_true", get_true() or get_true())
print("get_false or get_true", get_false() or get_true())
