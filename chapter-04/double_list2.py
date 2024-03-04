my_list = [10, 20, 30, 40]

for i in my_list:
    print("I is ", i)
    i *= 2

for index, value in enumerate(my_list):
    print("Index ", index, "Value ", value)
    my_list[index] *= 2

print("My List ", my_list)  # [20, 40, 60, 80]
