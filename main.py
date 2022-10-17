from tkinter import *
import pandas as pd
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')

current_card = {}
#<---Fetching Data---->

try:
    data_file = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_file = pd.read_csv('data/french_words.csv')
    data = original_file.to_dict(orient='records')
else:
    data = data_file.to_dict(orient='records')
#<----Updating Function---->
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    data.remove(current_card)
    print(len(data))

    to_learn = pd.DataFrame(data)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#<----UI SETUP---->
window = Tk()
window.title("Falshy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text='title', font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text='word', font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

#<-----Button---->
cross_image = PhotoImage(file='images/wrong.png')
wrong = Button(image=cross_image, bg=BACKGROUND_COLOR, highlightthickness=0
               , command=next_card)
wrong.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
right = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0
               , command=is_known)
right.grid(row=1, column=1)


next_card()

window.mainloop()