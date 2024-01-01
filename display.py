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
    for board_piece in board_pieces:
        for each in board_piece:
            pawn_x = each.pos[0] * square_size + 8
            pawn_y = each.pos[1] * square_size + 13

            screen.blit(each.p_icon, (pawn_x, pawn_y))
            # Update the display:
            pygame.display.flip()
