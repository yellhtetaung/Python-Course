my_str = '123'
my_num = 10

print("my_str + my_num ", int(my_str) + my_num)
print("int(' 1000 ')", int(' 1000 '))
# print("int('10.1')", int('10.1'))  # error
# print("int('0x10')", int('0x10'))  # error
print("int(True)", int(True))
print("int(False)", int(False))
print("int()", int())  # 0

print("float(' 1000 ')", float(' 1000 '))
print("float('10.1')", float('10.1'))
# print("float('0x10')", float('0x10'))  # error
print("float(True)", float(True))
print("float(False)", float(False))
print("float()", float())  # 0
