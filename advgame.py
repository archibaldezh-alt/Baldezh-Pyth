### **Repository 11: Text-Based Adventure Game**
```python
# Repository: python-text-adventure
# Description: A simple text-based adventure game.

def start_game():
    """Start the adventure game."""
    print("You are in a dark forest. You see two paths.")
    choice = input("Do you go left or right? ").lower()
    if choice == "left":
        print("You find a treasure chest!")
    elif choice == "right":
        print("You encounter a monster!")
    else:
        print("Invalid choice. Game over.")

# Example usage
start_game()
