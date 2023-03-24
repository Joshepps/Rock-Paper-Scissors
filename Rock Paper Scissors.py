from random import randint

#we bout to make some rock paper scissors
t = ["Rock", "Paper", "Scissors"]
#and our skilled opponent
computer = t[randint(0,2)]
player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("Try to be better.", computer, "covers", player)
        else:
            print("I guess you win.", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("Sucks to suck.", computer, "cut", player)
        else:
            print("Victory!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("Get rekt", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("How about you spell the input correctly?")

    player = False
    computer = t[randint(0,2)]
        
        
