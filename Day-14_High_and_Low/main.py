import random
import data
import art

print(art.logo)
print("Welcome to the Higher or Lower game.")
print("Guess which personality has more followers.")
print("Get it right → game continues. Get it wrong → game over.\n")

A = random.choice(data.data)
should_continue = True
score = 0

while should_continue:
    # Pick B — must be different from A
    B = random.choice(data.data)
    while B == A:
        B = random.choice(data.data)

    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")
    print(art.vs)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")

    choice = input("\nWho has more followers? Type A or B: ").strip().upper()

    if choice == "A" and A["followers"] >= B["followers"]:
        score += 1
        print(f"\nCorrect! Current score: {score}")
        # A stays, B becomes new challenger next round

    elif choice == "B" and B["followers"] >= A["followers"]:
        score += 1
        print(f"\nCorrect! Current score: {score}")
        A = B

    else:
        print(f"\nWrong! {A['name']} has {A['followers']}M vs {B['name']} has {B['followers']}M")
        print(f"Your final score: {score}")
        again = input("\nWould you like to play again? (y/n): ").strip().upper()
        if again == "Y":
            should_continue = True
        else:
            should_continue = False
            print("See you next time!")


