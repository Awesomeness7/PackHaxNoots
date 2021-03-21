import tkinter as tk
import os
import math
import functools
from functools import partial

# List where all the terms are stored
global terms
terms = []
# List where all definitions are stored
global definitions
definitions = []
# List where all the flashcard buttons are stored
global termCard
termCard =[]

# Function that both saves data to a table as well as a text file
def saveData():
    terms.append(term.get())
    with open('terms.txt', 'a') as f:
        f.write(term.get() + '`')
    definitions.append(definition.get())
    with open('definitions.txt', 'a') as f:
        f.write(definition.get() + '`')

def switchText(selfPlacement):
    defFromCard.config(text=definitions[selfPlacement])

# Function that creates a new Term and will be placed in box
def newTermPlace(tCard):
    saveData()
    index = len(termCard)
    # Creates a new button and stores it in a list
    termCard.append(tk.Button(cards, text=tCard, bg=bttnColor,activebackground=bttnAg, wraplength=100, relief="flat", command= lambda : switchText(index))) 
    # Calculates the x position the card needs(Still a work in progress)
    cardRow = int(math.floor(index/7))
    cardCol = int(math.fmod(index, 7))
    termCard[len(termCard) - 1].place(height=50, width=99, x=(cardCol*102)+3, y=(cardRow*53)+3)
    print(terms)
    term.delete(0, len(term.get()))
    definition.delete(0, len(definition.get()))

root = tk.Tk()
root.resizable(False, False)
# Defines the colors we will use
bgColor = "#5999ff"
frColor = "#b8d3ff"
bttnColor = "#418fd9"
bttnAg = '#6aa8e6'

# Creates the overall canvas for enitre program
canvas = tk.Canvas(root, width=1280, height=720, bg=bgColor)
canvas.pack()

# Creates the area where entry happens
settings = tk.Frame(root, bg=frColor, highlightcolor=frColor, highlightthickness=5)
settings.place(x=50, y=50, width=400, height=620)

# Creates the area where the cards will be
cards = tk.Frame(root, bg=frColor, highlightcolor=frColor, highlightthickness=5)
cards.place(x=500, y=50, width=730, height=620)

# Creates the entry space for the terms and labels
termLabel = tk.Label(settings, font=("calibre", 20), text="TERM:", anchor="w")
termLabel.pack(fill="x")
# Creates the box where terms will be entered
term = tk.Entry(settings, fg="black", bg="white", font=("calibre", 20))
term.pack(fill="x")
# Simple label that appears over the definition button
defLabel = tk.Label(settings, font=("calibre", 20), text="DEFINITION:", anchor="w")
defLabel.pack(fill="x")
# Creates the entry box for definitions to be added
definition = tk.Entry(settings, fg="black", bg="white", font=("calibre", 20))
definition.pack(fill="x")
# Creates the label that will display the definition of the card that is clicked on
defFromCard = tk.Label(settings, font=("calibre", 20), text="Click the cards on the right!", wraplength=400)
defFromCard.pack(expand="true")

# Creates button that on click will save the data in the entry box as a term
submit = tk.Button(settings, text="Submit",relief="flat",activebackground="#4fa7ff",bg=bgColor, font=("calibre", 20), command=lambda : newTermPlace(term.get()))
submit.place(width=350, height=100, x=25, y=125)
submit.pack()

# Retrieves all saved terms and turns them into buttons
if os.path.isfile('terms.txt'):
    with open('terms.txt', 'r') as f:
        tempTerms = f.read()
        tempTerms = tempTerms.split('`')
        tempTerms = [x for x in tempTerms if x.strip()]
        terms = tempTerms
        for fterm in terms:
            termIndex = len(termCard)
            # Creates a new button and stores it in a list
            switchTextWithArg = partial(switchText, termIndex)
            termCard.append(tk.Button(cards, text=fterm,bg=bttnColor, activebackground=bttnAg, wraplength=100, relief="flat", command=switchTextWithArg)) 
            # Calculates the x position the card needs(Still a work in progress)
            cardRow = int(math.floor(termIndex/7))
            cardCol = int(math.fmod(termIndex, 7))
            termCard[len(termCard) - 1].place(height=50, width=99, x=(cardCol*102)+3, y=(cardRow*53)+3)
# Retrieves all definitions and puts them into a list for the rest of the program to access
if os.path.isfile('definitions.txt'):
    with open('definitions.txt', 'r') as f:
        tempDef = f.read()
        tempDef = tempDef.split('`')
        tempDef = [x for x in tempDef if x.strip()]
        for fdefs in tempDef:
            definitions.append(fdefs)

root.mainloop()