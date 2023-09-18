import math

BACKGROUND_COLOR = "#95d9f0"
GREEN="#07736A"
RED="#730707"
LB="#DBFFFF"

FONT="Courier"
from tkinter import *
import numpy as np


def calculate():
    # d=[15.1, 38.2, 52.3, 60.4, 75.5, 90.6, 105.7, 120.8, 135.9, 151, 167.1, 182.2, 197.3, 212.4, 227.5,
    #    242.6, 257.7, 272.8, 287.9, 303, 318.1, 333.2, 348.3, 363.4, 378.5, 393.6, 408.7]
    canvas2.delete('all')
    global cr
    dir=np.round(np.linspace(15.5,408,14),1)
    conc=float(h.get())
    if conc<=0:
        cr.config(text="Invalid concentration (must be > 0)")
        cr.config(font=(FONT, 12, "bold"), padx=10, pady=10)
        cr.grid(row=5, column=1, columnspan=2)
        return
    # Formula: pH = -log10([H+])
    pH=math.log10(1/conc)
    type=classify(pH)
    cr.config(text=f"pH = {pH}\n{type}")
    cr.config(font=(FONT, 12, "bold"), padx=10, pady=10)
    cr.grid(row=5, column=2, columnspan=2)
    # dirx=int(pH)-1
    canvas2.create_image(420/14*pH, 8, image=arrow)


def classify(pH):
    if pH<7:
        return "Acidic"
    elif pH>7:
        return "Basic"
    else:
        return "Neutral"

def ex():
    exit()

window=Tk()
window.title("pH Calculator")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=100, pady=40)

enterl=Label(text="Enter the concentration of H+ ions in the solution in mol/L:")
enterl.config(font=(FONT, 14, "bold"), padx=5, pady=5)
enterl.grid(row=0, column=1, columnspan=4)

gap=Label(text="   ", bg=BACKGROUND_COLOR)
gap.grid(row=1, column=0)

h=Entry(width=40)
h.insert(0, "0.0000001")
h.grid(row=2, column=2, columnspan=2)
h.focus()

gap=Label(text="   ", bg=BACKGROUND_COLOR)
gap.grid(row=3, column=0)

gen=Button(text="GENERATE pH", command=calculate)
gen.config(font=(FONT, 14, "bold"))
gen.grid(row=4, column=2, columnspan=2)

gap=Label(text="   ", bg=BACKGROUND_COLOR)
gap.grid(row=5, column=0)

canvas=Canvas(width=423, height=53, bg=LB, highlightthickness=0)
scale = PhotoImage(file="s.png")
canvas.create_image(211,26, image=scale)
canvas.grid(row=6, column=0, columnspan=5)
canvas2 = Canvas(width=423, height=20, highlightthickness=0)
arrow = PhotoImage(file="ar_.png")
canvas2.grid(row=7, column=0, columnspan=5)

gap=Label(text="   ", bg=BACKGROUND_COLOR)
gap.grid(row=8, column=0)

e = Button(text="Exit", command=ex)
e.config(font=(FONT, 14, "bold"))
e.grid(row=9, column=2, columnspan=2)

cr = Label(text="",
    bg=BACKGROUND_COLOR, fg="black")
cr.grid(row=5, column=1, columnspan=2)

window.mainloop()