import random

limit = int(input("Enter your range: "))

computer = random.randint(1,limit)
counter = 0

while counter < 10:
    player = int(input(f"Enter your number(1 to {limit}): "))
    counter += 1
    if player == computer:
        print(f"You found it!:{computer}, in {counter} tries.")
        break
    elif player < computer:
        print("Higher, Try again!")
    elif player > computer:
        print("Lower, Try again!")
    if counter == 10:
        print(f"You couldn't find the number {computer}!")