x = 1500
y = 1500
print("x is y ", x is y)


def hello():
    k = 1500
    print("id of k ", id(k))


hello()  # 4333236688
print("Id of x ", id(x))  # 4333236688
print("Id of y ", id(y))  # 4333236688
