my_str = "123"
my_num = 10

print("my_str + my_num", int(my_str) + my_num)  # 133
print("int(' 1000 ')", int(" 1000 "))  # 1000
# print("int(' 10.1 ')", int(' 10.1 ')) # invalid literal
# print("int('0x10')", int('0x10')) # invalid literal
print("int(True)", int(True))  # 1
print("int(False)", int(False))  # 0
print("int()", int())  # 0

print("float(' 1000 ')", float(" 1000 "))  # 1000.0
print("float(' 10.1 ')", float(" 10.1 "))  # 10.1
# print("int('0x10')", float('0x10'))  # invalid literal
print("float(True)", float(True))  # 1.0
print("float(False)", float(False))  # 0.0
print("float()", float())  # 0.0
