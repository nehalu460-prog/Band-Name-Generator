import random

word = random.choice(["cat", "dog", "sun"])
guessed = ""
chances = 5

print("Welcome to Hangman!")

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if display == word:
        print("You Win 🎉")
        break

    guess = input("Enter a letter: ")
    guessed += guess

    if guess not in word:
        chances -= 1
        print("Wrong! Chances left:", chances)

if chances == 0:
    print("You Lose 💀 Word was:", word)