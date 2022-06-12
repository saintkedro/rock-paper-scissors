import random

while True:
    player = None
    choices = ["r","p","s"]
    computer = random.choice(choices).lower()
    player = input("What is your choice? 'R' for Rock, 'P' for Paper, 'S' for Scissors:\n").lower()
    while player not in choices:
        player = input("You picked a wrong option! Pick 'R' for Rock, 'P' for Paper, 'S' for Scissors:\n").lower()

    if player == computer:
            print("You selected the same option as the CPU:")
            print("It's a Tie!")

    elif player == "r":
        if computer == "p":
                print("CPU (Paper)")
                print("Player (Rock)")
                print("You lose!")
        if computer == "s":
                print("CPU (Scissors)")
                print("Player (Rock)")
                print("You win!")

    elif player == "p":
        if computer == "r":
                print("CPU (Rock)")
                print("Player (Paper)")
                print("You win!")
        if computer == "s":
                print("CPU (Scissors)")
                print("Player (Paper)")
                print("You lose!")

    elif player == "s":
        if computer == "r":
                print("CPU (Rock)")
                print("Player (Scissors)")
                print("You lose!")
        if computer == "p":
                print("CPU (Paper)")
                print("Player (Scissors")
                print("You win!")



