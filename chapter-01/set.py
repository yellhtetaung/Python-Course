my_set = {3, 1, 2, 10, 11, 1}
print("my_set ", my_set)  # {1, 2, 3, 10, 11}

my_set = set([3, 1, 2, 10, 11, 1])
print("my_set ", my_set)  # {1, 2, 3, 10, 11}

my_set.add(100)
print("my_set ", my_set)  # {1, 2, 3, 100, 10, 11}

my_set.remove(11)
print("my_set ", my_set)  # {1, 2, 3, 100, 10}
