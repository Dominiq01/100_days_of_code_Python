import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_FAMILY = "Arial"
TIMER_VALUE = 4000 # in milliseconds

try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_data = pandas.read_csv("data/french_words.csv")

words_data_dict = words_data.to_dict(orient="records")


timer = None
random_word = {}

def flip_card():
    canvas.itemconfig(card_img, image=card_back_image)
    canvas.itemconfig(word, text=f"{random_word["English"]}", fill="white")
    canvas.itemconfig(title, text="English", fill="white")
    window.after_cancel(timer)

def next_card(button_id):
    global timer, random_word, words_data_dict
    print(words_data_dict)
    if timer:
        window.after_cancel(timer)
    if button_id == "right" and random_word:
        words_data_dict.remove(random_word)
        new_data = pandas.DataFrame(words_data_dict)
        new_data.to_csv("data/words_to_learn.csv", index=False)

    canvas.itemconfig(card_img, image=card_front_img)
    random_word = random.choice(words_data_dict)
    canvas.itemconfig(word, text=f"{random_word["French"]}", fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    timer = window.after(ms=TIMER_VALUE, func=flip_card)



# ------------------ UI ---------------------------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

title = canvas.create_text(400, 150, text="French", font=(FONT_FAMILY, 30, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT_FAMILY, 40, "bold"))

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=lambda: next_card("wrong"))
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=lambda: next_card("right"))
right_btn.grid(column=1, row=1)

# ------------------ UI ---------------------------------------------------------

next_card("")

window.mainloop()
