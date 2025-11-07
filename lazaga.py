# filename.py

# Let's assume your first name starts with 'A' and your last name ends with 'Z'
# Convert the first letter of your first name to a number and last letter of your last name to a number

def letter_to_number(letter):
    return ord(letter.lower()) - ord('a') + 1


# Assign player coordinates based on your first name
# Replace 'A' with the first letter of your first name
player_x = letter_to_number('A')
# Replace 'A' with the first letter of your first name
player_y = letter_to_number('A')

# Assign treasure coordinates based on your last name
# Replace 'Z' with the last letter of your last name
treasure_x = letter_to_number('Z')
# Replace 'Z' with the last letter of your last name
treasure_y = letter_to_number('Z')

game_running = True

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
    move = input("Enter move (w/a/s/d for directions, q to quit): ").lower()

    if move == "Up":  # Up
        player_y += 1
    elif move == "Down":  # Down
        player_y -= 1
    elif move == "Left":  # Left
        player_x -= 1
    elif move == "Right":  # Right
        player_x += 1
    elif move == "Quit":  # Quit the game
        print("You quit the game.")
        break


