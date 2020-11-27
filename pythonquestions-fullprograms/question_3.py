'''
This program verifies the validity of scores entered
'''
class Error(Exception):
    pass

class MarkRangeError(Error):
    pass


while True:
    
    try:

        percentage_mark= int(input("Enter a percentage mark: "))

        if percentage_mark<0 or percentage_mark>100:

            raise MarkRangeError

        break

    except MarkRangeError:
        print("Invalid mark!")
        print()
    
print("Thank you!")