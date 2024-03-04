print("True == 1 ", True == 1)  # True
print("False == 0 ", False == 0)  # True

print("'True' == 0 ", "True" == 0)  # False

lst1 = [1, 2, 3]
lst2 = ["1", 2, 3]

tp1 = (1, 2, 3)
tp2 = (1, 2, 3)

print("lst1 == lst2 ", lst1 == lst2)  # False
print("lst1 == tp1 ", lst1 == tp1)  # False
print("tp1 == tp2 ", tp1 == tp2)  # True

set1 = {1, 2, 3}
set2 = {1, 2, 3}

print("set1 == set2 ", set1 == set2)  # True
