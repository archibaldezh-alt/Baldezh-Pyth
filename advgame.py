### **Repository 11: Text-Based Adventure Game**
```python
# Repository: python-text-adventure
# Description: A simple text-based adventure game.

def start_game():
    print("You are in a dark forest. You see three paths.")
    choice = input("Do you go left, right, or straight? ").lower()
    if choice == "left":
        print("You find a treasure chest!")
    elif choice == "right":
        print("You encounter a monster!")
    elif choice == "straight":
        print("You discover a hidden village.")
    else:
        print("Invalid choice. Game over.")

import json

def save_game(state, filename="savegame.json"):
    with open(filename, 'w') as file:
        json.dump(state, file)
    print(f"Game saved to {filename}")

def load_game(filename="savegame.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved game found.")
        return None

# Example usage in the game loop
state = {"location": "forest", "inventory": ["sword"]}
save_game(state)
loaded_state = load_game()
if loaded_state:
    print("Game loaded:", loaded_state)
