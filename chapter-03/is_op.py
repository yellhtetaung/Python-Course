x = 10
y = 10

print("id x ", id(x), "id y ", id(y))  # id x  4322259424 id y  4322259424
print("x is y ", x is y)  # True

a = [10, 20, 30]
b = [10, 20, 30]
c = b

print("id(a) ", id(a), "id(b) ", id(b))  # id(a)  4299267840 id(b)  4299368320
print("a is b ", a is b)  # False
print("c is b ", c is b)  # True

d = ()
e = ()

print("d is e ", d is e)  # True

str1 = "Hello"
str2 = "Hello"

print("str1 is str2 ", str1 is str2)  # True
