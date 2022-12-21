import random
ans = None
a = 0
b = 0
z = ["rock", "paper", "scissors"]

while ans != "YOU WON!":
    x = random.choice(z)
    y = input("Ready for Rock, Paper & Scissors! \nChoose one ? \n")
    y = y.lower()

    if y == "quit":
        break
    elif y not in z:
        print("\nPlease choose correct value!! \n")
    elif x == y:
        ans = "Its a DRAW!"
        print(f"\n{ans} \nYou choose: {y}, Computer choose: {x}")
    elif (x == 'rock' and y == "paper") or (x == 'scissors' and y == "rock") or (x == 'paper' and y == "scissors"):
        ans = "YOU WON!"
        a = a + 1
        print(f"\n{ans} \nYou choose: {y}, Computer choose: {x}")
    else:
        ans = "Computer WON!"
        b = b + 1
        print(f"\n{ans} \nYou choose: {y}, Computer choose: {x}")

    print(f"Scores: Computer {b} vs You {a} \n")
