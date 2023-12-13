with open('words.txt', 'r') as words, open('five-letter-words.txt', 'w') as five_letter_words:
    for line in words:
        if len(line) == 6 and line.rstrip('\n').isalpha():
            five_letter_words.write(line)
