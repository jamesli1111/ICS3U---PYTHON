input_list = []
number_of_numbers = int(input(f"How many numbers would you like to enter?: "))
for i in range (number_of_numbers):
    number = input(f"enter your number: ")
    input_list.append(number)
input_list.sort()
sum = 0
print(input_list)
for i in range (int(len(input_list))):
    sum += int(input_list[i])
print (f"The sum of the numbers you entered is {sum}")