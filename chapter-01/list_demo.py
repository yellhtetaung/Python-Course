ages = [10, 20, 28, 45, 18]
print("Ages ", ages)  # [10, 20, 28, 45, 18]
print("Ages[0] ", ages[0])  # 10
print("Ages[3] ", ages[3])  # 45
print("Len ", len(ages))  # 5
print("Sum ", sum(ages))  # 121
print("Average ", sum(ages) / len(ages))  # 24.2

ages.append(20)
print("Ages ", ages)  # [10, 20, 28, 45, 18, 20]
ages.remove(18)
print("Ages ", ages)  # [10, 20, 28, 45, 20]
