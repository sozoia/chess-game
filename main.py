from my_classes import *
from display import *


def choose_piese_to_play(x,y,turn):
    '''after the piece choosed ask for new pos'''

    ind = get_piece_at((x,y))
    new_pos_choosed = False
    running = True
    click_count = 0
    
    if not ind:
        return False

    choosed = board_pieces[ind[0]][ind[1]].color

    print(f"choose the new pos for {board_pieces[ind[0]][ind[1]].color}", end="")
    print(f" team at {board_pieces[ind[0]][ind[1]].pos}")
    if choosed == turn[0]:
        valid_moves_display(board_pieces[ind[0]][ind[1]].possible_moves())
    else:
        return False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(f"Left mouse button clicked at ({mouse_x // 75}, {mouse_y // 75})")
                new_pos_choosed = board_pieces[ind[0]][ind[1]].move(mouse_x // 75, mouse_y // 75)
                click_count += 1

        if click_count >= 2 or new_pos_choosed:
            if new_pos_choosed:
                if choosed == "white":
                    turn[0] = "black"
                else:
                    turn[0] = "white"
                return True
            elif not new_pos_choosed:
                '''didn't choose or not valid choise'''
                return False

    pygame.quit()


def main():

    # enter loop and track the game
    running = True
    turn = ["white"]

    board()
    piece_display(board_pieces)

    while running:

        for event in pygame.event.get():
            ''' check for the reactions of the user and control the game'''
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(f"Left mouse button clicked at ({mouse_x // 75}, {mouse_y // 75})")
                choose_piese_to_play(mouse_x // 75, mouse_y // 75, turn)
                board()
                piece_display(board_pieces)

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
