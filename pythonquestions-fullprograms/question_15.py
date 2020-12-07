class MarkTooLowError(Exception):
    pass
class MarkTooHighError(Exception):
    pass
while True:  
    try:
        percentage_mark= float(input("Enter a percentage mark: "))
        if percentage_mark<0:
            raise MarkTooLowError
        elif percentage_mark>100:
            raise MarkTooHighError
        break
    except ValueError:
        print(f"Enter a number")
    except MarkTooHighError:
        print("Mark cannot be greater than 100")
    except MarkTooLowError:
        print("Mark cannot be negative")        
print("Thank you!")