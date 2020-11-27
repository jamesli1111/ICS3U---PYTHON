count = 0

print("Please type 'quit' to stop.")

while True:

    word = input("Enter a word: ")
    if word != "quit":
        count += 1

    else:
        print(f"You entered {count} word(s)")
        break
    
# If the user inputs multiple words on one line with spaces in between, the code will read that one line of multiple words as one word.
# My counter "count" adds one to itself EVERYTIME the user inputs something. 
# So if the user inputs one line with multiple words, the code will still only add 1 to "count" since it recognizes that the user has entered something once.
# When the user enters "quit", my code prints out the number of times the user inputted something: not the number of words actually in that one string.