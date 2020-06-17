import random
import tkinter
from tkinter import *
stats = []

def get_winner(call):
    choicelist = ['rock','paper','scissors']
    throw = random.choice(choicelist)

    if (throw == 'rock' and call =='paper') or (throw == 'scissors' and call == 'rock') or (throw == 'paper' and call == 'scissors'):
        stats.append('W')
        result = "You won!"
    elif throw == call:
        stats.append('D')
        result = "It's a draw"
    else:
        stats.append('L')
        result = "You lost"

    global output
    output.config(text="Computer did: " + throw + "\n" + result)

def pass_s():
    get_winner("scissors")

def pass_r():
    get_winner("rock")

def pass_p():
    get_winner("paper")


window = tkinter.Tk()
window.geometry("500x250+800+100")
def end_game():
    window.destroy()

bottomframe = Frame(window)
bottomframe.pack( side ="bottom")
window.title("Rock-Paper-Scissors Game")
welcome = tkinter.Label(window, width=50, height=5, fg="red", text="Welcome To Boredom Incorporation, Play On!")
rock = tkinter.Button(window, text="Rock", highlightbackground="#80ff80", fg="black", padx=10, pady=5, command=pass_r, width=20)
paper = tkinter.Button(window, text="Paper", highlightbackground="#3399ff", padx=10, pady=5, command=pass_p, width=20)
scissors = tkinter.Button(window, text="Scissors", highlightbackground="#ff9999", padx=10, pady=5, command=pass_s, width=20)
output = tkinter.Label(window, width=20, fg="red", text="What's your call?")
gameend = tkinter.Button(bottomframe, text="End game", highlightbackground="black", padx=10, pady=5, command=end_game, width=20)


welcome.pack()
rock.pack(side="left")
paper.pack(side="left")
scissors.pack(side="left")
output.pack(side="right")
gameend.pack(side="bottom")
window.mainloop()

for i in stats: print(i, end=" ")
if stats.count('L') > stats.count('W'):
    result = "\n You lose the series"
elif stats.count('L') == stats.count('W'):
    result = "\n Series ended in a draw"
else:
    result = "\n You win the series"

print(result)

