from enum import Enum
from typing import Tuple
from pynput import keyboard

class Movement(Enum):
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    ROTATE = 4

def tetris():
    screen = [["🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"]]

    print_screen(screen)

    rotation = 0

    def on_press(key):
        nonlocal screen, rotation
        try:
            if key == keyboard.Key.esc:
                return False
            elif key == keyboard.Key.left:
                screen, rotation = move_pieces(screen, Movement.LEFT, rotation)
            elif key == keyboard.Key.right:
                screen, rotation = move_pieces(screen, Movement.RIGHT, rotation)
            elif key == keyboard.Key.down:
                screen, rotation = move_pieces(screen, Movement.DOWN, rotation)
            elif key == keyboard.Key.space:
                screen, rotation = move_pieces(screen, Movement.ROTATE, rotation)
        except AttributeError:
            pass

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def move_pieces(screen: list, movement: Movement, rotation: int) -> Tuple[list, int]:
    new_screen = [["🔲"] * 10 for _ in range(10)]

    rotation_item = 0
    rotations = [[(1, 1), (0, 0), (-2, 0), (-1, -1)],
                 [(0, 1), (-1, 0), (0, -1), (1, -2)],
                 [(0, 2), (1, 1), (-1, 1), (-2, 0)],
                 [(0, 0), (0, 0), (0, 0), (0, 0)]]

    new_rotation = rotation
    if movement is Movement.ROTATE:
        new_rotation = 0 if rotation == 3 else rotation + 1

    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):
            if item == "🔳":
                new_row_index = row_index
                new_column_index = column_index
                if movement is Movement.DOWN:
                    new_row_index += 1
                elif movement is Movement.RIGHT:
                    new_column_index += 1
                elif movement is Movement.LEFT:
                    new_column_index -= 1
                elif movement is Movement.ROTATE:
                    new_row_index += rotations[new_rotation][rotation_item][0]
                    new_column_index += rotations[new_rotation][rotation_item][1]
                    rotation_item += 1
                
                if new_row_index > 9 or new_column_index > 9 or new_row_index < 0 or new_column_index < 0:
                    print("No se puede mover")
                    return screen, rotation
                else:
                    new_screen[new_row_index][new_column_index] = "🔳"

    print_screen(new_screen)
    return new_screen, new_rotation

def print_screen(screen: list):
    print("\nPantalla de juego:\n")
    for row in screen:
        print("".join(map(str, row)))

tetris()