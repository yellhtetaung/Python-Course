lst1 = [10, 20, 50]
lst2 = [20, 30, 60]

# step 1 -> pairwise comparison
# go next element if the element are same
# if the list is shorter then smaller

print("[10, 20] > [10, 20, 30] ", [10, 20] > [10, 20, 30])  # False
print("[10, 20] > [5, 20, 30] ", [10, 20] > [5, 20, 30])  # True
print("[10, 5] < [10, 20, 30] ", [10, 5] < [10, 20, 30])  # True

print("[10, 20] >= [10, 20, 30] ", [10, 20] >= [10, 20, 30])  # False
print("[10, 20] >= [5, 20, 30] ", [10, 20] >= [5, 20, 30])  # True

tp1 = (5, 6, 7)

print("lst1 == tp1 ", lst1 == tp1)  # False
