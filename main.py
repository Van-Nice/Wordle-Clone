import random
import tkinter as tk

words_path = "assets/word-files/five-letter-words.txt"

with open(words_path, 'r') as words_file:
    words = [line.strip() for line in words_file]

random_word = random.choice(words)
random_word_hashm = {}
# create function that will create a hash map for the word. This hash map will use the letter as it's key and the index position as the value
for i in range(0, len(random_word)):
    random_word_hashm[random_word[i]] = i

root = tk.Tk()
root.title("Character Grid Input")

frame = tk.Frame(root, borderwidth=0, relief="groove")
frame.pack(padx=100, pady=100)

rows = 6
columns = 5
labels = []

for i in range(rows):
    row = []
    for j in range(columns):
        label = tk.Label(frame, text="", height=2, width=4, borderwidth=2.5, relief="solid", font=("Helvetica", 32))
        label.grid(row=i, column=j, padx=5, pady=5)
        row.append(label)
    labels.append(row)

current_row, current_col = 0, 0

def on_key_press1(event):
    global current_row, current_col
    if event.keysym == 'BackSpace':
        if current_col > 0:
            current_col -= 1
        else:
            return
        labels[current_row][current_col].config(text="")
    elif event.char.isalpha():
        labels[current_row][current_col].config(text=event.char.upper())
        current_col += 1

def get_first_row_letters():
    first_row_letters = []
    for label in labels[0]:
        letter = label.cget("text")
        if letter:
            first_row_letters.append(letter)
    return first_row_letters

enter_button = tk.Button(root, text="Enter", command=lambda: get_first_row_letters())
enter_button.pack()


# handle first row event
# take the first row list and iterate to if each letter is the correct position and change it green, if it is in hashm but not in the correct position change it yellow
# create edge cases for double and triple letters


if current_col <= 5 and current_row == 0:
    root.bind("<Key>", on_key_press1)

labels[0][0].config(foreground="white", background="green")

root.mainloop()



