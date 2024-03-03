print("True and True ", True and True)  # True
print("True and False ", True and False)  # False

print("False and False ", False and False)  # False
print("False and True ", False and True)  # False

# Left Truthy
print("'Hello' and 1 ", "Hello" and 1)  # 1
print("'Hello' and 300 ", "Hello" and 300)  # 300

# Left Falsy
print(" '' and 'Hello' ", "" and "Hello")  # ''
print(" 0 and 'Hello' ", 0 and "Hello")  # 0
print(" [] and 'Hello' ", [] and "Hello")  # []
print(" () and 'Hello' ", () and "Hello")  # ()
print(" False and 'Hello' ", False and "Hello")  # False
