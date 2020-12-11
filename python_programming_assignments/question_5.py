import random

while True:
    count = 0
    game_type = input (f"Do you want to:\n1. Choose a number between 1 and 100 or\n2. Choose the bounds for a random number?\n")

    if game_type == "1":
        generated_number = random.randint(1,5)

        while True:
            guess = int(input("What is your guess? "))
            count += 1

            if guess == generated_number:
                print (f"Congratulations, you got the correct number in {count} guess(es)")
                break

    elif game_type == "2":
        lowerbound = int(input("What is the lower bound for me to pick a number? "))
        upperbound = int(input("What is the upper bound for me to pick a number? "))
        generated_number = random.randint(lowerbound, upperbound)

        while True:
            guess = int(input("What is your guess? "))
            count += 1

            if guess == generated_number:
                print (f"Congratulations, you got the correct number in {count} guess(es)")
                break
            
    play_again = input(f"Would you like to play again? (Yes/No)")
    if play_again == "No":
        print(f"Thank you for playing")
        break

