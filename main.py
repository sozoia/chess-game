from my_classes import *
from display import *


def valid_moves_display(list_of_moves):
    ''' print pieces in the board:'''

    # access the pieces and print at position for each piece
    for board_piece in list_of_moves:
        for each in board_piece:
            pawn_x = each.pos[0] * square_size + 8
            pawn_y = each.pos[1] * square_size + 13

            screen.blit(each.p_icon, (pawn_x, pawn_y))
            # Update the display:
            pygame.display.flip()


def choose_piese_to_play(x,y):
    '''after the piece choosed ask for new pos'''

    ind = get_piece_at((x,y))
    new_pos_choosed = False
    running = True
    click_count = 0

    if not ind:
        return False

    print(f"choose the new pos for {board_pieces[ind[0]][ind[1]].color}", end="")
    print(f" team at {board_pieces[ind[0]][ind[1]].pos}")

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
                return True
            elif not new_pos_choosed:
                '''didn't choose or not valid choise'''
                return False

    pygame.quit()



def main():

    # enter loop and track the game
    running = True

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
                choose_piese_to_play(mouse_x // 75, mouse_y // 75)
                board()
                piece_display(board_pieces)

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
