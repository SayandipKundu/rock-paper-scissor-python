## **  ROCK PAPER SCISSOR GAME  ** ##

"""
WORKFLOW OF PROJECT :

1- Take input form user (rock , paper , scissor)
2- Coumputer choice (use random module)
3- Result print

Cases :
A- Rock -->
Rock - Rock = tie
Rock - Paper = Paper win
Rock - Scissor = Rock Win
B- Paper -->
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win
C- Scissor -->
Scissor - Scissor = tie
Scissor - Paper = Scissor win
Scissor - Rock = Rock Win

"""





import random

item_list = ["Rock" , "Paper" , "Scissor"]

user_choice = input("Enter your move (Rock , Paper , Scissor) : " )
comp_choice = random.choice(item_list)

print(f"User choice is : {user_choice}")
print(f"Coumputer choice is : {comp_choice}")


if user_choice == comp_choice :
    print("Both chose same := Match Draw .")

elif user_choice == "Rock" :
    if comp_choice == "Paper" :
        print("Paper cover Rock = Coumputer Win .")
    else :
        print("Rock smashes Scissor = You Win .")

elif user_choice == "Paper" :
    if comp_choice == "Rock" :
        print("Paper covers Rock = You Win .")
    else :
        print("Scissor cut the paper = Coumputer Win .")

elif user_choice == "Scissor" :
    if comp_choice == "Paper" :
        print("Scissor cut the paper = You Win .")
    else :
        print("Rock smashes Scissor = Coumputer Win .")