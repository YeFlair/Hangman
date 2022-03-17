import random

word_list = ["ardvark", "babbon", "camel"]
chosen_word = random.choice(word_list)
guess = input("Enter A Letter: ").lower()
display = []

for _ in range(len(chosen_word)):
    display += "_"
print(display)

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)