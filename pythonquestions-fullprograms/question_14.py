def validity_of_number(number):
    try:
        number = float(number)
    except ValueError:
        print(f"That's a non-numerical value! Try again!")

number = input(f"Enter a number: ")
validity_of_number(number)


