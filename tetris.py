from enum import Enum

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

    screen = move_pieces(screen, Movement.DOWN)
    screen = move_pieces(screen, Movement.DOWN)
    screen = move_pieces(screen, Movement.DOWN)
    screen = move_pieces(screen, Movement.LEFT)
    screen = move_pieces(screen, Movement.RIGHT)
    screen = move_pieces(screen, Movement.DOWN)
    screen = move_pieces(screen, Movement.DOWN)
    screen = move_pieces(screen, Movement.DOWN)
    screen = move_pieces(screen, Movement.DOWN)
    screen = move_pieces(screen, Movement.DOWN)        
    screen = move_pieces(screen, Movement.DOWN)        
    screen = move_pieces(screen, Movement.DOWN)        
    screen = move_pieces(screen, Movement.DOWN)        
        

def move_pieces(screen: list, movement: Movement) -> list:

    new_screen = [["🔲"] * 10 for _ in range(10)]

    # print_screen(new_screen)

    for row_index, row in enumerate(screen):
        for column_index,item in enumerate(row):
            
            if item == "🔳":    
                new_row_index = 0
                new_column_index = 0                
                match movement:
                    case Movement.DOWN:
                        new_row_index = row_index + 1
                        new_column_index = column_index
                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_column_index = column_index + 1 
                    case Movement.LEFT:
                        new_row_index = row_index
                        new_column_index = column_index - 1
                    case Movement.ROTATE:
                        print("rotate")

                if new_row_index > 9 or new_column_index > 9 or new_column_index < 0: 
                    print("No se puede mover")
                    return screen
                else:
                    new_screen[new_row_index][new_column_index] = "🔲"        
                new_screen[new_row_index][new_column_index] = "🔳"

    print_screen(new_screen)

    return new_screen
def print_screen(screen: list):
    print("\nPantalla de juego:\n")
    for row in screen:
        print("".join(map(str, row)))
    
    
tetris()