import random

# Mapping shown to the user
print("Choose: 1 = Rock, 2 = Paper, 3 = Scissors")
try:
    user = int(input("Enter your choice (1/2/3): ").strip())
except ValueError:
    print("Invalid input. Please enter a number 1, 2 or 3.")
    raise SystemExit

if user not in (1, 2, 3):
    print("Invalid choice. Use 1, 2 or 3.")
    raise SystemExit

bot = random.randint(1, 3)

# Helper to display choices
def name(n):
    return "Rock" if n == 1 else ("Paper" if n == 2 else "Scissors")

print(f"You: {name(user)}  |  Bot: {name(bot)}")

# Nested if decision logic
if user == 1:  # user chooses Rock
    if bot == 1:
        print("Tie.")
    else:
        if bot == 2:
            print("Bot wins. Paper covers Rock.")
        else:  # bot == 3
            print("You win. Rock crushes Scissors.")
elif user == 2:  # user chooses Paper
    if bot == 2:
        print("Tie.")
    else:
        if bot == 3:
            print("Bot wins. Scissors cut Paper.")
        else:  # bot == 1
            print("You win. Paper covers Rock.")
else:  # user == 3 -> Scissors
    if bot == 3:
        print("Tie.")
    else:
        if bot == 1:
            print("Bot wins. Rock crushes Scissors.")
        else:  # bot == 2
            print("You win. Scissors cut Paper.")

            # do 10 times