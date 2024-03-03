print("True or True ", True or True)  # True
print("True or False ", True or False)  # True

print("False or False ", False or False)  # False
print("False or True ", False or True)  # True

# Left Truthy
print("'hello' or 0 ", "hello" or 0)  # hello
print("1 or 0 ", 1 or 0)  # 1
print("[1, 20] or 0 ", [1, 20] or 0)  # [1, 20]

# Left Falsy
print("False or 'Hello' ", False or "Hello")  # Hello
print("'' or 'Hello' ", "" or "Hello")  # Hello
print("'' or 1000 ", "" or 1000)  # 1000
print("[] or 1000 ", [] or 1000)  # 1000
