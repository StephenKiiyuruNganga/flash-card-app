import json
import random
import tkinter
from tkinter import messagebox
import pandas


BACKGROUND_COLOR = "#B1DDC6"
FONT_FAMILY = "Ariel"

# ---------------------------- REMOVE KNOWN WORDS ------------------------------- #


def update_words():
    words_to_learn.remove(current_word)
    df = pandas.DataFrame(words_to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    generate_word()

# ---------------------------- FLIP CARD ------------------------------- #


def flip_card():
    canvas.itemconfig(displayed_img, image=back_img)
    canvas.itemconfig(title_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=current_word["English"])


# ---------------------------- GENERATE A WORD ------------------------------- #


def generate_word():
    global current_word, flip_timer
    if len(words_to_learn) == 0:
        window.after_cancel(flip_timer)
        canvas.itemconfig(title_text, text="Finished!", fill="black")
        canvas.itemconfig(word_text, text="", fill="black")
    else:
        window.after_cancel(flip_timer)
        current_word = random.choice(words_to_learn)
        canvas.itemconfig(displayed_img, image=front_img)
        canvas.itemconfig(title_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=current_word["French"], fill="black")
        flip_timer = window.after(3000, flip_card)


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

# globals
flip_timer = window.after(3000, flip_card)
current_word = None

# card canvas
canvas = tkinter.Canvas(height=526, width=800,
                        highlightthickness=0,
                        bg=BACKGROUND_COLOR)
front_img = tkinter.PhotoImage(file="./images/card_front.png")
back_img = tkinter.PhotoImage(file="./images/card_back.png")
displayed_img = canvas.create_image(400, 263, image=front_img)
title_text = canvas.create_text(
    400, 150, text="Title", font=(FONT_FAMILY, 40, "italic"))
word_text = canvas.create_text(
    400, 236, text="word", font=(FONT_FAMILY, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
check_mark_img = tkinter.PhotoImage(file="./images/right.png")
correct_btn = tkinter.Button(image=check_mark_img,
                             highlightthickness=0,
                             command=update_words)
correct_btn.grid(row=1, column=1)
x_mark_img = tkinter.PhotoImage(file="./images/wrong.png")
wrong_btn = tkinter.Button(image=x_mark_img,
                           highlightthickness=0,
                           command=generate_word)
wrong_btn.grid(row=1, column=0)

# load data
try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")
finally:
    words_to_learn = df.to_dict(orient="records")
    generate_word()

window.mainloop()
