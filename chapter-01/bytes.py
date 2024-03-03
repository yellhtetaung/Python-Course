x = [0, 10, 25, 200]
my_bytes = bytes(x)
print("my_bytes ", my_bytes)  # b'\x00\n\x19\x1e'
print("my_bytes type ", type(my_bytes))  # <class 'bytes'>
print("my_bytes slice ", my_bytes[1])

# my_bytes[0] = 100

my_str = "Hello"
# my_str[0] = "A"
