x = [10, 20, 30]
i = 0

i, x[i] = 1, 40

print("i is ", i)  # 1
print("x is ", x)  # [10, 40, 30]


def getTwo():
    return (10, 20)


x, y = getTwo()
print("x is ", x)  # 10
print("y is ", y)  # 20
