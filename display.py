import pygame


pygame.init()

# Set up the display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))

# Determine the size of each square based on the window dimensions
square_size = min(width // 8, height // 8)
square2_size = min(width // (8), height // (8))

# Load images
icon = pygame.image.load("./image/icon1.png")
dot_icon = pygame.image.load("./image/d_dot.jpg")

# Set the title and the icon
pygame.display.set_caption("Chess")
pygame.display.set_icon(icon)


def board():
    # Fill the screen with the chessboard pattern:
    for row in range(8):
        for col in range(8):
            # Calculate the position for each square
            x = (col) * square_size
            y = (row) * square_size

            # Alternate the color of squares to create a chessboard pattern
            color = (255, 255, 255) if (row + col) % 2 == 0 else (144, 238, 200)

            # Draw the square on the screen
            pygame.draw.rect(screen, color, (x, y, square_size, square_size))

def piece_display(board_pieces):
    ''' print pieces in the board:'''

    # access the pieces and print at position for each piece
    # each board_piece is a list of pieces of the same color and type
    for board_piece in board_pieces:
        for each in board_piece:
            pawn_x = each.pos[0] * square_size + 8
            pawn_y = each.pos[1] * square_size + 13

            screen.blit(each.p_icon, (pawn_x, pawn_y))  # draw the piece
            pygame.display.flip() # Update the display


def valid_moves_display(list_of_moves):
    ''' print dots of the valid moves of chosed piece:'''

    # access the postions and print a dot at each position
    for each in list_of_moves:
        pawn_x = each[0] * square_size + 30
        pawn_y = each[1] * square_size + 30

        screen.blit(dot_icon, (pawn_x, pawn_y))
        # Update the display:
        pygame.display.flip()
