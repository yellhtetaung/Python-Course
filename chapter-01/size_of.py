import sys

x = 10
print("get size of number ", sys.getsizeof(x))  # 28

x = 10.2
print("get size of number ", sys.getsizeof(x))  # 24

c = 10
print("get reference count ", sys.getrefcount(c))
