import random

choice = int(input("Please pick and option:\n 1.rock\n 2.paper\n 3.scissors\n"))

if choice == 1:
    user_choice = 'Rock'
elif choice == 2:
    user_choice = 'Paper'
else:
    user_choice = 'Scissors'

print("Your choice is: " + user_choice + "\nNow its the computer's turn")

comp_list = ['Rock','Paper','Scissors']

comp_choice = random.choice(comp_list)

print("Computer's choice is: " + comp_choice)

if user_choice == comp_choice:
    print("Its a tie, no winner")
elif (user_choice == 'Rock' and comp_choice =='Paper') or (user_choice == 'Rock' and comp_choice == 'Scissors') or (user_choice == 'Scissors' and comp_choice == 'Paper'):
    print("You win!")
else:
    print("You lose!")

