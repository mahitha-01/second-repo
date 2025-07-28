import random
item_list = ["rock", "paper", "scissor"]

user_choice = input("enter your move = rock, paper, scissor= ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice :
    print("both chooses same: = Match tie")

elif user_choice == "rock" :
    if comp_choice == "paper" :
        print("paper covers rock = Computer win")
    else :
        print("rock smashes scissor = You win")

elif user_choice == "paper" :
    if comp_choice == "scissor" :
        print("scissor cuts paper = Computer win")
    else:
        print("paper covers rock, ypu win")

elif user_choice == "scissor" :
    if comp_choice == "paper":
        print("scissor cuts paper = You win")
    else:
        print("rock smashes scissor = Computer win")

