import random
Rock =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
Paper
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors
""")
RPS =[Rock, Paper, Scissors]
a =int(input("choose 0 for Rock, 1 for Paper, 2 for Scissors\n"))
b =random.randint(0,2)
if a <=2 and a >=0 :
    print("You chose" + "\n" +RPS[a])
    print("Computer choose"+"\n" +RPS[b])

if 0 <= a <= 2:
    if a == b:
        print("It's a Draw")
    elif (a - b) % 3 == 1:
        print("You Win!")
    else:
        print("You Lose!")
else:
    print("Invalid input")






