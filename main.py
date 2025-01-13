import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = []

# ----------------------- Read CSV Data into List ------------------------ #
def get_words_to_learn():
    global to_learn
    try:
        data = pandas.read_csv("./data/words_to_learn.csv")
    except (FileNotFoundError, pandas.errors.EmptyDataError):
        data = pandas.read_csv("./data/french_words.csv")
        data.to_csv("./data/words_to_learn.csv", sep=",", index=False)
    finally:
        to_learn = data.to_dict(orient="records")

# ----------------------- Known/Unknown Button methods ------------------------ #

def word_is_known():
    global current_card

    # remove current card from to_learn dictionary
    to_learn.remove(current_card)

    # write to_learn into words_to_learn.csv
    df = pandas.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)

    # generate next card
    next_card()

def next_card():
    global current_card, flip_timer, to_learn

    # if to_learn list is empty, then refresh it
    if len(to_learn) == 0:
        get_words_to_learn()

    # choose a random card
    current_card = random.choice(to_learn)

    # if window.after timer is running, cancel it
    window.after_cancel(flip_timer)

    # show front of the card with the current word
    canvas.itemconfig(canvas_background, image=img_front)
    canvas.itemconfig(label_language, text="French", fill="black")
    canvas.itemconfig(label_word, text=current_card["French"], fill="black")

    # start timer to flip the card
    flip_timer = window.after(3000, flip_card)

def flip_card():
    # change appearance of canvas to the back of the card, show word translation
    canvas.itemconfig(canvas_background, image=img_back)
    canvas.itemconfig(label_language, text="English", fill="white")
    canvas.itemconfig(label_word, text=current_card["English"], fill="white")

# ------------------------- UI Interface --------------------------- #
# set up window
window = Tk()
window.title("Karte-Memuar")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# set up canvas
img_front = PhotoImage(file="./images/card_front.png")
img_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_background = canvas.create_image(400, 263)
canvas.grid(row=0, column=0, columnspan=2)

# text fields on canvas
label_language = canvas.create_text(
    400,
    150,
    font=("Ariel", 40, "italic")
)
label_word = canvas.create_text(
    400,
    263,
    font=("Ariel", 60, "bold")
)

# "Unknown word" button
img_unknown_word = PhotoImage(file="./images/wrong.png")
button_unknown_word = Button(image=img_unknown_word, command=next_card)
button_unknown_word.grid(row=1, column=0)

# "Known word" button
img_known_word = PhotoImage(file="./images/right.png")
button_known_word = Button(image=img_known_word, command=word_is_known)
button_known_word.grid(row=1, column=1)

# start window timer, 3 seconds to flip the card
flip_timer = window.after(3000, flip_card)

# generate a random word and display
next_card()

# keep window running
window.mainloop()