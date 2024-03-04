number_of_subject = int(input("Enter number of subject "))

pass_mark = 40
is_pass = True

for i in range(number_of_subject):
    mark = float(input("Enter mark for subject " + str(i) + " "))
    is_pass = is_pass and mark >= 40

if is_pass:
    print("Pass the exam")
else:
    print("Fail the exam")
