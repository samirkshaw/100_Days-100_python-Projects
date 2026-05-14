import random
from art import logo

print("\nWelcome to the Number Guessing Game!\n")
print("Guess a number between 1 and 100.\n")

number = random.randint(1, 100)
print(logo)
# Level selection with validation
while True:
    level = input("Which level? Press 'H' for Hard, 'E' for Easy: ").strip().upper()
    if level == "H":
        attempt = 5
        break
    elif level == "E":
        attempt = 10
        break
    else:
        print("Invalid choice, please type H or E.\n")

print(f"\nYou have {attempt} attempts. Good luck!\n")

def guess_number(attempt, number):
    guess = int(input("Guess the number: "))

    if guess == number:
        return "won"
    elif guess > number:
        print("Too high!\n")
    elif guess < number:
        print("Too low!\n")

    attempt -= 1
    print(f"Attempts remaining: {attempt}\n")
    return attempt

# Game loop
while attempt > 0:
    result = guess_number(attempt, number)

    if result == "won":
        print("You guessed right! You Won! 🎉")
        break
    else:
        attempt = result

if attempt == 0:
    print(f"Out of attempts! The number was {number}. Better luck next time!")

