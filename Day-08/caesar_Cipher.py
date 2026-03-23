import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
print("Welcome to the Caesar cipher.\nOne of the oldest encyption method in history.\n")

def caesar(text, shift, direction):
    result = ""

    if direction == "decode":
        shift = -shift

    for letter in text:
        if letter in alphabet:                          # skip spaces, symbols
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            result += alphabet[new_position]
        else:
            result += letter                            # keep spaces/symbols as-is

    print(f"The {direction}d text is: {result}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number (1-25): ")) % 26

    caesar(text, shift, direction)

    restart = input("\nDo you want to go again? (yes/no): ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")