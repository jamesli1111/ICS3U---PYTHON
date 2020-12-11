import random
count = 0
game_type = input (f"Do you want to:\n1. Choose a number between 1 and 100 or\n2. Choose the bounds for a random number?\n")

if game_type == "1":
     
    while True:
            generated_number = random.randint(1,101)
            guess = int(input("What is your guess?"))
            count += 1

            if guess == generated_number:
                print (f"Congratulations, you got the correct number in {count} guesse(s)")
                break
        

