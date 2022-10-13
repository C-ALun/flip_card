from tkinter import *
import pandas as pd
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')

#<---Fetching Data---->

try:
    data_file = pd.read_csv('data/french_words.csv')
    data = data_file.to_dict(orient='records')
except FileNotFoundError:
    print('File is not found')

#<----Updating Function---->
def is_cross():
    random_index = random.randint(0,100)
    word = data[random_index]
    canvas.itemconfig(french_word, text=word['French'])
    canvas.itemconfig(english_word, text=word['English'])


def flip():
    new_image = PhotoImage(file='images/card_back.png')
    old_image = PhotoImage(file='images/card_front.png')
    canvas.itemconfig(image=new_image)
    time.sleep(3000)
    canvas.itemconfig(image=old_image)
    is_cross()



#<----UI SETUP---->
window = Tk()
window.title("Falshy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

random_index = random.randint(0,100)
word = data[random_index]
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_front_image)
french_word = canvas.create_text(400, 150, text=word['French'], font=TITLE_FONT)
english_word = canvas.create_text(400, 263, text=word['English'], font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

#<-----Button---->
cross_image = PhotoImage(file='images/wrong.png')
wrong = Button(image=cross_image, bg=BACKGROUND_COLOR, highlightthickness=0
               , command=flip)
wrong.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
right = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0
               , command=flip)
right.grid(row=1, column=1)




window.mainloop()