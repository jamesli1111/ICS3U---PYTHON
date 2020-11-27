integer = input("integer: ")
list_integer = list(integer)
value = 0

for i in range(len(integer)):
    value+= int(list_integer[i])
        
print(f"{integer} has {len(integer)} digits and their sum is {value}")

