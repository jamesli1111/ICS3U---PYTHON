class MarkRangeError(Exception):
    pass
while True:  
    try:
        percentage_mark= float(input("Enter a percentage mark: "))
        if percentage_mark<0 or percentage_mark>100:
            raise MarkRangeError
        break
    except ValueError:
        print(f"Enter a number")
    except MarkRangeError:
        print("Mark is not within possible range")      
print("Thank you!")