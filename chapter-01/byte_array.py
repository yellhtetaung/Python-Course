x = [0, 10, 25, 200]
my_bytes = bytearray(x)
print("my_bytes ", my_bytes)  # bytearray(b'\x00\n\x19\xc8')
print("my_bytes type ", type(my_bytes))  # <class 'bytes'>
print("my_bytes slice ", my_bytes[1])

my_bytes[0] = 100  # bytearray(b'd\n\x19\xc8')
print("my_bytes ", my_bytes)
print("my_bytes[0] ", my_bytes[0])  # 100
