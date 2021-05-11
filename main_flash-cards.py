
from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_SPANISH = ("Arial", 40, "italic")
FONT_ENGLISH = ("Arial", 50, "bold")
current_card = {}


# RANDOM WORD #

try:
	data_words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
	original_data = pandas.read_csv("./data/english_verbs (2).csv")
	data_dictionary = original_data.to_dict(orient="records")
else:
	data_dictionary = data_words.to_dict(orient="records")

# ----------------------------   Fonctions  ------------------------------- #

def next_card():
	global current_card, flip_timer
	window.after_cancel(flip_timer)
	current_card = random.choice(data_dictionary)

	canvas.itemconfig(title, text="English", fill="black")
	canvas.itemconfig(word_card, text=current_card["English"], fill="black")
	canvas.itemconfig(image_front, image = canvas_image_front)
	flip_timer = window.after(3000, func= return_card)


def return_card():
	canvas.itemconfig(title, text="Spanish", fill = "white")
	canvas.itemconfig(word_card, text= current_card["Spanish"], fill = "white")
	canvas.itemconfig(image_front, image=canvas_image_back)

def words_you_know():
	data_dictionary.remove(current_card)

	words_learn = pandas.DataFrame(data_dictionary)
	words_learn.to_csv("./data/words_to_learn.csv", index = False)
	# print(words_learn)

	next_card()


# ---------------------------- UI  ------------------------------- #

window = Tk()

window.title("Flashy")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer =window.after(3000, func=return_card)

# front card

canvas = Canvas( width = 800, height = 525, highlightthickness = 0, bg=BACKGROUND_COLOR)
canvas_image_front = PhotoImage(file = "./images/card_front.png")
canvas_image_back = PhotoImage(file = "./images/card_back.png")

image_front = canvas.create_image(400,263, image = canvas_image_front)

# Text Front

title = canvas.create_text(400, 150, text="", font=FONT_SPANISH)
word_card = canvas.create_text(400, 263, text="", font=FONT_ENGLISH)

canvas.grid(column = 0 ,  row= 0, columnspan = 2)


# Buttons

wrong_image = PhotoImage(file = "./images/wrong.png")
wrong_button = Button(image= wrong_image, highlightthickness=0, command =next_card )
wrong_button.grid(column= 0, row = 1)

right_image = PhotoImage(file = "./images/right.png")
right_button = Button(image = right_image, highlightthickness=0, command = words_you_know )
right_button.grid(column= 1, row = 1)

espace = Label(text="", bg = BACKGROUND_COLOR)
espace.grid(column= 0, row = 2)
quit_button = Button(text="Quit", highlightthickness=0, font=("Arial", 14, "bold"), command = quit, width=25, bg= BACKGROUND_COLOR)
quit_button.grid(column= 0, row = 3, columnspan = 2)

next_card()

window.mainloop()

