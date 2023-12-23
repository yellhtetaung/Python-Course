def getTrue():
    print("Get True")
    return True


def getFalse():
    print("Get False")
    return False


# print("getTrue and getTrue", getTrue() and getTrue())
# print("getFalse and getTrue", getFalse() and getTrue())

# print("getTrue or getTrue", getTrue() or getTrue())
print("getFalse or getTrue", getFalse() or getTrue())
