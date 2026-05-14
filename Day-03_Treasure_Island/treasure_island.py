print(r'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a junction. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    # Using triple quotes makes the story much easier to edit
    print("""
    You walked 300 meters and reached a river. You have 3 choices:
    1. 'return' - Go back (you lose your chance).
    2. 'swim'   - Brave the water (watch out for crocodiles!).
    3. 'tarzon' - Swing through the trees like a pro.
    """)

    choice2 = input("What is your move? ").lower()

    if choice2 == "return":
        print("Safety first, I guess? You're alive, but broke. Game Over.")
    elif choice2 == "swim":
        print("A crocodile named Magar enjoyed his human snack. YOU ARE DEAD.")
    elif choice2 == "tarzon":
        print("Your grip strength saved you! You crossed the river safely.\n")

        print("You found the treasure chest, but it's locked. There are two doors:")
        print("Type 'pink' for the Pink Door or 'blue' for the Blue Door.")

        choice3 = input("Choose wisely: The  wrong door has a demon who will eat you alive. ").lower()
        if choice3 == "pink":
            print("\nSuccess! You found the key... and a brand new lipstick? Congrats, you win!")
        elif choice3 == "blue":
            print("\n Demon grabs you!You are now frying Allu Tikka for him in case he likes it and makes you his personal chef for eternity. Game Over.")
        else:
            print("\nYou stumbled into a wall while deciding. The demon heard you. Game Over.")
    else:
        print("\nYou stood there indecisively until it got dark. Game Over.")
else:
    print("\nA bear was hiding in the bushes to the right. You are now bear-food. Game Over.")

