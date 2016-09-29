import tkinter
#...and for creating random numbers.
import random

#the list of possible colour.
colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown','Cyan']
#initial score
score=0
#timer
timeleft=30

def startGame(event):

    if timeleft == 30:
        countdown()

    nextColour()

def nextColour():

    global score
    global timeleft

    if timeleft > 0:

        e.focus_set()

        if e.get().lower() == colours[1].lower():
            score += 1
            #increase the time left by 2 seconds if the input is correct.
            timeleft += 2

        #clear the input box
        e.delete(0, tkinter.END)

        random.shuffle(colours)
        #changing the text and the colour to a random colour value
        label.config(fg=str(colours[1]), text=str(colours[0]))
        #update the score
        scoreLabel.config(text="Score: " + str(score))

#a countdown timer function.
def countdown():

    global timeleft

    if timeleft > 0:

        timeleft -= 1
        #update the time left label.
        timeLabel.config(text="Time left: " + str(timeleft))
        #run the function again after 1 second
        timeLabel.after(1000, countdown)

#create a GUI window.
root = tkinter.Tk()

root.title("Color Game")
#size of window
root.geometry("375x230")

instructions = tkinter.Label(root, text="Type in the color of the words, and not the word text!\nYou have these options: Red,Blue,Green,\nPink,Black,Yellow,Orange,White,Purple,Brown,Cyan", font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

#For displaying the colours.
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

#input field
e = tkinter.Entry(root)
#run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)
e.pack()
#set focus on the input field
e.focus_set()

root.mainloop()