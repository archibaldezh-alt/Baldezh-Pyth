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

# Example usage
state = {"location": "forest", "inventory": ["sword"]}
save_game(state)
loaded_state = load_game()
if loaded_state:
    print("Game loaded:", loaded_state)
