import random
options=("Rock","paper","scissors")
running=True
while running:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("enter a choice(Rock,paper,scissors):")
        print(f"player:{player}")
        print(f"computer:{computer}")
        if player==computer:
            print("TIE")
        elif player=="Rock" and computer=='scissors':
            print("WON")
        elif player=='paper' and computer=="Rock":
            print("WON")
        elif player=="scissors" and  computer=="paper":
            print("WON")
        else:
            print("LOOSE")

        if not input("play again ?(yes/no)").lower()=="yes":
            running=False
print("Thanks for playing")

