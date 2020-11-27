starting_value = int(input("Enter the starting value: "))
ending_value = int(input("Enter the ending value: "))
increment = int(input("What is the increment: "))

print("{:>12} {:>11}".format("List Value", "Square"))
for i in range(starting_value, ending_value, increment):
    print("{:>8} {:13}".format(i,i**2))