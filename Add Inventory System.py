# Repository: python-text-adventure
# New Feature: Add inventory system

inventory = []

def start_game():
    """Start the adventure game with an inventory system."""
    print("You are in a dark forest. You see three paths.")
    choice = input("Do you go left, right, or straight? ").lower()
    if choice == "left":
        inventory.append("treasure chest")
        print("You find a treasure chest and add it to your inventory!")
    elif choice == "right":
        print("You encounter a monster!")
    elif choice == "straight":
        print("You discover a hidden village.")
    else:
        print("Invalid choice. Game over.")
    print("Inventory:", inventory)

# Example usage
start_game()
