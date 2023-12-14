import random
import tkinter as tk

words_path = "assets/word-files/five-letter-words.txt"

with open(words_path, 'r') as words_file:
    words = [line.strip() for line in words_file]

random_word = random.choice(words)

def guess1():
    guess = input("Enter a 5 letter word:\n")
    if len(guess) > 5 or len(guess) < 5 or guess.isalpha() == False:
        print("Invalid input, must be 5 characters and alphabetic")
        guess1()
    return guess

# Graphic User Interface
root = tk.Tk()

root.geometry("500x700")
root.title("Wordle V2")

textbox_frame = tk.Frame(root)
textbox_frame.columnconfigure(0, weight=1)
textbox_frame.columnconfigure(1, weight=1)
textbox_frame.columnconfigure(2, weight=1)
textbox_frame.columnconfigure(3, weight=1)
textbox_frame.columnconfigure(4, weight=1)

# Row 1
# Box 1
textbox1 = tk.Text(textbox_frame, height=3, font=('Arial', 16))
textbox1.grid(row=0, column=0, sticky=tk.W+tk.E)

# Box 2
textbox2 = tk.Text(textbox_frame, height=3, font=('Arial', 16))
textbox2.grid(row=0, column=1, sticky=tk.W+tk.E)

# Box 3
textbox3 = tk.Text(textbox_frame, height=3, font=('Arial', 16))
textbox3.grid(row=0, column=2, sticky=tk.W+tk.E)

# Box 4
textbox4 = tk.Text(textbox_frame, height=3, font=('Arial', 16))
textbox4.grid(row=0, column=3, sticky=tk.W+tk.E)

# Box 5
textbox5 = tk.Text(textbox_frame, height=3, font=('Arial', 16))
textbox5.grid(row=0, column=4, sticky=tk.W+tk.E)

textbox_frame.pack(fill='x')


root.mainloop()

# create game loop
run = True
while run:
    print("Welcome to wordle v2!\nThe rules are the same as wordle you get 6 tries to guess a 5 letter word!\n")
    guess1()
    run = False


