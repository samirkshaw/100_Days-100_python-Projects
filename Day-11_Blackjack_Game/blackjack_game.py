import random
from art import logo

card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck = card_values * 4
random.shuffle(deck)

def deal_card():
    return deck.pop()

player_hand = [deal_card(), deal_card()]
dealer_hand = [deal_card(), deal_card()]
print(logo)
print(f"Your hand: {player_hand}  → Total: {sum(player_hand)}")
print(f"Dealer shows: [{dealer_hand[0]} , __]")

player_bust = False

while True:
    if sum(player_hand) > 21:
        print(f"Bust! You went over with {sum(player_hand)}")
        player_bust = True
        break

    move = input("\nHit (H) or Stand (S)? ").strip().upper()

    if move == "H":
        new_card = deal_card()
        player_hand.append(new_card)
        print(f"\nYour hand: {player_hand}  → Total: {sum(player_hand)}")

    elif move == "S":
        print(f"\nDealer shows: {dealer_hand}  -> total: {sum(dealer_hand)}")
        while sum(dealer_hand) < 17:
            print("Dealer total under 17 — dealer draws.")
            dealer_hand.append(deal_card())
            print(f"Dealer shows: {dealer_hand}  -> total: {sum(dealer_hand)}")
        break

# Final result
if not player_bust:
    if sum(dealer_hand) > 21:
        print("Dealer Bust! You win! 🎉")
    elif sum(player_hand) > sum(dealer_hand):
        print("You win! 🎉")
    elif sum(player_hand) == sum(dealer_hand):
        print("It's a tie! 🤝")
    else:
        print("Dealer wins! 🃏")
