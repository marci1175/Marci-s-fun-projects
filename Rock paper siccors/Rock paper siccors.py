import random
import os
import sys
count = 5
roptions = ["rock", "paper","scissors"]
print("Welcome to Marci's rock paper scissors simulator!")
while count > 0:
    ransw = random.choice(roptions)
    print(f"The robot has {count}HPs left!")
    user_ans1 = input("Enter your choice!\n1) Rock\n2) Scissors\n3) Paper\n: ")
    if user_ans1 == "1":
        if ransw == "rock":
            mindegy = input("Draw! Better luck next time!\n")
            os.system('cls')
            continue
        elif ransw == "paper":
            mindegy = input("You lost! Better luck next time!\n")
            os.system('cls')
            continue
        elif ransw == "scissors":
            count = count - 1
            mindegy = input("You won this round, you were lucky! :) \n")
            os.system('cls')
            continue
    if user_ans1 == "2":
        if ransw == "rock":
            mindegy = input("You lost! Better luck next time!\n")
            os.system('cls')
            continue
        elif ransw == "paper":
            count = count - 1
            mindegy = input("You won this round, you were lucky! :) \n")
            os.system('cls')
            continue
        elif ransw == "scissors":
            mindegy = input("Draw! Better luck next time!\n")
            os.system('cls')
            continue
    if user_ans1 == "3":
        if ransw == "rock":
            count = count - 1
            mindegy = input("You won this round, you were lucky! :) \n")
            os.system('cls')
            continue
        elif ransw == "paper":
            mindegy = input("Draw! Better luck next time!\n")
            os.system('cls')
            continue
        elif ransw == "scissors":
            mindegy = input("You lost! Better luck next time\n")
            os.system('cls')
            continue
print("Congratulations!\nYou have succesfully beaten the boss!\n")
szamit1 = input("Press ENTER to restart!")
os.system('cls')
os.startfile(sys.argv[0])
