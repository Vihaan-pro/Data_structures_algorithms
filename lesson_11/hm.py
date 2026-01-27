# Treasure Hunt Game using Tree Structure

TreasureTree = {
    "location": "You are at the entrance of an ancient temple",
    "choice1": {
        "option": "Go LEFT into the dark corridor",
        "location": "You enter a dusty corridor",
        "choice1": {
            "option": "Open the GOLDEN CHEST",
            "result": "TREASURE FOUND! You got 1000 Gold Coins! 🎉"
        },
        "choice2": {
            "option": "Ignore the chest and go DEEPER",
            "location": "You find a hidden chamber",
            "choice1": {
                "option": "Drink the mysterious POTION",
                "result": "TRAPPED! You turned to stone! Game Over! 💀"
            },
            "choice2": {
                "option": "Take the ANCIENT SCROLL",
                "result": "You got a map to the real treasure! You earned 500 Gold Coins! 🗺️"
            }
        }
    },
    "choice2": {
        "option": "Go RIGHT into the bright hall",
        "location": "You enter a grand golden hall",
        "choice1": {
            "option": "Take the DIAMOND on the throne",
            "result": "SUCCESS! You got a priceless Diamond! 💎"
        },
        "choice2": {
            "option": "Check the STONE DOOR",
            "location": "Behind the door is a treasure room",
            "choice1": {
                "option": "Take ALL the treasure",
                "result": "You triggered a trap! Game Over! 💣"
            },
            "choice2": {
                "option": "Take only one RUBY",
                "result": "WISE CHOICE! You got a rare Ruby! 💍"
            }
        }
    }
}

def treasure_hunt(node, depth=0):
    """Recursively play the treasure hunt game"""
    
    if "result" in node:
        print(f"\n{'-'*50}")
        print(node["result"])
        print(f"{'-'*50}\n")
        return
    
    if "location" in node:
        print(f"\n[Location {depth+1}] {node['location']}")
    
    if "option" in node:
        print(f"➜ {node['option']}")
    
    # Check which choices are available
    choice1 = node.get("choice1")
    choice2 = node.get("choice2")
    
    if choice1 and choice2:
        print(f"\nChoice 1: {choice1.get('option', 'Unknown')}")
        print(f"Choice 2: {choice2.get('option', 'Unknown')}")
        
        user_choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if user_choice == "1":
            treasure_hunt(choice1, depth + 1)
        elif user_choice == "2":
            treasure_hunt(choice2, depth + 1)
        else:
            print("Invalid choice! Try again.")
            treasure_hunt(node, depth)
    else:
        print("\nGame Ended!")

# Main Game
print("=" * 50)
print("⚔️  TREASURE HUNT ADVENTURE ⚔️")
print("=" * 50)
print("\nWelcome to the ancient temple treasure hunt!")
print("Make wise choices to find the treasure and avoid traps!")

treasure_hunt(TreasureTree)

