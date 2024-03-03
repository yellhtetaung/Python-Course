def getTrue():
    print("Get True")
    return True


def getFalse():
    print("Get False")
    return False


# And
# two time print Get True
# print("getTrue and getTrue ", getTrue() and getTrue())

# one time print Get False
# print("getFalse and getTrue ", getFalse() and getTrue())

# two time print Get False and Get False
# print("getTrue and getFalse ", getTrue() and getFalse())

# one time print Get False
# print("getFalse and getFalse ", getFalse() and getFalse())

# Or
# one time print Get True
# print("getTrue or getTrue ", getTrue() or getTrue())

# two time print Get False and Get True
# print("getFalse or getTrue ", getFalse() or getTrue())

# one time print Get True
# print("getTrue or getFalse ", getTrue() or getFalse())

# two time print Get False and Get False
# print("getFalse or getFalse ", getFalse() or getFalse())
