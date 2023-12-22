x = [0, 10, 25, 30]
my_bytes = bytearray(x)

print("my_bytes", my_bytes)  # b'\x00\n\x19\x1e'
print("type my_bytes", type(my_bytes))  # <class 'bytes'>
print("my_bytes[1]", my_bytes[1])  # 10

my_bytes[0] = 100
print("my_bytes", my_bytes)  # b'\x00\n\x19\x1e'
print("my_bytes", my_bytes[0])  # b'\x00\n\x19\x1e'
