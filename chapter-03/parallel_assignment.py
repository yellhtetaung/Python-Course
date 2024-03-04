x = 1
y = 2

temp = x
x = y
y = temp

print("x is ", x)  # 2
print("y is ", y)  # 1

x, y = y, x

print("x is ", x)  # 1
print("y is ", y)  # 2
