import random

HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "camel", "baboon", "python", "hangman",
             "keyboard", "monitor", "elephant", "jungle", "wizard" ]

chosen_word = random.choice(word_list)
lives = 6
guessed_letters = []                        #  tracks what's been tried
display = ["_"] * len(chosen_word)

print("Welcome to the Hangman game.")
print("You have the choose the correct alphabets of the random word.\n Every wrong choice takes the hangman closer to be hanged.")
print(HANGMANPICS[0])
print("Word: " + " ".join(display))

while "_" in display and lives > 0:

    print(f"Guessed so far: {guessed_letters}")
    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    #  Duplicate check
    if guess in guessed_letters:
        print(f"You already tried '{guess}'. Pick a different letter!")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("\nGood guess!")
        for i in range(len(chosen_word)):    # update every matching position
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print(HANGMANPICS[6 - lives])
        print(f"Wrong! {lives} lives remaining.")

    print("Word: " + " ".join(display))

# Final result
if lives == 0:
    print(f"\nGame over! The word was: {chosen_word}")
else:
    print(f"\nYou win! The word was: {chosen_word} 🎉")


