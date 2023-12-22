ages = [10, 20, 28, 45, 18]

print("Ages ", ages)
print("Ages[0] ", ages[0])
print("Ages[3] ", ages[3])
print("Sum ", sum(ages))
print("Average ", sum(ages) / len(ages))

ages.append(20)
print("Ages ", ages)
ages.remove(28)
print("Ages ", ages)
