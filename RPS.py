import random

print("Let's Play Rock Paper Scissors!")

options = ["r","p","s"]

computer_choice = random.choice(options)
player_choice = input("Make your choice: (r)ock, (p)aper, (s)cissors? ")

#star conditionals
if (player_choice == "p" and computer_choice == "p"):
    print("It's a tie!")

if (player_choice == "p" and computer_choice == "r"):
    print("Humanity wins!")

if (player_choice == "p" and computer_choice == "s"):
    print("AI Takeover!")

if (player_choice == "r" and computer_choice == "s"):
    print("Humanity wins!")
    
if (player_choice == "r" and computer_choice == "r"):
    print("It's a tie!")

if (player_choice == "r" and computer_choice == "p"):
    print("AI Takeover!")
                
if (player_choice == "s" and computer_choice == "s"):
    print("It's a tie!")
    
if (player_choice == "s" and computer_choice == "r"):
    print("AI Takeover!")

if (player_choice == "s" and computer_choice == "p"):
    print("Humanity wins!") 

else:
    print("Please enter 'r' 's' or 'p'")
