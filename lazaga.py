# filename.py


def letter_to_number(letter):
    return ord(letter.lower()) - ord('a') + 1


print("Welcome to Lazaga's Maze!")
print("Instructions: Use up, left, right, down to move through the maze!")

player_x = letter_to_number('A')
player_y = letter_to_number('A')

treasure_x = letter_to_number('Z')
treasure_y = letter_to_number('Z')

game_running = True

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
    move = input("Enter move (w/a/s/d for directions, q to quit): ").lower()

    if move == "w":
        player_y += 1
    elif move == "s":
        player_y -= 1
    elif move == "a":
        player_x -= 1
    elif move == "d":
        player_x += 1
    elif move == "q":
        print("You quit the game.")
        break

    print(f"Player position: ({player_x}, {player_y})")

    if player_x == treasure_x and player_y == treasure_y:
        print("You found the treasure! You win!")
        break
