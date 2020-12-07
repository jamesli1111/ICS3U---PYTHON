import random

while True:
    your_point = random.randint(1,7)
    roll = random.randint(1,7)
    print(f"Your first roll and point value is: {your_point} ")
    count = 0
    while True:
        roll = random.randint(1,7)
        count = count + 1
        print(f"Next roll is: {roll}")
        if roll == your_point:
            print(f"It took {count} times to get your point again.")
            break 
    play_again = input (f"Would you like to play again? (Y/N): ")
    if play_again == "N":
        break